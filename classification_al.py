import operator
from sklearn import tree

class ActiveLearning:

    def __init__(self, budget=200, iteration_budget=10, k=5):
        '''

        :param budget: total labelling budget
        :param iteration_budget: number of pairs being labelled in each iteration
        :param k: number of classifiers generated by bootstrapping
        '''
        self.budget = budget
        self.iteration_budget = iteration_budget
        self.k = k


    def active_learning(self, sim_vec_dict, true_match_set):
        try:
            import numpy as np
            import sklearn.tree
        except:
            print('Either the "numpy" or "sklearn" modules is not installed! Aborting.')
            print('')

            return set(), set()  # Return two empty sets so program continues
        num_train_rec = len(sim_vec_dict)
        num_features = len(list(sim_vec_dict.values())[0])

        print('  Number of training records and features: %d / %d' % \
              (num_train_rec, num_features))

        #all similarity vectors
        all_train_data = np.zeros([num_train_rec, num_features])
        # class label 0 and 1 for each vector in all_train_data
        all_train_class = np.zeros(num_train_rec)

        rec_pair_id_list = []

        num_pos = 0
        num_neg = 0
        i = 0
        # initialization of numpy arrays representing the similarity vectors and the corresponding classes
        for (rec_id1, rec_id2) in sim_vec_dict:
            rec_pair_id_list.append((rec_id1, rec_id2))
            sim_vec = sim_vec_dict[(rec_id1, rec_id2)]

            all_train_data[:][i] = sim_vec

            if (rec_id1, rec_id2) in true_match_set:
                all_train_class[i] = 1.0
                num_pos += 1
            else:
                all_train_class[i] = 0.0
                num_neg += 1
            i += 1


        num_all = num_pos + num_neg
        print('  Number of positive and negative records: %d / %d' % \
              (num_pos, num_neg))
        print('')
        # initial training data for active learning method
        seed_index = np.random.choice(all_train_class.shape[0], self.iteration_budget, replace=False)
        current_train_vectors = all_train_data[seed_index]
        current_train_class = all_train_class[seed_index]
        # remove selected vectors and classes from original vectors resp. classes
        unlabeled_vectors = np.delete(all_train_data, seed_index, axis=0)
        unlabeled_classes = np.delete(all_train_class, seed_index, axis=0)
        # set the number of used budget to the number of selected seed vectors
        used_budget = current_train_vectors.shape[0]
        # iterative active learning method

        # train decision tree using the generated training data set
        # init DecisionTrees
        while used_budget < self.budget:
            # generate k models based on bootstrapping
            classifiers = []
            # ADD classifier generation code here
            selector = np.array(np.arange(len(current_train_vectors)))

            # Number of records for each decision tree to train
            n = len(selector)//self.k
            for i in range(self.k):
                np.random.shuffle(selector)
                decision_trees = [tree.DecisionTreeClassifier() for _ in range(self.k)]
                dt = decision_trees[i]
                dt.fit(current_train_vectors[selector[:n]], current_train_class[selector[:n]])
                classifiers.append(dt)

            # ADD uncertainty computation code here
            # compute the uncertainty for each similarity vector in unlabelled_vectors
            # dictionary <index in unlabeled_vectors, uncertainty value of the corresponding vector>
            model_results = {ind: sum([classifier.predict([val])[0]/self.k for classifier in classifiers])
                             for ind, val in enumerate(unlabeled_vectors)}

            uncertainties = {ind: [res * (1 - res) for res in model_results.values()][-1]
                             for ind, val in enumerate(unlabeled_vectors)}

            # sort the unlabelled vectors by the computed uncertainty and select new vectors
            candidate_examples = sorted(uncertainties.items(), key=operator.itemgetter(1), reverse=True)[
                                 :min(self.iteration_budget, len(uncertainties))]
            next_batch_idxs = [val[0] for val in candidate_examples]
            new_vectors = unlabeled_vectors[next_batch_idxs]
            new_classes = unlabeled_classes[next_batch_idxs]
            # remove selected vectors and classes from the unlabelled vectors resp. classes
            unlabeled_vectors = np.delete(unlabeled_vectors, next_batch_idxs, axis=0)
            unlabeled_classes = np.delete(unlabeled_classes, next_batch_idxs, axis=0)
            # add the selected vectors and classes to the existing training data set
            current_train_vectors = np.vstack((current_train_vectors, new_vectors))
            current_train_class = np.hstack((current_train_class, new_classes))
            # increase the used budget
            used_budget = current_train_vectors.shape[0]

        decision_tree = tree.DecisionTreeClassifier()
        decision_tree.fit(current_train_vectors, current_train_class)
        # classify all record pairs
        predictions = decision_tree.predict(all_train_data)
        class_match_set = set()
        class_nonmatch_set = set()
        for i in range(num_all):
            rec_id_pair = rec_pair_id_list[i]

            if predictions[i] == 1:
                class_match_set.add(rec_id_pair)
            else:
                class_nonmatch_set.add(rec_id_pair)
        return class_match_set, class_nonmatch_set

from sklearn.decomposition import PCA
from sklearn.svm import SVC
np.random.seed(0)

X = np.load('trainX.py')
Y = np.load('trainY.py')

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

n_components = [10,20,30,40,50]
for i in range(100,10000,100):
	n_components.append(i)
	
for i in n_components:

	pca = PCA(n_components=n_components, svd_solver='randomized',whiten=True).fit(X_train)
	X_train_pca = pca.transform(X_train)
	X_test_pca = pca.transform(X_test)
	print("pca done " + str(i))

	param_grid = {'C': [1e3, 1e4, 1e5],
              'gamma': [0.001, 0.01, 0.1], }
	clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)
	clf = clf.fit(X_train_pca, y_train)
	print("Best estimator found by grid search:")
	print(clf.best_estimator_)
	print(clf.score(X_test,y_test))
	print()

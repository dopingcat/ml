from sklearn import svm, metrics

datas = [[0,0], [1,0], [0,1], [1,1]]
labels = [0, 1, 1, 0]
examples = [[0, 0], [1, 0]]
examples_labels = [0, 1]

clf = svm.SVC()
clf.fit(datas, labels)
results = clf.predict(examples)
print(results)

score = metrics.accuracy_score(examples_labels, results)
print(score)
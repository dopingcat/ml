from sklearn import svm, metrics
import glob, os.path, re, json
import matplotlib.pyplot as plt
import pandas as pd

files = glob.glob("./lang/train/*.txt")
train_data = []
train_label = []

for file_name in files:
    # extract label
    basename = os.path.basename(file_name)
    lang = basename.split("-")[0]   # 책에는 regex 사용
    # extract text
    file = open(file_name, "r", encoding="utf-8")
    text = file.read()
    text = text.lower()
    file.close()
    # rate
    code_a = ord("a")
    code_z = ord("z")
    count = [0 for n in range(0, 26)]
    for character in text:
        code_current = ord(character)
        if code_a <= code_current <= code_z:
            count[code_current - code_a] += 1

    # normalize
    total = sum(count)
    count = list(map(lambda n: n / total, count))

    train_label.append(lang)
    train_data.append(count)

graph_dict = {}
for i in range(0, len(train_label)):
    label = train_label[i]
    data = train_data[i]
    if not (label in graph_dict):
        graph_dict[label] = data

asclist = [[chr(n) for n in range(97, 97 + 26)]]
df = pd.DataFrame(graph_dict, index=asclist)

plt.style.use('ggplot')
df.plot(kind="bar", subplots=True, ylim=(0, 0.15))
plt.savefig("lang-plot.png")
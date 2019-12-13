<<<<<<< HEAD
import argparse
import ast
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
import numpy as np

import check


parser = argparse.ArgumentParser()
parser.add_argument("--n", "-n", help="Number of components for PCA", type=int, default=-1)
parser.add_argument("--k", "-k", help="k value for k-NN", type=int, default=4)
parser.add_argument("--challenge", "-c", help="Add challenge labels", action="store_true")
args = parser.parse_args()


def read_vectors(filename):
    with open(os.path.join("data", filename)) as file:
        return [ast.literal_eval(line) for line in file.read().split("\n")[:-1]]


cee_inject_vectors = read_vectors("CeeInject_w2v.txt")
renos_vectors = read_vectors("Renos_w2v.txt")
cee_inject_train = cee_inject_vectors[:800]
renos_train = renos_vectors[:800]
cee_inject_test = cee_inject_vectors[800:]
renos_test = renos_vectors[800:]
challenge_vectors = read_vectors("Challenge_w2v.txt")

labelled_train = np.concatenate((cee_inject_train, renos_train))

if args.n >= 0:
    pca = PCA(n_components=args.n)
    pca.fit(labelled_train)
    labelled_train = pca.transform(labelled_train)
    cee_inject_test = pca.transform(cee_inject_test)
    renos_test = pca.transform(renos_test)
    challenge_vectors = pca.transform(challenge_vectors)

labels = np.concatenate(([0] * len(cee_inject_train), [1] * len(renos_train)))
neighbors = KNeighborsClassifier(n_neighbors=args.k).fit(labelled_train, labels)
print("Cee Inject:", check.accuracy(neighbors.predict(cee_inject_test), [0] * len(cee_inject_test)))
print("Renos:", check.accuracy(neighbors.predict(renos_test), [1] * len(renos_test)))

if args.challenge:
    golden = [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0]
    print("Challenge:", check.accuracy(neighbors.predict(challenge_vectors), golden))
=======
import argparse
import ast
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
import numpy as np

import check


parser = argparse.ArgumentParser()
parser.add_argument("--n", "-n", help="Number of components for PCA", type=int, default=-1)
parser.add_argument("--k", "-k", help="k value for k-NN", type=int, default=4)
parser.add_argument("--challenge", "-c", help="Add challenge labels", action="store_true")
args = parser.parse_args()


def read_vectors(filename):
    with open(os.path.join("data", filename)) as file:
        return [ast.literal_eval(line) for line in file.read().split("\n")[:-1]]


cee_inject_vectors = read_vectors("CeeInject_w2v.txt")
renos_vectors = read_vectors("Renos_w2v.txt")
cee_inject_train = cee_inject_vectors[:800]
renos_train = renos_vectors[:800]
cee_inject_test = cee_inject_vectors[800:]
renos_test = renos_vectors[800:]
challenge_vectors = read_vectors("Challenge_w2v.txt")

labelled_train = np.concatenate((cee_inject_train, renos_train))

if args.n >= 0:
    pca = PCA(n_components=args.n)
    pca.fit(labelled_train)
    labelled_train = pca.transform(labelled_train)
    cee_inject_test = pca.transform(cee_inject_test)
    renos_test = pca.transform(renos_test)
    challenge_vectors = pca.transform(challenge_vectors)

labels = np.concatenate(([0] * len(cee_inject_train), [1] * len(renos_train)))
neighbors = KNeighborsClassifier(n_neighbors=args.k).fit(labelled_train, labels)
print("Cee Inject:", check.accuracy(neighbors.predict(cee_inject_test), [0] * len(cee_inject_test)))
print("Renos:", check.accuracy(neighbors.predict(renos_test), [1] * len(renos_test)))

if args.challenge:
    golden = [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0]
    print("Challenge:", check.accuracy(neighbors.predict(challenge_vectors), golden))
>>>>>>> 20bc189dd0a395b44ced554429676cef5efbb187

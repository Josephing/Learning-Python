import pickle

aDict = {'a':1, 'b':15, 'z':-99}

pickle.dump(aDict, open("aDict.pickle", "wb"))
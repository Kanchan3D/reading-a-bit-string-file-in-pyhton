'''“Pickling” is the process whereby a Python object
    hierarchy is converted into a byte stream,
    and “unpickling” is the inverse operation, 
    whereby a byte stream (from a binary file or bytes-like object)
     is converted back into an object hierarchy.'''
import pickle

f1=open("abc.xyz",'rb')
data2=pickle.load(f1)
print(data2)
f1.close()

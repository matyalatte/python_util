import numpy as np
import matplotlib.pyplot as plt

#managements a numpy array
class Holder():
    def __init__(self, label="", dtype=np.float32):
        self.label=label
        self.data=np.array([]).astype(dtype)

    def add(self,x):
        self.data = np.append(self.data, x)

    def get(self):
        return self.data

    def mean(self):
        return np.mean(self.data)

    def sum(self):
        return np.sum(self.data)

    def max(self):
        return np.max(self.data)

    def min(self):
        return np.min(self.data)

    def save_as_txt(self, file):
        lines=map(str, self.data.tolist())
        with open(file, "w") as f:
            f.write("\n".join(lines)) 

    def save_as_fig(self, file, title=""):
        fig = plt.figure()
        ax=fig.add_subplot(111, ylabel=self.label, title=title)
        x=np.array(range(len(self.data)))
        ax.plot(x,self.data,label=self.label)
        fig.savefig(file)

#sample
'''
test=Holder(label="test")
for i in range(100):
    test.add(i*3)

print(test.get())
print(test.mean())
print(test.sum())
print(test.max())
print(test.min())
test.save_as_txt("test.txt")
test.save_as_fig("test.png")
'''

#output
'''
[  0.   3.   6.   9.  12.  15.  18.  21.  24.  27.  30.  33.  36.  39.
  42.  45.  48.  51.  54.  57.  60.  63.  66.  69.  72.  75.  78.  81.
  84.  87.  90.  93.  96.  99. 102. 105. 108. 111. 114. 117. 120. 123.
 126. 129. 132. 135. 138. 141. 144. 147. 150. 153. 156. 159. 162. 165.
 168. 171. 174. 177. 180. 183. 186. 189. 192. 195. 198. 201. 204. 207.
 210. 213. 216. 219. 222. 225. 228. 231. 234. 237. 240. 243. 246. 249.
 252. 255. 258. 261. 264. 267. 270. 273. 276. 279. 282. 285. 288. 291.
 294. 297.]
148.5
14850.0
297.0
0.0
'''
此代码主要针对基本的UE、SO模型以及带约束的UE模型进行求解
所采用的基本算法为Frank-Wolfe算法
主要用到的python库为scipy，sympy和math

frank-wolfe算法主要是通过将带线性约束的非线性问题转化为带线性约束的线性问题，再进行求解。

简单网络UE.py主要是前期试验，熟悉算法使用的，其所使用的网络图较为简单（如下图所示）
![image text](https://github.com/jiujiaocjj/test/blob/master/img/3.jpg)

单出发点多ODUE.py与单出发点多ODSO.py两个文件主要是针对单出发点，多目的地的网络的用户平衡配流(如下图所示)
![image text](https://github.com/jiujiaocjj/test/blob/master/img/4.jpg)
具体参数见代码
两个文件不同之处主要对在求解对应步长时的函数不同，即目标函数不同，其他包括约束条件完全相同。

多出发点多ODUE.py与多出发点多ODSO.py两个文件主要是针对多出发点，多目的地的网络的用户平衡配流（如下图所示）
![image text](https://github.com/jiujiaocjj/test/blob/master/img/5.jpg)

之所以区分多出发点与单出发点，是为了体会模型中OD流量等各路径流量之和这一约束条件的重要性，即在单出发点时，流量不存在一种归属性（从1出发的车辆必须到达4，而不是到达其他目的地，从而使得得到的结果更优），所以当路网复杂时，往往会因为前期简单网络的影响而忽略这一关键约束条件。
为了使的解满足OD流量等各路径流量之和这一约束条件，这里采用的是将流量标记，即区分从不同出发点出发的流量，分开设定变量，但这就导致原来x条路段的网络直接变成了n（出发点个数)\* x个变量，不知道除了改变求解算法之外，还有没有其他的方法。
以上的文件中所使用的就是一般化的fw算法,在其中可以随意添加线性约束,都可以求得结果（只要有解）

多OD下的求解路票约束问题-Copy1.ipynb文件主要针对复杂的网络，不可能由人工写出所有的路径再去计算，所以对于这个时候的我们最好采用邻接矩阵的方式来记录网络信息，作为求解的输入数据，再通过深度优先搜索找到各个OD对之间的可行路径集，然后求解。
这个文件中对FW算法做了一定的变形，使他只适用于求解UE和SO问题

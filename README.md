## Ljk's ops utilities

This project is a collection of **scripts(shell or python)** and **python code snippet** which I wrote in the past. I will try to make these code reuse as easy as possible and I hope this can help others.


1. 对数值型列表的追加过程加入对最大值(index:-1)/最小值(index:-2)的维护， 对于需要频繁调用max()/min()方法的场景可大幅提高性能  
    [python.functions.append_list_preserve_extremum()](https://github.com/jkklee/Ljk-ops-utilities/blob/master/python/functions.py#L23)
    ```
    >>> a=[0,1]
	>>> append_list_preserve_extremum(a,-1)
	>>> a
	[0, -1, 1]
	>>> append_list_preserve_extremum(a,8)
	>>> a
	[0, 1, -1, 8]
	>>> append_list_preserve_extremum(a,-2)
	>>> a
	[0, 1, -1, -2, 8]
    ```
2. 对以B为单位的数值返回更可读的size单位（ls命令的-h参数做的事情）  
    [python.functions.get_human_size()](https://github.com/jkklee/Ljk-ops-utilities/blob/master/python/functions.py#L43)
    ```
    >>> get_human_size(100)
	'100.00 B'
	>>> get_human_size(3000)
	'2.93 KB'
	>>> get_human_size(20480)
	'20.00 KB'
	>>> get_human_size(4096000)
	'3.91 MB'
    ```
3. 获取列表的中位数  
    [python.functions.get_median()](https://github.com/jkklee/Ljk-ops-utilities/blob/master/python/functions.py#L1)
    ```
    >>> get_median([1,2,3,4,5,6])
	3.5
	>>> get_median([1,2,3,4,5,6,7])
	4.0
    ```
4. 获取列表的4分位数(参考盒须图思想,用于体现响应时间和响应大小的分布)，以及min和max值  
    [python.functions.get_quartile()](https://github.com/jkklee/Ljk-ops-utilities/blob/master/python/functions.py#L7)
    ```
    >>> get_quartile([1,2,3,4,5,6,7,8,9,10])
	(1, 3.0, 5.5, 8.0, 10)
	>>> get_quartile([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
	(1, 5.5, 10.5, 15.5, 20)
    ```
5. 对uri和args进行抽象化,利于分类  
        默认规则:  
        - uri中若 两个`/`之间 或 `/`和`.`之间仅由正则`[0-9或-_]+`组成,则将其抽象为'\*'  
        - args中所有参数的值抽象为'\*'  
        - 函数返回包含两个元素的元组，分别为url抽象结果和参数部分抽象结果  
    [python.functions.text_abstract()](https://github.com/jkklee/Ljk-ops-utilities/blob/master/python/functions.py#L58)
    ```
    >>> text_abstract('/user/100/article/5')
	('/user/*/article/*', '')
	>>> text_abstract('/user/article/5?commentid=10')
	('/user/article/*', 'commentid=*')
    ```
 6. 监控服务器网卡流量，可同时监控多块网卡  
     [python.netflow-statics.py](https://github.com/jkklee/Ljk-ops-utilities/blob/master/python/netflow-statics.py)  
     ![1](https://s1.51cto.com/wyfs02/M02/81/FD/wKiom1dGuoqS6honAAA8gQMh4e8068.png)  
     ![2](https://s2.51cto.com/wyfs02/M02/81/FC/wKioL1dGu5HDfYfbAABaNXTdogo428.png)  

 

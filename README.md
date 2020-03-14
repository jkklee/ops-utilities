## Ljk's ops utilities

This project is a collection of **scripts(shell or python)** and **python code snippet** which I wrote in the past. I will try to make these code reuse as easy as possible and I hope this can help others.


1. 对数值型列表的追加过程加入对最大值(index:-1)/最小值(index:-2)的维护， 对于需要频繁调用max()/min()方法的场景可大幅提高性能  
    [functions.append_list_preserve_extremum()](https://github.com/jkklee/Ljk-ops-utilities/blob/master/functions.py#L23)
2. 对以B为单位的数值返回更可读的size单位（ls命令的-h参数做的事情）  
    [functions.get_human_size()](https://github.com/jkklee/Ljk-ops-utilities/blob/master/functions.py#L43)
3. 获取列表的中位数  
    [functions.get_median()](https://github.com/jkklee/Ljk-ops-utilities/blob/master/functions.py#L1)
4. 获取列表的4分位数(参考盒须图思想,用于体现响应时间和响应大小的分布)，以及min和max值  
    [functions.get_quartile()](https://github.com/jkklee/Ljk-ops-utilities/blob/master/functions.py#L7)
5. 对uri和args进行抽象化,利于分类  
        默认规则:  
        - uri中若 两个'/'之间 或 '/'和'.'之间仅由"0-9或-或_"组成,则将其抽象为'\*'  
        - args中所有参数的值抽象为'\*'  
    [functions.text_abstract()](https://github.com/jkklee/Ljk-ops-utilities/blob/master/functions.py#L56)
 

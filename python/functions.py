def get_median(sorted_data):
    """获取列表的中位数"""
    half = len(sorted_data) // 2
    return (sorted_data[half] + sorted_data[~half]) / 2


def get_quartile(data):
    """
    获取列表的4分位数(参考盒须图思想,用于体现响应时间和响应大小的分布),以及min和max值
    依赖get_median()函数
    """
    data = sorted(data)
    size = len(data)
    if size == 1:
        return data[0], data[0], data[0], data[0], data[0]
    half = size // 2
    q1 = get_median(data[:half])
    q2 = get_median(data)
    q3 = get_median(data[half + 1:]) if size % 2 == 1 else get_median(data[half:])
    return data[0], q1, q2, q3, data[-1]


def append_list_preserve_extremum(arr, v):
    """
    对数值型列表的追加过程加入对最大值(index:-1)/最小值(index:-2)的维护
    对于需要频繁调用max()方法的场景可大幅提高性能
    arr: 要操作的列表
    v: 要加入的值
    """
    if len(arr) > 0:
        if v >= arr[-1]:
            if len(arr) > 1:
                arr[-1], arr[-2] = arr[-2], arr[-1]
            arr.append(v)
        elif v <= arr[-2 if len(arr)>1 else -1]:
            arr.insert(-1, v)
        else:
            arr.insert(-2, v)
    else:
        arr.append(v)


def get_human_size(n):
    """
    对以B为单位的文件大小返回更可读的size单位
    n: 以B为单位的大小值
    """
    units = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB'}
    i = 0
    while n//1024 > 0 and i < 3:
        n = n/1024
        i += 1
    return format(n, '.2f') + ' ' + units[i]


import re
from urllib.parse import unquote
def text_abstract(text, site=None):
    """
    对uri和args进行抽象化,利于分类
    默认规则:
        uri中若 两个'/'之间 或 '/'和'.'之间仅由"0-9或-或_"组成,则将其抽象为'*'
        args中所有参数的值抽象为'*'
    text: 待处理的内容
    site: 站点名称, 配合配置文件中的abs_special来控制指定站点的特殊规则
    """
    uri_args = text.split('?', 1)
    uri = unquote(uri_args[0])
    args = '' if len(uri_args) == 1 else unquote(uri_args[1])
    # 特殊抽象规则
    if site and site in abs_special:
        for uri_pattern in abs_special[site]:
            if re.search(uri_pattern, uri):
                if 'uri_replace' in abs_special[site][uri_pattern]:
                    uri = re.sub(uri_pattern, abs_special[site][uri_pattern]['uri_replace'], uri)
                if 'arg_replace' in abs_special[site][uri_pattern]:
                    for arg_pattern in abs_special[site][uri_pattern]['arg_replace']:
                        if re.search(arg_pattern, args):
                            args = re.sub(arg_pattern, abs_special[site][uri_pattern]['arg_replace'][arg_pattern], args)
                        else:
                            args = re.sub('=[^&=]+', '=*', args)
                return uri, args
    # uri默认抽象规则(耗时仅为原逻辑的1/3)
    for i in re.findall('/[0-9_-]+(?=[/.]|$)', uri):
        uri = uri.replace(i, '/*', 1)
    return uri, re.sub('=[^&=]+', '=*', args)

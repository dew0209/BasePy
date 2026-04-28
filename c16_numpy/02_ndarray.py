""""""

"""
多维性：支持0维（标量），1维（向量），2维（矩阵）及更高维数组

同性质：所有元素类型必须一致（通过dtype指定）

高效性：基于连续内存块存储，支持向量化运算


属性：
    1.shape：数组的形状：行数和列数 arr.shape
    2.ndim：维度数量 arr.ndim
    3.size：总元素个数：数组中所有元素的总数 arr.size
    4.dtype：元素类型：数组中元素的类型（整数，浮点数等） arr.dtype
    5.T：转置：行变列，列变行  arr.T
    6.itemsize:每个元素占用的内存字节数 arr.itemsize
    7.nbytes：数组总内存占用量：size * itemsize   arr.nbytes
    8.flags：内存存储方式：是否联塑存储（高级优化） arr.flags
    
"""

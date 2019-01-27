# simpleOption
Simple Option module(using QuantLib)

Graph sample:
https://github.com/zaq9/simpleOption/blob/master/example_graph.ipynb


```python

    """ 
    Example1
    ---------
    """
    from simpleOption import *
    #Simple Example
    o = Option('02/P20500')
    op_price = o.v(20625, 20.8, 20190124)
    print(f"{o}@{op_price:.2f}  (nk=20625,IV=20.8%)  jan24 ")
    
    """
    OUTPUT 1
    ---------
    02/P20500@285.49  (nk=20625,IV=20.8%)  jan24
    Example2
    ---------
    #underlying change: 20625 >>20500
    op_price2 = o.v(20500)
    print(f"{o}@{op_price2:.2f} (nk=20500,IV=20.8%)  jan24")
    OUTPUT 2
    ---------
    02/P20500@285.49  (nk=20625,IV=20.8%)  jan24
    Example3
    ---------
    #underlying & IV change: 20625>>20000 &IV=25%
    op_price3 = o.v(20000, 25)
    print(f"{o}@{op_price3:.2f} (nk=20000,IV=25%)  jan24")
    OUTPUT 3
    ---------
    02/P20500@703.62 (nk=20000,IV=25%)  jan24
    Example4
    ---------
    #use keyword
    op = Option('02/P20500')
    op_price4 = op(
        underlying=20250,
        iv=25,
        evaluationDate=20190122
    )
"""







```

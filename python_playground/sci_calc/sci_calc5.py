

import numpy as np
import pandas as pd
import logging

index = [('California', 2000), ('California', 2010),
                ('New York', 2000), ('New York', 2010),
                ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956,
                      18976457, 19378102,
                      20851820, 25145561]

pop = pd.Series(populations, index=index)

index = pd.MultiIndex.from_tuples(index)
print(index)

pop = pop.reindex(index)
print(pop)


logging.basicConfig(level=logging.DEBUG, filename='log.txt')  # , format="%(lineno)d 123"
logging.warning("警告！")
logging.debug("调试信息？")
logging.info("信息？")

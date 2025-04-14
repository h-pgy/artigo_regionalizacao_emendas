from typing import Callable
from functools import wraps
from pandas import DataFrame

def copy_df(func:Callable)->Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):

        if 'df' in kwargs:
            df = kwargs.get('df')
        else:
            df= args[0]
            args = args[1:]
        
        if type(df) is not DataFrame:
            raise ValueError(f'df parameter must be a dataframe: {type(df)}')
        
        df = df.copy()

        if 'df' in kwargs:
            kwargs['df'] = df
        else:
            args = (df, *args)

        result = func(*args, **kwargs)
        return result
    
    return wrapper
from typing import Union

import pandas as pd
import numpy as np


class PMUM:

    def __init__(self) -> None:
        self._dataset = None
        self._y_idx = None
        self._y_hat_idx = None

    def load_dataset(self, x: Union[pd.DataFrame, np.ndarray],
                     y: Union[pd.Series, np.ndarray],
                     y_hat: Union[pd.DataFrame, pd.Series, np.ndarray]) -> None:

        if not isinstance(x, (pd.DataFrame, np.ndarray)):
            raise TypeError('x should be pandas DataFrame or numpy ndarray')

        if not isinstance(y, (pd.Series, np.ndarray)):
            raise TypeError('y should be pandas Series or numpy ndarray')

        if not isinstance(y_hat, (pd.Series, pd.DataFrame, np.ndarray)):
            raise TypeError('y_hat should be pandas Series or DataFrame or numpy ndarray')

        if isinstance(x, pd.DataFrame):
            self._dataset = x.values
        else:
            self._dataset = x.copy()

        if not isinstance(y_hat, np.ndarray):
            y_hat = y_hat.values
        if len(y_hat.shape) == 1:
            y_hat = y_hat.reshape(-1, 1)

        self._dataset = np.hstack((self._dataset, y_hat))

        if isinstance(y, np.ndarray):
            self._dataset = np.hstack((self._dataset, y.reshape(-1, 1)))
        else:
            self._dataset = np.hstack((self._dataset, y.values.reshape(-1, 1)))

        self._y_idx = self._dataset.shape[1] - 1
        self._y_hat_idx = [self._y_idx - i - 1 for i in range(y_hat.shape[1])][::-1]

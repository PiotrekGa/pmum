import pandas as pd

from pmum.pmum import PMUM


def test_load_data():
    x = pd.DataFrame([[1, 1], [2, 3], [4, 5]])
    y = pd.Series([1, 2, 3])
    y_hat1 = pd.Series([2, 2, 3])
    y_hat2 = pd.DataFrame([[2, 2], [1, 1], [3, 3]])

    pmum1 = PMUM()
    pmum1.load_dataset(x, y, y_hat1)
    assert pmum1._dataset.shape == (3, 4)
    assert pmum1._y_idx == 3
    assert pmum1._y_hat_idx == [2]

    pmum2 = PMUM()
    pmum2.load_dataset(x, y, y_hat2)
    assert pmum2._dataset.shape == (3, 5)
    assert pmum2._y_idx == 4
    assert pmum2._y_hat_idx == [2, 3]

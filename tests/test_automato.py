import numpy as np
from sklearn.datasets import make_blobs  # type: ignore

from automato import Automato  # type: ignore


def test_automato_blobs():
    X, y = make_blobs(centers=2, random_state=42)
    aut = Automato(random_state=42).fit(X)
    assert aut.n_clusters_ == 2
    assert (aut.labels_ == y).all() == np.True_

Implementation of the AuToMATo clustering algorithm introduced in [<em>AuToMATo: An Out-Of-The-Box Persistence-Based Clustering Algorithm</em>](https://arxiv.org/abs/2408.06958).

---

__Example of running AuToMATo__

```
>>> from automato import Automato
>>> from sklearn.datasets import make_blobs
>>> X, y = make_blobs(centers=2, random_state=42)
>>> aut = Automato(random_state=42).fit(X)
>>> aut.n_clusters_
2
>>> (aut.labels_ == y).all()
True
```

---

__Installation and requirements__

AuToMATo can be installed via `pip` by running `pip install -U automato`.

Required Python dependencies are specified in `pyproject.toml`. Provided that `uv` is installed, these dependencies can be installed by running `uv pip install -r pyproject.toml`. The environment specified in `uv.lock` can be recreated by running `uv sync`.

---

__Installing AuToMATo from PyPI for `uv` users__

```
$ uv init
$ uv add automato
$ uv run python
>>> from automato import Automato
>>> ...
```

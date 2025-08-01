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

__Requirements__

Required Python dependencies are specified in `pyproject.toml`. Provided that `uv` is installed, these dependencies can be installed by running `uv pip install -r pyproject.toml`. The environment specified in `uv.lock` can be recreated by running `uv sync`.

---

__Example of installing AuToMATo from source for `uv` users__

```
$ git clone github.com/m-a-huber/AuToMATo
$ cd AuToMATo
$ uv sync --no-dev
$ source .venv/bin/activate
$ python
>>> from automato import Automato
>>> ...
```

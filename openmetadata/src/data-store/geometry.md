### Open Geometry

Storing geometric primitives with Open Metadata

# Goal

Open Metadata is plain and verbose. By storing geometry in such a way opens up doors beyond traditional use and may help educate or inspire further analysis of what it takes to serialise geometric primitives into plain data.

Techniques applicable to plain data becomes applicable to previously complex data; such as cascading and maintained history.

# Architecture

* `points`
* `edges`
* `faces`

```
cache
	points
		point
```

3d geometry is defined by a set of points, connected by edges, connected by faces. Moving geometry then is defined by the same three (3) collections, with additional points.
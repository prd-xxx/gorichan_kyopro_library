# LowLink

LowLinkアルゴリズムで、グラフの橋や関節点を効率的に列挙します。  
非再帰で実装しており、PyPyで高速に動作します。  
`build()` が O(V + E) です。  
グラフが非連結でも対応しています。  

## 使い方

* 初期化、構築

```
N = 5
es = [[1,2], [0,2,3], [0,1], [1,4], [3]] #隣接リスト、双方向
lowlink = LowLink(N, es)
lowlink.build()
``` 

* 橋のリスト

`bridges` には、与えられたグラフの橋がリストで格納されます  
橋は `(u,v)` の形式で、`u`が探索時のDFS木における「親」になります  
```
print(lowlink.bridges)
# [(3, 4), (1, 3)]
```

* 関節点のコレクション

`articulation_points` には、与えられたグラフの関節点がsetで格納されます  
(setで実装されているのでご注意ください)  

```
print(lowlink.articulation_points)
# {1, 3}
```

## その他得られるものたち

* `order`

探索時のDFS探索木(森)における訪問順です  

* `low`  

辺(u,v)が橋となるとき、 `order[u] < low[v]` を満たします  

* `dfs_parent`

探索時のDFS探索木(森)における親頂点が格納された配列です  
`dfs_parent[v]` は、vの親が入ります 根なら`-1` です  

* `dfs_child`

探索時のDFS探索木(森)における子頂点の配列が格納された配列です  
`dfs_child[v]` は、vの子頂点の配列です 葉なら空配列です  

* `is_dfs_root`

探索時のDFS探索木(森)における根なら`1`、そうでなければ`0` です  

* `component_num`

探索時のDFS探索森の連結成分数です。連結なら`1`です  



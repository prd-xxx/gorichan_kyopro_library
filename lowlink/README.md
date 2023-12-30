# LowLink

LowLinkアルゴリズムで、グラフの橋や関節点を効率的に列挙します。  
非再帰で実装しており、PyPyで高速に動作します。  
`build()` が O(V + E) です。  

## 使い方

* 初期化、構築

```
N = 4
es = [[1,2], [0,2,3], [0,1], [1]] #隣接リスト、双方向
lowlink = LowLink(N, es)
lowlink.build()
``` 

* 橋のリスト

```
lowlink.bridges
```

* 関節点のコレクション (setで実装されているので必要ならlistにしてください)

```
lowlink.articulation_points
```


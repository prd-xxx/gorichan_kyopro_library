# random_access_deque

Pythonで、ランダムアクセスがO(1)でできる両端キュー、(通称: **ごりちゃんDeque**) です  
以下の記事に詳しく書いています  
https://prd-xxx.hateblo.jp/entry/2020/02/07/114818  

## 使い方

ほとんど上記記事の引用です  

#### 初期化

次のいずれかの形式で初期化します (引数省略可能です)  

```
q = Deque()
q = Deque([10, 20])
q = Deque([10, 20], 500000)
```

* 第1引数 `src_arr` はDequeとして初期化したい配列を指定してください。
両略した場合は空です。

* 第2引数 `max_size` はDeque内部で保持するバッファの初期長さを指定します。
省略した場合は `300000` です。  
必要に応じて動的に大きくなるので基本的に気にすることはありませんが、**何度も初期化を呼び出す場合には10などの小さめの値を指定しておくことを推奨します**  

#### append,pop

この辺は `collections.deque` モジュールと同じ感じで使えます  

```
q = Deque([10, 20])
print(q) # Deque([10, 20])
q.append(30)
print(q) # Deque([10, 20, 30])
q.appendleft(40)
print(q) # Deque([40, 10, 20, 30])
a = q.pop()
print(q, a) # Deque([40, 10, 20]) 30
b = q.popleft()
print(q, b) # Deque([10, 20]) 40
```

#### indexを指定してのget,set

この辺も `deque` モジュールと使い勝手は一緒ですが、listのようにO(1) です！  
Pythonらしく負のindexにも対応しています！

```
q = Deque([10, 20, 30, 40, 50])
a = q[1]
print(q, a) # Deque([10, 20, 30, 40, 50]) 20
q[1] = 60
print(q) # Deque([10, 60, 30, 40, 50])
b = q[-2]
print(q, b) # Deque([10, 60, 30, 40, 50]) 40
q[-2] = 70
print(q) # Deque([10, 60, 30, 70, 50])
```

#### 型変換  

`list(q)` のようにすれば list に変換できます！  
`set(q)` で set に、`list(reversed(q))` で逆順リストに変換できます  
もちろん `len(q)` で要素数も取れます    


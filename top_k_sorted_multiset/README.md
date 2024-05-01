# TopKSortedMultiset

大きい方/小さい方からK個の値の和とかを保持しつつ、自由に追加/削除できるくん  
追加/削除 O(√N) です  
内部でtatyam-primeさんの`SortedMultiset`を2本持ってるだけです  
追加/削除の際に、`topk`側は要素K個以下、`other`側は`topk`が要素K個未満ならば必ず空を保ちます  

## 使い方
本ソースコードを貼り付け、さらにtatyam-primeさんの[SortedMultiset](https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py)を貼り付けるといい感じに動きます  

初期化と使用例は以下の感じです  
初期化の引数1つ目は`k`, 2つ目は初期化配列(Iterableなら良い、省略化)  
`mode_max=False` にすると小さい方からK個を`topk`とします (省略すると大きい方)  

```
# 大きい方から 3個を topk として管理
ts = TopKSortedMultiset(3, [3,1])
print(ts) # {1, 3} | {}
ts.add(4)
print(ts) # {1, 3, 4} | {}
ts.add(1)
print(ts) # {1, 3, 4} | {1}
ts.add(5)
print(ts) # {3, 4, 5} | {1, 1}
ts.discard(4)
print(ts) # {1, 3, 5} | {1}
print(ts.sum_topk, ts.sum_other) # 9 1

# 小さい方から 3個を topk として管理
ts = TopKSortedMultiset(3, [3,1], mode_max=False)
print(ts) # {1, 3} | {}
ts.add(4)
print(ts) # {1, 3, 4} | {}
ts.add(1)
print(ts) # {1, 1, 3} | {4}
ts.add(5)
print(ts) # {1, 1, 3} | {4, 5}
ts.discard(1)
print(ts) # {1, 3, 4} | {5}
print(ts.sum_topk, ts.sum_other) # 8 5
```

`discard()` を呼んだときに該当の要素がないと例外を返すので注意です  
任意の時点で、`sum_topk`, `sum_other` はそれぞれの SortedMultisetの和を保持しています  
和以外のものを管理したくなったらお好みで改造してください  

## 補足など

たぶん同じような役目のコードはheapq2本などで頑張れば書けるのですが、かなりバグりそうなのでやめました (そっちのが計算量軽くなるのでそうしたい気持ちはあります)  
topK でなく、単に最大/最小から取り出しができ、追加/削除ができるheapq実装は[こちら](https://github.com/prd-xxx/gorichan_kyopro_library/tree/main/deletable_heapq)にあるのでこちらも検討ください(宣伝)  

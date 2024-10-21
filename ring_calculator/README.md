# RingCaluculator

周期`N`の円環があって、indexが`from_index`のところから`to_index`のところまで時計回り/反時計回りで距離がどれぐらいかをO(1)で計算します  
ただし、始点を除き1ずつindexが増える方向を時計回りとしています (時計盤と同じです)  

## 使い方

初期化は以下のようにします  
引数1つ目は円環の長さです  
`base_index=1` のように指定すると 1_indexed (つまり1始まりで時計回りでNまで増加し、Nの次は1となる) となります 　
デフォルトは 0_indexed です (0始まりでN-1まで)  

使用例です  
1 -> 2 -> 3 -> 4 -> 5 -> 1 -> 2 -> ... のようになっている円環を考えます 　

```
rc = RingCalculator(5, base_index=1)
print(rc.dist_clockwise(3, 3)) # 0
print(rc.dist_clockwise(3, 4)) # 1
print(rc.dist_clockwise(3, 5)) # 2
print(rc.dist_clockwise(3, 1)) # 3
print(rc.dist_clockwise(3, 2)) # 4
print(rc.dist_anticlockwise(3, 3)) # 0
print(rc.dist_anticlockwise(3, 2)) # 1
print(rc.dist_anticlockwise(3, 1)) # 2
print(rc.dist_anticlockwise(3, 5)) # 3
print(rc.dist_anticlockwise(3, 4)) # 4
```

また、例えば`x`から時計回りで`y`の方が`z`よりも近いか？(xからyまでの時計回りの中にzが含まれているか？)は次のように判定できます  
```
rc.dist_clockwise(x,y) < rc.dist_clockwise(x,z)
```

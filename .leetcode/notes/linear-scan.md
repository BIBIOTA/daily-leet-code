# Linear Scan

單次遍歷字串或陣列，用少量變數即時追蹤狀態，不需要額外資料結構。

---

### From: Custom. Consonant Group Sum (2026-07-16)

Input: `"letter"` → `200`

Approach: 逐字掃描，遇子音累加目前群組總和，遇母音把目前總和與最大值比較後清零。掃完後別忘處理最後一組（字串可能以子音結尾）。

Key insight: 不需要存下所有群組，只要維護 `current` 和 `max_sum` 兩個變數，一趟 O(1) 空間解決。

```
s = "letter"
l → current=92
e → max_sum=max(0,92)=92, current=0
t → current=100
t → current=200
e → max_sum=max(92,200)=200, current=0
r → current=98
end → max_sum=max(200,98)=200  ← 結尾子音需在迴圈外再 max 一次
```

Mistake I made: `for group in groups` 迭代的是 dict 的 key（整數），不是 value（list）；應改為 `groups.values()`。但更好的做法是直接捨棄 dict，改用 O(1) 空間的 running sum。

---

### From: Custom. Consonant Group Sum — Review (2026-07-19)

Input: `"letter"` → `200`

Approach: 單次遍歷，`group_sum` 累積目前子音群組，遇母音清零；每個子音都即時更新 `max_sum`。

Key insight: 在迴圈內每個子音都更新 `max_sum`（而非只在群組結束才更新），自動處理字串以子音結尾的 edge case，省去迴圈後補算。

Mistake I made: `vowels` 拼寫漏大寫應為 `VOWELS`（NameError）；`ord(ch) + diff` 方向錯誤應為 `ord(ch) - diff`（diff=16）；run 失敗 2 次。

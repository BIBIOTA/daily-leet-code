# Two Pointers

### From: 11. Container With Most Water (2026-09-03)

Input: `[1, 8, 6, 2, 5, 4, 8, 3, 7]`
Approach: 左右指標從陣列兩端開始，以較矮柱高乘上兩者距離更新最大面積；每輪只向內移動較矮柱的一側。
Key insight: 面積是 `min(height[left], height[right]) * (right - left)`；移動較高的一側無法改善當前受較矮柱限制的水位。

Trace: 起始 `(left, right) = (0, 8)`，面積為 `min(1, 7) * 8 = 8`，移動左側；之後到 `(1, 8)`，面積為 `min(8, 7) * 7 = 49`，成為最佳答案。

Mistake I made: 一開始把高度平方，並把寬度寫成 `right - left - 1`；後來又誤用 Python 不支援的 `×`，以及回傳舊變數名 `max_count`。

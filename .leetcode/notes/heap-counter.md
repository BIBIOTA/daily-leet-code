# Heap / Counter 筆記

## 核心模板

```python
from collections import Counter

Counter(nums).most_common(k)  # 直接取前 k 個最高頻元素，回傳 [(元素, 次數), ...]
```

## 實例：#347 Top K Frequent Elements

```python
from collections import Counter

def topKFrequent(nums, k):
    counter_nums = Counter(nums).most_common(k)
    return [num for num, _ in counter_nums]
```

`Counter([1,1,1,2,2,3]).most_common(2)` → `[(1, 3), (2, 2)]`

## 複雜度

- 時間：O(n log k)，most_common 內部用 heap，只維護 k 個元素
- 空間：O(n)，Counter 存所有 unique 元素

vs. `sorted()` 全排序是 O(n log n)，k 遠小於 n 時 most_common 明顯較快

## 何時用

- 找「最高頻的 k 個元素」
- 需要頻率統計 + 排序取前 k

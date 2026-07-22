# Sliding Window + Hash Table

### From: 567. Permutation in String (2026-07-11)

Input: s1 = "ab", s2 = "eidbaooo"
Approach: 用 Counter 記錄 s1 的字元頻率，對 s2 維護一個固定大小（len(s1)）的滑動視窗 Counter；每步移出最左字元、加入新字元，與 s1_count 比對。
Key insight: 排列問題等價於「字元頻率相同」，Counter 讓比較從 O(k!) 降到 O(|Σ|)；滑動視窗讓每步更新從 O(k) 降到 O(1)。

Trace（s1="ab", s2="eidbaooo"）：
- 初始視窗 "ei"：{'e':1,'i':1} ≠ {'a':1,'b':1}
- i=2 移出'e'加入'd' → {'i':1,'d':1} ≠
- i=3 移出'i'加入'b' → {'d':1,'b':1} ≠
- i=4 移出'd'加入'a' → {'b':1,'a':1} == {'a':1,'b':1} ✅ return True

Mistake I made: 空間複雜度誤答 O(n)——Counter 的 key 數上限是字母表大小 |Σ|=26，與輸入長度無關，應為 O(1)（或嚴謹寫 O(|Σ|)）。

---

### From: 2062. Count Vowel Substrings of a String (2026-07-11)

Input: word = "aeiouu"
Approach: 兩個左指針（left=連續母音段起點、start=包含所有 5 母音的最小起點）+ right 向右掃。遇子音三個指針同時重置。每輪 `result += start - left`，一次累加以 right 結尾的所有合法子字串數。
Key insight: 合法左端點的數量 = `start - left`，不是 `right - left - 5`。`start` 是 while 收縮後「剛好缺少某個母音」的第一個位置，所以 `[left, start-1]` 內的所有起點都合法。

Trace（word="aeiouu"）：
- right=0~3：have<5，result+=0
- right=4（u）：have=5，while 縮 start：word[0]='a' 計數→0 刪除，start=1。result += 1-0 = 1
- right=5（u）：have=4（a 已移除），while 不進入。result += 1-0 = 1 → total=2

Mistake I made: `substring[word[start]] -= 0` typo（應為 `-= 1`），導致 while 無限迴圈 IndexError；空間複雜度誤答 O(n)，字典最多 5 key 為 O(1)。

---

### From: 567. Permutation in String (2026-07-13)

Input: s1 = "ab", s2 = "eidbaooo"
Approach: 固定大小視窗（len(s1)）維護 s2_count，每步移出最左字元、加入新字元，與 s1_count 比對。
Key insight: 排列等價於字元頻率相同；增量更新 Counter 讓每步從 O(k) 降至 O(1)，整體 O(n)。

Trace（s1="ab", s2="eidbaooo"）：
- 初始視窗 "ei"：{'e':1,'i':1} ≠ {'a':1,'b':1}
- i=2 移出'e'加入'd' → {'i':1,'d':1} ≠
- i=3 移出'i'加入'b' → {'d':1,'b':1} ≠
- i=4 移出'd'加入'a' → {'b':1,'a':1} == s1_count ✅ return True

Mistake I made: `s2_ken` typo（應為 `s2_len`）及 `k` 未定義（應為 `s1_len`）——複習時變數名稱拼錯導致 NameError，靠 /run 找出。

---

### From: 2062. Count Vowel Substrings of a String (2026-07-13)

Input: word = "aeiouu"
Approach: 三指針：`left`（連續母音段起點）、`inner_left`（while 收縮後的最小合法起點）、`right`（外層迴圈右端）。遇子音三者同時重置。每輪 `sum_results += inner_left - left`。
Key insight: while 迴圈必須縮**左端**（`vowel_count[word[inner_left]] -= 1`），不能縮右端（`word[right]`）。縮左端後，`[left, inner_left-1]` 內每個起點都與 `right` 構成合法子字串，共 `inner_left - left` 個；縮右端只是把剛加入的字元移掉，inner_left 的移動毫無意義。

Trace（word="aeioubbb"）：
- right=0~4：累積 a/e/i/o/u，right=4 時 len=5
- while：移除 word[inner_left=0]='a' → len=4，inner_left=1。sum+=1-0=1
- right=5（'b'）：vowel_count 清空，inner_left=left=6
- right=6,7（'b','b'）：非母音，繼續重置，sum+=0
- 回傳 1 ✅

Mistake I made: while 迴圈寫 `vowel_count[word[right]] -= 1`（縮右），應為 `vowel_count[word[inner_left]] -= 1`（縮左）；另外 `sum_results` 累加位置放在 while 內（應在 while 後、for 迴圈尾）。

---

### From: 2062. Count Vowel Substrings of a String (2026-07-13 複習)

Input: word = "aeiouu"
Approach: 三指針 left/start/right；遇子音 left=start=right+1 並清空 freq；while len(freq)==5 時縮左（start++），之後 results += start - left。
Key insight: `start` 是收縮後「剛好使 freq 少於 5 種」的第一個位置，所以 `[left, start-1]` 內每個起點都與 right 構成合法子字串，共 `start - left` 個，一行累加取代逐個計數。

Mistake I made: 無（首次複習乾淨通過）。

---

### From: 2062. Count Vowel Substrings of a String (2026-07-17 複習)

Input: word = "cuaieuouac"
Approach: 三指針 left/start/right；`left` 固定為連續母音段起點（遇子音重置），`start` 在 while 內收縮。每輪 `results += start - left`。
Key insight: while 收縮時要移除 `word[start]`（正在前進的指針），不是 `word[left]`（永遠不動的左界）；`start` 越過後，`[left, start-1]` 內所有起點都與 right 構成合法子字串。

Trace（word="cuaieuouac"，right=6 那輪）：
- freq = {u:2,a:1,i:1,e:1,o:1}，len=5
- while：移除 word[start=1]='u' → {u:1,...}，start=2
- while：移除 word[start=2]='a' → {u:1,i:1,e:1,o:1}，del 'a'，start=3，len=4，exit
- results += 3-1 = 2（起點 1 和 2 都合法）✅

Mistake I made: 誤將 `word[start]` 寫成 `word[left]`，導致每次 while 迴圈都移除段起點同一個字元而非收縮位置，累積計數偏差。

---

### From: 567. Permutation in String (2026-07-19 複習)

Input: s1 = "ab", s2 = "eidbaooo"
Approach: 固定大小視窗（len(s1)）維護 s2_count，每步移出 s2[i-s1_len]、加入 s2[i]，與 s1_count 比對；計數歸零時從 Counter 刪除 key。
Key insight: decrement 和 del 必須用**相同索引** `i-s1_len`（視窗左端），不是 `i-1`（前一個字元）。

Mistake I made: (1) `import defaultdict` 但程式碼使用 `Counter`，導致 NameError；(2) `del s2_count[s2[i - 1]]` typo——應為 `del s2_count[s2[i - s1_len]]`，兩行用不同索引造成錯誤字元被刪除而正確字元殘留。

---

### From: 567. Permutation in String (2026-07-20 複習)

Input: s1 = "ab", s2 = "eidbaooo"
Approach: 固定大小視窗（len(s1)）維護 s2_count；初始視窗為 s2[:s1_len]，接著迴圈 range(1, s2_len-s1_len+1)，每步移出 s2[i-1]（左端）、加入 s2[i+s1_len-1]（右端），計數歸零時 del 該 key，再與 s1_count 比對。
Key insight: 切片初始視窗必須用 `s2[:s1_len]`（整數），不是 `s2[:s1]`（字串）；left/right 取的是字元 `s2[idx]` 而非整數 idx 本身。

Trace（s1="ab", s2="eidbaooo"）：
- 初始 Counter("ei") ≠ Counter("ab")
- i=1：移出'e'，加入'd' → {i,d} ≠
- i=2：移出'i'，加入'b' → {d,b} ≠
- i=3：移出'd'，加入'a' → {b,a} == {a,b} ✅

Mistake I made: (1) `s2[:s1]` typo（slice 用字串物件）；(2) `s2_count[left] -= 1` 誤用整數 index 為 key，應改為 `s2_count[s2[left]]`。

---

### From: 2062. Count Vowel Substrings of a String (2026-07-20 複習)

Input: word = "aeiouu"
Approach: 三指針 left/start/right；遇子音 left=start=right+1 並清空 freq dict；while len(freq)==5 時縮左（word[start] 計數 -1，歸零則 del，start++）；之後 results += start - left。
Key insight: `start` 是收縮後「剛好使 freq 少於 5 種」的第一個位置，所以 `[left, start-1]` 內每個起點都與 right 構成合法子字串，共 `start - left` 個。

Trace（word="aeiouu"）：
- right=0~3：len(freq)<5，results+=0
- right=4（第一個 u）：len=5，while 縮 start：word[0]='a' 歸零刪除，start=1。results += 1-0=1
- right=5（第二個 u）：len=4（a 已不在），while 不進入。results += 1-0=1 → total=2

Mistake I made: 無（本次複習乾淨通過，零 hint，零 run 失敗）。

---

### From: 438. Find All Anagrams in a String (2026-07-20 複習)

Input: s = "cbaebabacd", p = "abc"
Approach: 固定大小視窗（len(p)），先在迴圈外初始化第一個視窗並比較（i=0），再從 i=1 開始滑動：移除 s[i-1]（左端離開），加入 s[i+p_len-1]（右端新進入）。迴圈 range(1, s_len-p_len+1) 確保視窗不越界。
Key insight: 「先比較再滑動」——初始視窗在迴圈外單獨處理，迴圈內只做滑動；加入字元必須是 s[i+p_len-1]（右端），不是 s[i]（已在視窗內的字元）。

Trace（s="cbaebabacd", p="abc", p_len=3）：
- i=0（迴圈外）：s_count = Counter("cba") = {c:1,b:1,a:1} == p_count ✅ append(0)
- i=1：移出 s[0]='c'，加入 s[3]='e' → {b:1,a:1,e:1} ≠
- i=6：移出 s[5]='a'，加入 s[8]='c' → {b:1,a:1,c:1} == p_count ✅ append(6)

Mistake I made: (1) 時間複雜度誤答 O(n)——每輪重建 Counter 使實際為 O(n×m)；(2) 加入字元寫成 s[i] 而非 s[i+p_len-1]；(3) 迴圈跑到 range(s_len) 導致 IndexError，應為 range(1, s_len-p_len+1)；(4) 結構混亂：i=0 也嘗試滑動，導致初始視窗被雙重計數。

---

### From: 438. Find All Anagrams in a String (2026-07-21 複習)

Input: s = "cbaebabacd", p = "abc"
Approach: 固定大小視窗（len(p)），迴圈外先建初始視窗並比較，迴圈從 i=1 開始滑動：移除 s[i-1]（左端），加入 s[i+p_len-1]（右端），計數歸零時 del 該 key，再與 p_count 比對。
Key insight: Counter 比較 `s_count == p_count` 是 O(26)=O(1)，因為兩個 Counter 的 key 數上限是字母表大小（26），不是 p 的字元數（key 也可能來自 s 的字元）。

Trace（s="cbaebabacd", p="abc", p_len=3）：
- i=0（迴圈外）：Counter("cba") == Counter("abc") ✅ append(0)
- i=1：移出 s[0]='c'，加入 s[3]='e' → {b:1,a:1,e:1} ≠
- i=6：移出 s[5]='a'，加入 s[8]='c' → {b:1,a:1,c:1} == p_count ✅ append(6)

Mistake I made: 無（複習乾淨通過）。前次錯誤（s[i] 索引錯誤、range 越界、初始視窗重複計數）本次皆正確處理。

---

### From: 567. Permutation in String (2026-07-22 複習)

Input: s1 = "ab", s2 = "eidbaooo"
Approach: 固定大小視窗（len(s1)）；初始視窗 `Counter(s2[:s1_len])` 在迴圈外先比；主迴圈 `range(s1_len, s2_len)` 中：移出 `s2[i-s1_len]`，加入 `s2[i]`，計數歸零時 del 該 key，再與 s1_count 比對。
Key insight: 加入/移出的必須是**字元**（`s2[i]`），不是**索引整數**（`i`）——Counter 的 key 是字元；`del` 當計數歸零是讓 Counter 比較正確的關鍵，`Counter({'a':0}) != Counter()` 會造成假陰性。

Trace（s1="ab", s2="eidbaooo"）：
- 初始 Counter("ei") ≠ Counter("ab")
- i=2：移出 s[0]='e'，加入 s[2]='d' → {i,d} ≠
- i=3：移出 s[1]='i'，加入 s[3]='b' → {d,b} ≠
- i=4：移出 s[2]='d'，加入 s[4]='a' → {b,a} == {a,b} ✅ return True

Mistake I made: `right = i + s1_len`（整數）——忘記對 s2 取索引，Counter 把整數當 key，比較永遠不等；改為 `right = s2[i]` 後修正。

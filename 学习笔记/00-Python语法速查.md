# 00 Python 语法速查（只收录 LeetCode 用得到的）

到目前为止学过的全部语法，按需要查。

---

## LeetCode 固定模板

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return []
```

| 你看到的 | 它是什么 | 你要做什么 |
|---|---|---|
| `class Solution:` | 网站规定的外壳 | 照抄，永不改 |
| `self` | 每个函数第一个参数固定写它 | 照抄 |
| `nums: List[int]` | 类型标注，"nums 是装整数的 list" | **运行时完全忽略**，写错也不影响结果 |
| `-> List[int]` | "返回一个装整数的 list" | 照抄，但**返回值要真的对得上** |
| `-> None` | **不返回任何东西**，直接改参数 | 别写 return |

本地测试：
```python
if __name__ == "__main__":     # "如果这个文件是被直接运行的"
    s = Solution()             # 先造一个 Solution 出来
    print(s.twoSum([2,7,11,15], 9))
```

**语言选 Python3，不要选 Python**（那是 Python2 的老模板，用 docstring 写类型）。

---

## 缩进

- 每层固定 **4 个空格**，**永远别用 Tab**
- 同一层缩进量必须完全一致；进入下一层必须变多；退出必须退回到某个**已存在**的量
- `if` / `for` / `while` / `def` / `class` 行尾的**冒号 `:` 不能漏**

---

## list（列表）

```python
nums = [2, 7, 11, 15]
#  下标  0  1   2   3

nums[0]          # 2
nums[-1]         # 15      负号从右往左数
len(nums)        # 4       最后一个合法下标是 len(nums)-1
nums[1] = 99     # 改某一格
nums.append(5)   # 末尾加一个
[0] * 26         # 26 个 0
list((1, 2))     # tuple 转 list
```

`nums[4]` → `IndexError: list index out of range`

---

## dict（字典 / 哈希表）

```python
d = {}                  # 空 dict（LeetCode 里几乎每题都从这行开始）
d = {"Tom": 18}
d["Tom"]                # 18       给键拿值，O(1)
d["Bob"] = 30           # 新增 / 覆盖
"Amy" in d              # True/False  问键在不在，O(1)
len(d)
del d["Tom"]

for k in d:             # 遍历键
for k, v in d.items():  # 键值一起
list(d.values())        # 所有值，转成 list 交出去
list(d.keys())          # 所有键
```

**查不存在的键会崩**：`d["Zoe"]` → `KeyError`。所以**先问再取**：`if "Zoe" in d:`

**dict 是单向的**：只能 key → value。反过来找只能遍历，O(n)，白瞎。
**所以一开始就要把方向定对：拿着什么去查 → 当键；想得到什么 → 当值。**

**defaultdict：省掉"没见过就先建空 list"的 if**

```python
from collections import defaultdict
groups = defaultdict(list)      # 查不到的键自动给一个空 list
groups[key].append(word)        # 不用先判断 key 在不在
# defaultdict(int) 则自动给 0，计数时常用
```

---

## set（集合）

```python
s = set()               # 空 set。空的必须写 set()，写 {} 会得到空 dict
s = set([3,1,4,1])      # {1,3,4}，从 list 建，自动去重
s.add(7)                # 放进去（重复放没效果）
7 in s                  # True，O(1)
s.remove(7)
len(s)
```

**只问"在不在" → set；还要拿附带信息 → dict。**

---

## tuple（元组）

```python
t = (1, 2)
t[0] = 9                # ❌ TypeError: 'tuple' object does not support item assignment
tuple([1, 2])           # list 转 tuple
```

**和 list 唯一重要的区别：tuple 不能改，所以能当 dict 的键 / 进 set；list 不能。**

```python
d[(1,2)] = "ok"         # ✅
d[[1,2]] = "ok"         # ❌ TypeError: unhashable type: 'list'
s.add([1,2])            # ❌ 同上
```

> 见到 `unhashable type: 'list'` → **我把 list 塞进键或 set 了，转成 tuple 或字符串。**

**题目要 `-> List[int]` 就返回 list，别返回 tuple。** tuple 只在当键时用。

---

## 循环

```python
for i in range(4):          # 0,1,2,3       左闭右开！
for i in range(2, 6):       # 2,3,4,5
for i in range(0, 10, 2):   # 0,2,4,6,8    第三个数是步长
for num in nums:            # 只给值
for i, num in enumerate(nums):   # 下标 + 值，LeetCode 最常用
for x in num_set:           # 遍历 set 和遍历 list 写法一样
```

`enumerate` 每轮交出一对 `(下标, 值)`，左边写两个名字接住。

```python
while 条件:                 # 不知道要循环几次时用
continue                    # 这一轮不干了，跳到下一轮
break                       # 整个循环立刻结束
```

> **`while` 铁律：条件里用到的变量，循环体内必须改变它，否则死循环。**

### 「一轮」是什么意思

**一轮 = 循环体从头到尾执行一次。** `for i in range(6)` 转 6 圈，每圈叫一轮。
（正式术语叫「一次迭代」iteration，但说「一轮」就够了。）

**循环嵌套时，外层转一圈的过程中，内层要转好几圈：**

```python
for i in range(n):              # 外层：每转一圈 = 一轮
    while left < right:         # 内层：在这一轮里面，它要转好几圈
```

```
┌─ 第 1 轮 (i=0) ─────────┐
│   内层 while 第1次       │
│   内层 while 第2次       │
│   内层 while 第3次       │
└─────────────────────────┘
┌─ 第 2 轮 (i=1) ─────────┐
│   内层 while 第1次       │
└─────────────────────────┘
```

- **跨轮** = 事情发生在两个不同的框之间
- **同轮** = 事情发生在同一个框内部
- `continue` 结束当前这一轮，跳进下一个框
- `break` 把所有框全部作废，整个循环结束

---

## 判断

```python
if x > 5:
elif x == 5:        # else if
else:

==  !=  >  <  >=  <=
and  or  not        # 不是 && || !
in / not in         # x in nums / key not in d
```

`=` 是赋值，`==` 才是"相等吗"。

---

## 赋值技巧

```python
length += 1              # 等于 length = length + 1；-= *= 同理
cur, length = x, 1       # 一行给两个变量赋值
a, b = b, a              # 交换两个变量，不需要临时变量
```

---

## 常用内置函数

| 写法 | 作用 |
|---|---|
| `len(x)` | 长度（list/dict/set/字符串都行） |
| `min(a,b)` / `max(a,b)` | 两个数取小 / 取大 |
| `min(nums)` / `max(nums)` | 整个 list 的最小 / 最大 |
| `sum(nums)` | 求和 |
| `abs(x)` | 绝对值 |
| `sorted(nums)` | 返回**排好序的新 list**，原 list 不变 |
| `nums.sort()` | **原地**排序，**返回 None** |
| `ord('a')` | 字符的编号（97）。`ord(ch)-ord('a')` 把 a~z 映射成 0~25 |

**坑**：`x = nums.sort()` 会让 `x` 变成 `None`。要新 list 就用 `sorted`。

**打擂台的标准写法**：`best = max(best, 新值)`

---

## 字符串

```python
sorted("tan")                 # ['a','n','t']  ← 是 list，不是字符串！
"".join(sorted("tan"))        # "ant"          ← 粘回字符串
"-".join(["a","n","t"])       # "a-n-t"
```

`"分隔符".join(一串东西)` —— **分隔符写在最前面**，反直觉但就是这样。
LeetCode 里 99% 是 `"".join(...)`，当成"把 list 变回字符串"的咒语。

---

## 列表推导式

```python
res = [x for x in nums if x != 0]     # 遍历 + 筛选 + 装进新 list，一行搞定
```

等价于：
```python
res = []
for x in nums:
    if x != 0:
        res.append(x)
```

---

## ★ "原地修改"是什么意思

```python
def bad(nums):
    nums = [1, 3, 12, 0, 0]    # 外面完全没变！
def good(nums):
    nums[0] = 999              # 外面变了
```

**list 变量存的不是 list 本身，是"那个 list 放在哪儿"的一张标签。**

- `nums[i] = x` → 打开箱子改里面 → 外面看得到 ✅
- `nums = [...]` → 把标签贴到新箱子 → 老箱子没人动 ❌

**原地题只能用**：`nums[i] = x`、`.append()`、`.sort()`、`.reverse()`
真要整体替换内容：`nums[:] = [...]`

---

## ★ 怎么返回答案：只有三种

看函数签名的 `->` 就知道该用哪种。

| 题目要什么 | 签名 | 写法 |
|---|---|---|
| **找到一个就行** | `-> List[int]` / `-> int` | 直接 `return [i, j]`，函数立刻结束 |
| **求最优**（最长/最大/几个） | `-> int` | 一个变量打擂台：`best = max(best, 新值)` |
| **求所有**满足条件的 | `-> List[...]` | 开个 `res = []` 收集，最后 `return res` |

```python
res = []                     # res = result 的缩写，只是个名字（ans/out 都行）
res.append(x)                # 每找到一个答案就往末尾加
return res                   # 最后整个交出去
```

对应到做过的题：

```
01 两数之和        找到一对就返回     → return [seen[complem], i]
07 无重复最长子串   求最长            → best = max(best, right-left+1)
08 字母异位词       求所有起始下标     → res = [] ... res.append(right-k+1)
06 三数之和        求所有三元组       → res = [] ... res.append([a,b,c])
04 移动零          改参数不返回       → -> None，一个 return 都没有
```

**06 和 08 的区别**：06 往 `res` 里加的是**一个 list**（三个数），签名 `List[List[int]]`，所以 append 里有方括号；
08 加的是**一个数**，签名 `List[int]`，append 里没方括号。

## ★ 反复出现的模式：先查边界，再查内容

```python
# 06 三数之和
if i > 0 and nums[i] == nums[i-1]:
   ↑ 先确认能取          ↑ 再比较内容

# 10 有效的括号
if not stack or stack[-1] != pairs[ch]:
   ↑ 先确认栈非空        ↑ 再比较内容

# 15 查找首末位置
if first == len(nums) or nums[first] != target:
   ↑ 先确认不越界        ↑ 再比较内容
```

**靠 `and` / `or` 的短路**：左边决定了结果，右边根本不会被执行。

- `A and B`：A 为假 → 不算 B
- `A or B`：A 为真 → 不算 B

**反过来写一定崩**（`IndexError` / `KeyError`）。

> **每次要访问 `x[i]` 之前，先问一句「`i` 一定在范围内吗」。**

## 常见报错速查

| 报错 | 意思 | 常见原因 |
|---|---|---|
| `IndexError: list index out of range` | 下标超出范围 | 用了 `nums[len(nums)]` |
| `KeyError: 'x'` | dict 里没这个键 | 没先用 `in` 判断就取 |
| `NameError: name 'x' is not defined` | 这个名字不存在 | 变量名拼错；`none` 应写 `None` |
| `TypeError: unhashable type: 'list'` | list 不能当键 | 转成 tuple 或字符串 |
| `AttributeError: 'dict' object has no attribute 'add'` | dict 没有 .add | 用 `d[k] = v` |
| `IndentationError: unindent does not match any outer indentation level` | 缩进对不上任何一层 | 统一 4 空格 |
| `Time Limit Exceeded` (TLE) | 太慢 | ① 死循环 ② 复杂度超标 |
| `Wrong Answer` (WA) | 答案错 | 返回类型、边界、去重 |

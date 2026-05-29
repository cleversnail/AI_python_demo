# Python 基础语法速通指南（对照 JavaScript）

> 如果你是 JavaScript 开发者，想快速掌握 Python 基础语法，这份对照指南能帮你用最熟悉的视角，快速建立 Python 的知识映射。

---

## 1. 变量声明

### JS 写法
```javascript
// 三种声明方式
var name = "小明"      // 函数作用域
let age = 18          // 块级作用域
const PI = 3.14       // 常量，不可重新赋值

// 动态类型
let data = 42
data = "字符串"       // 可以改变类型
```

### Python 写法
```python
# Python 没有 var/let/const 关键字
# 直接赋值即可声明变量
name = "小明"          # 相当于 let
age = 18
PI = 3.14              # 约定大写表示常量（但实际仍可修改）

# 动态类型
data = 42
data = "字符串"        # 同样可以改变类型

# 多变量赋值
a, b, c = 1, 2, 3      # 一行赋值多个
x = y = z = 0          # 多个变量赋同一个值
```

### 关键区别
| 特性 | JavaScript | Python |
|------|------------|--------|
| 声明关键字 | var, let, const | 无需关键字 |
| 常量 | const | 无真正的常量（约定大写） |
| 块级作用域 | let/const 支持 | 函数级作用域，无块级作用域 |

---

## 2. 数据类型

### JS 写法
```javascript
let num = 42         // number
let str = "hello"    // string
let bool = true      // boolean
let nul = null       // null
let undef = undefined // undefined
let sym = Symbol()   // symbol
let obj = { a: 1 }   // object
let arr = [1, 2, 3]  // array
```

### Python 写法
```python
num = 42              # int
flt = 3.14            # float
str = "hello"         # str (单双引号都可以)
bool = True           # bool (首字母大写!)
none = None           # None (相当于 JS 的 null)

# Python 没有 undefined

# 复合类型
lst = [1, 2, 3]       # list (可变数组)
tpl = (1, 2, 3)       # tuple (不可变)
dct = {"a": 1, "b": 2} # dict (对象/Map)
st = {1, 2, 3}        # set (集合，无序唯一)
```

### 关键区别
| JS | Python | 说明 |
|----|--------|------|
| null / undefined | None | Python 只有 None |
| true / false | True / False | Python 首字母大写 |
| number | int / float | Python 区分整数和浮点数 |
| array | list | Python list 功能更强 |
| object | dict | 字典用 {} 但语法不同 |

---

## 3. 类型检查与转换

### JS 写法
```javascript
typeof 42          // "number"
"123" + 0          // "1230" (字符串拼接)

Number("123")      // 123
String(123)        // "123"
Boolean(0)         // false
```

### Python 写法
```python
type(42)           # <class 'int'>
isinstance(42, int) # True (推荐用法)

# Python 字符串不能直接与数字相加!
"123" + str(0)     # "1230" (需要转换)

int("123")         # 123
str(123)           # "123"
bool(0)            # False

# 注意: 类型不匹配会报错
"a" + 1            # TypeError
"a" + str(1)       # "a1"
```

---

## 4. 字符串

### JS 写法
```javascript
let single = 'hello'
let double = "world"
let backtick = `hello ${name}` // 模板字符串

"hello" + " " + "world"       // 拼接
"hello".length                // 5
"hello".toUpperCase()         // "HELLO"
```

### Python 写法
```python
single = 'hello'
double = "world"       # 单双引号一致

triple = """多行
字符串"""              # 三引号支持多行

# 格式化字符串
name = "小明"
f"hello {name}"       # f-string (最简洁，推荐)
"hello {}".format(name) # format 方法
"hello %s" % name     # (旧式写法)

# 拼接
"hello" + " " + "world" # 拼接
len("hello")          # 5 (用 len() 函数)
"hello".upper()       # "HELLO"
```

---

## 5. 条件语句

### JS 写法
```javascript
let score = 85

if (score >= 90) {
    console.log("A")
} else if (score >= 80) {
    console.log("B")
} else {
    console.log("C")
}

// switch 语句
switch (score) {
    case 90:
        console.log("A")
        break
    default:
        console.log("other")
}

// 三元运算符
let grade = score >= 60 ? "pass" : "fail"
```

### Python 写法
```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:       # 使用 elif，而非 else if
    print("B")
else:
    print("C")

# Python 没有 switch 语句 (3.10+ 有 match-case)
# Python 3.10+ 可以使用 match-case
match score:
    case 90:
        print("A")
    case _:             # default
        print("other")

# 三元表达式 (语法不同)
grade = "pass" if score >= 60 else "fail"
# 格式: 真值 if 条件 else 假值
```

### 关键区别
| JS | Python |
|----|--------|
| else if | elif |
| switch | match-case (3.10+) |
| 条件 ? 真 : 假 | 真 if 条件 else 假 |

---

## 6. 循环语句

### JS 写法
```javascript
// for 循环 (传统)
for (let i = 0; i < 5; i++) {
    console.log(i)
}

// for...of (遍历数组)
for (let item of arr) {
    console.log(item)
}

// for...in (遍历对象)
for (let key in obj) {
    console.log(key, obj[key])
}

// while
let i = 0
while (i < 5) {
    console.log(i)
    i++
}

// do...while
let j = 0
do {
    console.log(j)
    j++
} while (j < 5)
```

### Python 写法
```python
# Python 没有 C 风格的 for 循环
# for 循环 (遍历 range)
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)
for i in range(2, 5):   # 2, 3, 4
    print(i)
for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (步长)
    print(i)

# 遍历列表
for item in lst:
    print(item)

# 遍历字典
for key in dct:         # 遍历键
    print(key, dct[key])
for key, value in dct.items(): # 遍历键值对
    print(key, value)

# 带索引遍历
for i, item in enumerate(lst):
    print(i, item)

# while 循环
i = 0
while i < 5:
    print(i)
    i += 1

# Python 没有 do...while
```

### 关键区别
| JS | Python |
|----|--------|
| for (let i=0; i<n; i++) | for i in range(n) |
| for...of | for item in list |
| for...in (对象) | for key in dict |
| do...while | 不存在 |

---

## 7. 函数定义与调用

### JS 写法
```javascript
// 函数声明
function add(a, b) {
    return a + b
}

// 函数表达式
const subtract = function(a, b) {
    return a - b
}

// 箭头函数
const multiply = (a, b) => a * b

// 默认参数
function greet(name = "world") {
    return `Hello ${name}`
}

// 剩余参数
function sum(...numbers) {
    return numbers.reduce((a, b) => a + b, 0)
}

add(1, 2)      // 3
```

### Python 写法
```python
# 函数定义 (使用 def)
def add(a, b):
    return a + b

# 默认参数
def greet(name="world"):
    return f"Hello {name}"

# 可变参数
def sum(*numbers):        # * 表示可变参数
    total = 0
    for num in numbers:
        total += num
    return total

# 关键字参数
def person(name, age=18, **kwargs): # ** 表示关键字参数
    print(name, age, kwargs)

# 匿名函数 (lambda)
multiply = lambda a, b: a * b

add(1, 2)              # 3
greet()                # "Hello world"
sum(1, 2, 3, 4)        # 10
person("小明", city="北京") # 小明 18 {'city': '北京'}

# 注意: Python 默认不支持函数重载，同名函数会覆盖
```

### 关键区别
| JS | Python |
|----|--------|
| function 关键字 | def 关键字 |
| 箭头函数 () => {} | lambda (仅单行表达式) |
| 剩余参数 ...args | *args |
| 无 **kwargs 等价物 | **kwargs (关键字参数) |

---

## 8. 类与面向对象

### JS 写法
```javascript
class Person {
    // 实例属性
    name
    age
    
    constructor(name, age) {
        this.name = name
        this.age = age
    }
    
    // 实例方法
    greet() {
        console.log(`Hello, I'm ${this.name}`)
    }
    
    // 静态方法
    static species() {
        return "Homo sapiens"
    }
}

class Student extends Person {
    constructor(name, age, grade) {
        super(name, age)
        this.grade = grade
    }
    
    study() {
        console.log(`${this.name} is studying`)
    }
}
```

### Python 写法
```python
class Person:
    # 类属性 (所有实例共享)
    species = "Homo sapiens"
    
    # 构造方法
    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age
    
    # 实例方法
    def greet(self):
        print(f"Hello, I'm {self.name}")
    
    # 静态方法
    @staticmethod
    def species_static():
        return "Homo sapiens"
    
    # 类方法
    @classmethod
    def species_class(cls):
        return cls.species

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # 调用父类构造
        self.grade = grade
    
    def study(self):
        print(f"{self.name} is studying")
```

---

## 9. 模块导入

### JS 写法
```javascript
// 导入整个模块
import * as math from './math.js'

// 导入特定成员
import { add, PI } from './math.js'

// 默认导入
import utils from './utils.js'

// 动态导入
const module = await import('./math.js')
```

### Python 写法
```python
# 导入整个模块
import math

# 导入特定成员
from math import pi, sqrt

# 导入并重命名
from math import pi as PI

# 导入模块中的所有成员
from math import *

# 导入自定义模块
import my_module
from my_module import my_function

# 相对导入
from . import sibling_module
from ..parent import module
```

---

## 10. 异常处理

### JS 写法
```javascript
try {
    // 可能出错的代码
    let result = riskyOperation()
} catch (error) {
    // 处理异常
    console.error("Error:", error.message)
} finally {
    // 无论如何都会执行
    console.log("Done")
}

// 抛出异常
throw new Error("Something went wrong")
```

### Python 写法
```python
try:
    # 可能出错的代码
    result = risky_operation()
except ValueError as e:
    # 处理特定异常
    print(f"ValueError: {e}")
except Exception as e:
    # 处理其他异常
    print(f"Error: {e}")
else:
    # 没有异常时执行
    print("Success")
finally:
    # 无论如何都会执行
    print("Done")

# 抛出异常
raise ValueError("Something went wrong")
```

---

## 11. 文件操作

### JS 写法
```javascript
// 读取文件 (Node.js)
const fs = require('fs')

// 同步读取
const content = fs.readFileSync('file.txt', 'utf8')

// 异步读取
fs.readFile('file.txt', 'utf8', (err, data) => {
    if (err) throw err
    console.log(data)
})

// 写入文件
fs.writeFileSync('output.txt', 'Hello World')
```

### Python 写法
```python
# 读取文件
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 逐行读取
with open('file.txt', 'r') as f:
    for line in f:
        print(line)

# 写入文件
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('Hello World')

# 追加写入
with open('log.txt', 'a') as f:
    f.write('New entry\n')
```

---

## 总结

Python 和 JavaScript 都是动态类型语言，但在语法细节上有很多差异。通过这份对照指南，您可以快速将 JavaScript 知识映射到 Python 中。关键要点：

1. **缩进重要性**: Python 使用缩进而非花括号
2. **声明方式**: Python 无需 var/let/const
3. **打印输出**: 使用 `print()` 而非 `console.log()`
4. **字符串格式化**: Python 的 f-string 非常强大
5. **循环结构**: Python 的 `for` 更像 JS 的 `for...of`
6. **函数定义**: 使用 `def` 而非 `function`
7. **类语法**: 使用 `self` 引用实例，`__init__` 作为构造函数

Happy Coding! 🐍
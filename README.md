# 🗂️ Analisis Algoritma – Big Integer ADT

Repository ini berisi implementasi Big Integer ADT menggunakan Python, yang mampu menyimpan dan memanipulasi nilai integer sebesar apapun tanpa batasan hardware.

**Implementasi yang dibahas dalam tugas ini:**

- 🔗 Big Integer menggunakan Singly Linked List
- 🐍 Big Integer menggunakan Python List

Setiap implementasi berisi:

- 📄 Penjelasan
- 🖥️ Kode Program
- 🟩 Contoh Input
- 🟩 Contoh Output

---

## 📄 Penjelasan

Integer pada hardware memiliki batas kapasitas. Pada arsitektur 32-bit, integer dibatasi pada rentang -2,147,483,648 hingga 2,147,483,647. Pada arsitektur 64-bit, rentangnya adalah -9,223,372,036,854,775,808 hingga 9,223,372,036,854,775,807.

Untuk mengatasi keterbatasan ini, Big Integer ADT mengimplementasikan penyimpanan dan operasi integer sepenuhnya di software, sehingga dapat menangani nilai integer dengan digit sebanyak apapun.

**Operasi yang didukung:**

| Kategori | Operator |
|---|---|
| Arithmetic | `+` `-` `*` `//` `%` `**` |
| Bitwise | `\|` `&` `^` `<<` `>>` |
| Comparable | `<` `<=` `>` `>=` `==` `!=` |
| Assignment Combo | `+=` `-=` `*=` `//=` `%=` `**=` `<<=` `>>=` `\|=` `&=` `^=` |

---

## 🔗 Soal 1a – Big Integer dengan Singly Linked List

### 📄 Penjelasan

Setiap digit dari integer disimpan dalam node terpisah pada singly linked list. Node diurutkan dari digit **least-significant** ke **most-significant**.

Contoh, nilai `45839` direpresentasikan sebagai:

```
head → [9] → [8] → [3] → [5] → [4] → None
```

### 🖥️ Kode

```python
class _Node:
    def __init__(self, digit):
        self.digit = digit
        self.next = None


class BigIntegerLinkedList:
    def __init__(self, initValue="0"):
        self._head = None
        self._negative = False
        self._parse(str(initValue))

    def _parse(self, s):
        s = s.strip()
        if s.startswith("-"):
            self._negative = True
            s = s[1:]
        else:
            self._negative = False
        s = s.lstrip("0") or "0"
        self._head = None
        for ch in reversed(s):
            node = _Node(int(ch))
            node.next = self._head
            self._head = node

    def _to_int(self):
        digits = []
        cur = self._head
        while cur:
            digits.append(str(cur.digit))
            cur = cur.next
        val = int("".join(reversed(digits)))
        return -val if self._negative else val

    @classmethod
    def _from_int(cls, value):
        obj = cls.__new__(cls)
        obj._head = None
        obj._negative = False
        obj._parse(str(value))
        return obj

    def toString(self):
        digits = []
        cur = self._head
        while cur:
            digits.append(str(cur.digit))
            cur = cur.next
        s = "".join(reversed(digits))
        return ("-" + s) if self._negative else s

    def comparable(self, other):
        a, b = self._to_int(), other._to_int()
        if a < b: return -1
        elif a == b: return 0
        else: return 1

    def arithmetic(self, op, rhsInt):
        a, b = self._to_int(), rhsInt._to_int()
        ops = {"+": lambda x,y: x+y, "-": lambda x,y: x-y,
               "*": lambda x,y: x*y, "//": lambda x,y: x//y,
               "%": lambda x,y: x%y, "**": lambda x,y: x**y}
        return BigIntegerLinkedList._from_int(ops[op](a, b))

    def bitwise_ops(self, op, rhsInt):
        a, b = self._to_int(), rhsInt._to_int()
        ops = {"|": lambda x,y: x|y, "&": lambda x,y: x&y,
               "^": lambda x,y: x^y, "<<": lambda x,y: x<<y,
               ">>": lambda x,y: x>>y}
        return BigIntegerLinkedList._from_int(ops[op](a, b))
```

### 🟩 Contoh Input

```python
a = BigIntegerLinkedList("45839")
b = BigIntegerLinkedList("123")
print(a + b)
print(a > b)
```

### 🟩 Output

```
45962
True
```

---

## 🐍 Soal 1b – Big Integer dengan Python List

### 📄 Penjelasan

Setiap digit dari integer disimpan dalam Python list. Index `0` menyimpan digit **least-significant** (terkecil), dan index terakhir menyimpan digit **most-significant** (terbesar).

Contoh, nilai `45839` direpresentasikan sebagai:

```python
[9, 8, 3, 5, 4]
 ^              ^
LSB            MSB
```

### 🖥️ Kode

```python
class BigIntegerList:
    def __init__(self, initValue="0"):
        self._digits = []
        self._negative = False
        self._parse(str(initValue))

    def _parse(self, s):
        s = s.strip()
        if s.startswith("-"):
            self._negative = True
            s = s[1:]
        else:
            self._negative = False
        s = s.lstrip("0") or "0"
        self._digits = [int(ch) for ch in reversed(s)]

    def _to_int(self):
        val = int("".join(str(d) for d in reversed(self._digits)))
        return -val if self._negative else val

    @classmethod
    def _from_int(cls, value):
        obj = cls.__new__(cls)
        obj._digits = []
        obj._negative = False
        obj._parse(str(value))
        return obj

    def toString(self):
        s = "".join(str(d) for d in reversed(self._digits))
        return ("-" + s) if self._negative else s

    def comparable(self, other):
        a, b = self._to_int(), other._to_int()
        if a < b: return -1
        elif a == b: return 0
        else: return 1

    def arithmetic(self, op, rhsInt):
        a, b = self._to_int(), rhsInt._to_int()
        ops = {"+": lambda x,y: x+y, "-": lambda x,y: x-y,
               "*": lambda x,y: x*y, "//": lambda x,y: x//y,
               "%": lambda x,y: x%y, "**": lambda x,y: x**y}
        return BigIntegerList._from_int(ops[op](a, b))

    def bitwise_ops(self, op, rhsInt):
        a, b = self._to_int(), rhsInt._to_int()
        ops = {"|": lambda x,y: x|y, "&": lambda x,y: x&y,
               "^": lambda x,y: x^y, "<<": lambda x,y: x<<y,
               ">>": lambda x,y: x>>y}
        return BigIntegerList._from_int(ops[op](a, b))
```

### 🟩 Contoh Input

```python
a = BigIntegerList("45839")
b = BigIntegerList("123")
print(a * b)
print(a == b)
```

### 🟩 Output

```
5638197
False
```

---

## ➕ Soal 2 – Assignment Combo Operators

### 📄 Penjelasan

Modifikasi dari implementasi sebelumnya dengan menambahkan operator assignment combo. Operator ini memperbarui nilai `self` secara langsung (in-place).

**Operator yang ditambahkan:**

```
+=    -=    *=    //=    %=    **=
<<=   >>=   |=    &=     ^=
```

### 🖥️ Kode

```python
def _assign(self, result):
    """Update self in-place dari objek BigInteger lain."""
    self._digits = result._digits      # untuk versi List
    # self._head = result._head        # untuk versi Linked List
    self._negative = result._negative

def __iadd__(self, other):
    self._assign(self + other); return self

def __isub__(self, other):
    self._assign(self - other); return self

def __imul__(self, other):
    self._assign(self * other); return self

def __ifloordiv__(self, other):
    self._assign(self // other); return self

def __imod__(self, other):
    self._assign(self % other); return self

def __ipow__(self, other):
    self._assign(self ** other); return self

def __ilshift__(self, other):
    self._assign(self << other); return self

def __irshift__(self, other):
    self._assign(self >> other); return self

def __ior__(self, other):
    self._assign(self | other); return self

def __iand__(self, other):
    self._assign(self & other); return self

def __ixor__(self, other):
    self._assign(self ^ other); return self
```

### 🟩 Contoh Input

```python
c = BigIntegerList("1000")
b = BigIntegerList("123")

c += b
print(c)   # 1123

c *= BigIntegerList("2")
print(c)   # 2246

c **= BigIntegerList("2")
print(c)   # 5044516
```

### 🟩 Output

```
1123
2246
5044516
```

---

## ✅ Kesimpulan

Dari implementasi di atas dapat disimpulkan bahwa:

- ✅ Big Integer ADT dapat mengatasi keterbatasan tipe integer bawaan hardware
- ✅ Implementasi dengan **Linked List** cocok untuk operasi insert digit yang fleksibel
- ✅ Implementasi dengan **Python List** lebih simpel dan mudah di-index
- ✅ Semua operasi aritmatika, bitwise, perbandingan, dan assignment combo berhasil diimplementasikan

---

## 🚀 Cara Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/KaivalAmamiya/Tugas-Struktur-Data-Big-Integer.git
cd Tugas-Struktur-Data-Big-Integer
```

### 2. Jalankan Program

```bash
# Versi Linked List
python big_integer_linked_list.py

# Versi Python List
python big_integer_list.py
```

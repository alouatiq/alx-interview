# 0x01. Lockboxes

## 📚 Description

This project is a classic algorithmic problem aimed at determining if all boxes in a given list can be opened. Each box may contain keys to other boxes. The task is to design an efficient solution using graph traversal techniques.

---

## 🧠 Problem Statement

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to other boxes.

- A key with the same number as a box opens that box.
- The first box `boxes[0]` is always unlocked.
- Your goal is to determine whether all boxes can be opened starting from the first one.

---

## ✅ Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All Python files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- Code must follow **PEP 8** style (version 1.7.x)
- The first line of all files must be exactly `#!/usr/bin/python3`
- All files must be executable and end with a new line

---

## 🔧 Usage

Create a file named `main_0.py`:

```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
```

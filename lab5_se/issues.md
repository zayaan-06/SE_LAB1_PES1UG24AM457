# Lab 5 – Issues Table (todo_manager.py)

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| B605 os.system with string concat | Security (High, CWE-78) | 57 | `address` is concatenated into a shell command, so shell injection is possible | Validate address with a regex; use `subprocess.run([...])` as an argument list, no shell, with `stdin=` file |
| B301 / B403 pickle load | Security (Medium/Low, CWE-502) | 3, 47 | `pickle.load` can execute arbitrary code from an untrusted file | Replace pickle with JSON for save/load (convert keys back to int on load) |
| B311 random.choice | Security (Low, CWE-330) | 70 | `random` is not cryptographically secure | Use `secrets.choice` |
| W0102 mutable default arg | Bug | 11 | `labels=[]` is shared across calls and was never used | Remove the unused parameter |
| R1710 inconsistent return | Bug | 33 | `findTask` returns an id or implicitly None | Add explicit `return None` |
| E0001 import os syntax error | Environment | 2 | Pylint picked up a local file named `os.py` in the folder; `os` import is also now unused | Remove `import os`; delete/rename any stray `os.py` |
| W1514 open without encoding | Bug/portability | 51 | Default encoding depends on platform | Add `encoding="utf-8"` |
| E225 | Style (flake8) | 12 | Missing whitespace around `=` | `task_id = len(tasks) + 1` |
| E303 | Style (flake8) | 40 | 3 blank lines | Reduce to 2 |
| E261 | Style (flake8) | 69 | One space before inline comment | Two spaces before `#` |
| E231 | Style (flake8) | 74 | No space after `,` | Add space |
| C0103 naming | Style (pylint) | many | camelCase functions/variables | Rename to snake_case |
| C0114 / C0116 docstrings | Style (pylint) | 1, 11, 19... | Missing module/function docstrings | Add docstrings |

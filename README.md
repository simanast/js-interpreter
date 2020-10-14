## Интерпретатор JavaScript

- Установить antlr4 и сгенерировать лексер и парсер [по инструкции](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md)

- Установить библиотеку antlr4-runtime
```
pip install antlr4-python3-runtime
```
- Чтобы запустить тесты, из корневой папки проекта выполните
```
python -m unittest test\test.py
```

Источники:
- [Грамматика](https://github.com/antlr/grammars-v4/tree/master/javascript/javascript)
- [Тесты](https://github.com/jquery/esprima/tree/master/test/)
# ...


## Как запустить


### Установить зависимости
```pip install -r requirements.txt```


### Help

```gendiff -h```

### Сравнение файлов (JSON)

```gendiff before.json after.json```


### Сравнение файлов (yaml)
```gendiff before.yml after.yml```


### Сравнение файлов (ini)
```gendiff before.ini after.ini```


### Плоский формат вывода
```gendiff  --format plain before.json after.json```

### Тест
```python -m unittest -v test.py```


### Линтер
```pylint parsers.py```
 

### Цель проекта

тестовое задание
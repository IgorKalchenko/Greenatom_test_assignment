# Greenatom_test_assignment


Решения тестовых заданий на позицию python-стажёр в Гринатом. 

## Как запустить код:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/IgorKalchenko/Greenatom_test_assignment
```

```
cd Greenatom_test_assignment
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

## 1 задание

Какие шаги следует предпринять, если пользователь сообщит о том, что API возвращает ему ошибку 500?

**[Решение](Q1.py)**

## 2 задание

Какие проблемы в следующем фрагменте кода? Как его следует исправить? Необходимо исправить ошибку и переписать код ниже с использованием типизации.

```python
def create_handlers(callback):
    handlers = []
    for step in range(5):
        handlers.append(lambda: callback(step))
    return handlers


def execute_handlers(handlers):
    for handler in handlers:
        handler()
```

**[Решение](Q2.py)**

## 3 задание

Сколько HTML-тегов в коде главной страницы сайта [greenatom.ru](https://greenatom.ru/)? Сколько из них содержит атрибуты? Необходимо написать скрипт на Python, который выводит ответы на вопросы выше.

**[Решение](Q3.py)**


## 4 задание

Написать функцию на Python, которая возвращает текущий публичный IP-адрес компьютера с использованием сервиса [ifconfig.me](https://ifconfig.me/).

**[Решение](Q4.py)**


## 5 задание

Написать функцию на Python, выполняющую сравнение версий по условиям ниже.

```
- Return -1 if version A is older than version B
- Return 0 if versions A and B are equivalent
- Return 1 if version A is newer than version B
- Each subsection is supposed to be interpreted as a number, therefore 1.10 > 1.1.
```

**[Решение](Q5.py)**

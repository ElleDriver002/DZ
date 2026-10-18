# Lesson 10 — Page Object + Allure

Доработка ДЗ №7 (Page Object) с добавлением типизации методов и отчётов Allure.

## Структура проекта

```
lesson_10/
├── pages/
│   ├── login_page.py        # страница логина Sauce Demo
│   ├── inventory_page.py    # каталог товаров
│   ├── cart_page.py         # корзина
│   ├── checkout_page.py     # оформление заказа
│   └── calculator_page.py   # медленный калькулятор
├── tests/
│   ├── test_shop.py         # сценарий покупки
│   └── test_calculator.py   # сценарий калькулятора
├── conftest.py              # фикстуры Chrome / Firefox
├── requirements.txt
├── allure-results/          # результаты прогона (не пушить)
├── allure-report/           # HTML-отчёт (не пушить)
└── README.md
```

## Установка

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux / macOS:
source venv/bin/activate

pip install -r lesson_10/requirements.txt
```

Нужен [Allure Commandline](https://docs.qameta.io/allure/#_installing_a_commandline):

- Windows: `scoop install allure`
- macOS: `brew install allure`
- Linux: скачать release с GitHub и добавить в PATH

## Запуск тестов и формирование отчёта Allure

```bash
# Запуск всех тестов, результаты сохраняются в allure-results
pytest lesson_10/tests -v --alluredir=lesson_10/allure-results

# Интерактивный просмотр отчёта (откроется в браузере)
allure serve lesson_10/allure-results
```

Статический HTML-отчёт:

```bash
allure generate lesson_10/allure-results -o lesson_10/allure-report --clean
allure open lesson_10/allure-report
```

## Просмотр отчёта

После `allure serve` отчёт открывается в браузере. В нём видны:

- Title и Description тестов
- Feature и Severity
- Пошаговые Steps с результатами assert

> Папки `allure-results` и `allure-report` **не нужно** пушить в репозиторий  
> (в проекте лежат только пустые директории с `.gitkeep`).

## Проверка стиля кода

```bash
flake8 lesson_10
```

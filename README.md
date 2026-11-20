# style-guide-project

Руководство по стилю документации проекта FileTransfer — асинхронной
клиент-серверной системы удалённой передачи файлов изображений.
Руководство ведётся по методологии Docs as Code: исходные тексты в Markdown,
сборка сайта MkDocs, проверки и публикация в GitHub Actions.

Сайт: <https://filippovvladimir.github.io/style-guide-project/>

Репозиторий: <https://github.com/FilippovVladimir/style-guide-project>

## Структура

```text
docs/                 исходные тексты руководства
  style/              стиль изложения
  formatting/         оформление
  content/            содержание документов
  doc-templates/      шаблоны документов
scripts/check_terms.py  проверка терминологии и буквы «ё»
.markdownlint-cli2.yaml правила линтера Markdown
.github/workflows/    CI/CD
mkdocs.yml            настройки сайта и навигация
```

## Быстрый старт

```bash
pip install -r requirements.txt
mkdocs serve
```

Как предложить изменение — в [CONTRIBUTING.md](CONTRIBUTING.md).

## Авторы

Филиппов Владимир Леонидович, Шукалов Андрей Денисович, группа К3439,
Университет ИТМО.

"""Проверка терминологии и буквы «ё» в документации (правила ТР-2, ОП-1, ОП-2).

Запуск: python scripts/check_terms.py docs
Фрагменты между <!-- terms-off --> и <!-- terms-on --> не проверяются,
как и код (блоки ``` и `встроенный код`) и заголовки блоков !!!.
"""
import re
import sys
from pathlib import Path

# (регулярное выражение, сообщение, учитывать ли регистр)
RULES = [
    (r"\bскачк\w*|\bскачивани\w*|\bдаунлоад\w*", "ТР-2: используйте «загрузка»", False),
    (r"\bюзер\w*|\bпользак\w*", "ТР-2: используйте «оператор» или «пользователь»", False),
    (r"\bфронт\b|\bморд[аы]\b", "ТР-2: используйте «клиент»", False),
    (r"\b(?:GRPC|Grpc|грпц)\b", "ТР-2: пишите «gRPC»", True),
    (r"\bQT\b", "ТР-2: пишите «Qt»", True),
    (r"\bпротобаф\w*", "ТР-2: пишите «Protocol Buffers» или «protobuf»", False),
    (r"\bреквест\w*", "ТР-3: используйте «запрос»", False),
    (r"\bбранч\w*", "ТР-3: используйте «ветка»", False),
    (r"\bобъем\w*", "ОП-1: пишите «объём»", False),
    (r"\bудаленн\w*", "ОП-1: пишите «удалённый»", False),
    (r"\bпередает\b|\bпередается\b", "ОП-1: пишите «передаёт(ся)»", False),
    (r"\bсохраненн\w*", "ОП-1: пишите «сохранённый»", False),
    (r'"[А-Яа-яЁё][^"\n]*"', "ОП-2: используйте кавычки «ёлочки»", True),
]

FENCE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE = re.compile(r"`[^`]*`")
LINK_URL = re.compile(r"\]\([^)]*\)")


def check_file(path: Path) -> list[str]:
    errors = []
    in_code = False
    enabled = True
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if "<!-- terms-off -->" in line:
            enabled = False
        if "<!-- terms-on -->" in line:
            enabled = True
            continue
        if FENCE.match(line):
            in_code = not in_code
            continue
        if in_code or not enabled or line.lstrip().startswith("!!!"):
            continue
        text = LINK_URL.sub("]()", INLINE_CODE.sub("", line))
        for pattern, message, case_sensitive in RULES:
            flags = 0 if case_sensitive else re.IGNORECASE
            for match in re.finditer(pattern, text, flags=flags):
                errors.append(f"{path}:{number}: «{match.group(0)}» — {message}")
    return errors


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "docs")
    errors = []
    for path in sorted(root.rglob("*.md")):
        errors.extend(check_file(path))
    for error in errors:
        print(error)
    print(f"Проверено файлов: {len(list(root.rglob('*.md')))}, замечаний: {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

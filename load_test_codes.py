import requests
import re
import os

# Список задач
# tasks = ["any", "dict", "final", "kwargs", "list", "optional", "parameter", "return",
#          "tuple", "typealias", "union", "variable"]
tasks = [
    "await",
    "callable",
    "class-var",
    "decorator",
    "empty-tuple",
    "generic",
    "generic2",
    "generic3",
    "instance-var",
    "literal",
    "literalstring",
    "self",
    "typed-dict",
    "typed-dict2",
    "typed-dict3",
    "unpack",
]

# Папка, в которую будут сохраняться файлы
# output_dir = "tasks/basic"
output_dir = "tasks/intermediate"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


def parse_tasks() -> None:
    base_url = "https://python-type-challenges.zeabur.app/intermediate/"

    for i, task in enumerate(tasks, start=1):
        url = f"{base_url}{task}"
        print(f"Обработка {url}...")

        try:
            response = requests.get(url)
            response.raise_for_status()
            html_content = response.text

            # Используем регулярное выражение для поиска содержимого внутри let testCode = "..."
            match = re.search(r'let\s+testCode\s*=\s*"(.*?)";', html_content, re.DOTALL)

            if match:
                extracted_code = match.group(1)

                final_code = extracted_code.encode().decode("unicode_escape")

                filename = f"t{i}_{task}.py"
                filepath = os.path.join(output_dir, filename)

                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(final_code)

                print(f"Успешно сохранено в {filename}")
            else:
                print(f"Ошибка: Не удалось найти testCode на странице {task}")

        except Exception as e:
            print(f"Произошла ошибка при обработке {task}: {e}")


if __name__ == "__main__":
    parse_tasks()

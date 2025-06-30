import json
import base64
import sys


def hex_to_base64(hex_str):
    raw_bytes = bytes.fromhex(hex_str)
    return base64.b64encode(raw_bytes).decode()


def main():
    if len(sys.argv) != 2:
        print(f"Использование: python {sys.argv[0]} <путь_к_файлу.json>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as f:
            users = json.load(f)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)

    with open('hashes.txt', 'w') as out_file:
        for user in users:
            username = user.get('lower_name') or user.get('name') or user.get('email')
            iterations = 50000
            salt_hex = user.get('salt')
            hash_hex = user.get('passwd')

            if not salt_hex or not hash_hex:
                print(f"Пропущен пользователь {username}: отсутствуют salt или passwd")
                continue

            salt_b64 = hex_to_base64(salt_hex)
            hash_b64 = hex_to_base64(hash_hex)

            line = f"{username}:sha256:{iterations}:{salt_b64}:{hash_b64}\n"
            out_file.write(line)

    print("Файл hashes.txt создан успешно.")


if __name__ == "__main__":
    main()

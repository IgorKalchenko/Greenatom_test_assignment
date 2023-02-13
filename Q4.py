import requests


def get_public_ip(service_url: str) -> str:
    return requests.get(service_url).text


if __name__ == "__main__":
    public_ip = get_public_ip(service_url='https://ifconfig.me/')
    print(f"Ваш текущий публичный IP-адрес: {public_ip}")

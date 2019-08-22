import requests
from requests.exceptions import RequestException

def get_one_page(url):
    try:
        respone = requests.get(url)
        if respone.status_code == 200:
            return respone.text
        else:
            return None
    except RequestException:
        return None

def main():
    url = 'https://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)

if __name__ == '__main__':
    main()
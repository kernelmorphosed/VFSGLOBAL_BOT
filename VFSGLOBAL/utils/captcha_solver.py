import time
import requests
import logging

def get_request(api, id_post):
    time.sleep(30)
    response = requests.get(f'https://rucaptcha.com/res.php?key={api}&action=get&id={id_post}&json=1')

    if response.status_code == 200:
        json_response = response.json()
        answer = json_response.get("request")
        if answer == 'CAPCHA_NOT_READY':
            return None
        else:
            logging.info(answer)
            return answer
    else:
        logging.error("Ошибка выполнения запроса. Статус код:", response.status_code)
        return None

def solve_captcha(api, sitekey, pageurl):
    json_data = {
        "key": api,
        "method": "turnstile",
        "sitekey": sitekey,
        "pageurl": pageurl,
        "json": 1
    }

    response = requests.post('https://rucaptcha.com/in.php', json=json_data)

    if response.status_code == 200:
        json_response = response.json()
        id_post = json_response.get("request")
        answer = None
        while answer is None:
            answer = get_request(api, id_post)
        return answer
    else:
        logging.error("Ошибка выполнения запроса. Статус код:", response.status_code)
        return None

from typing import Optional

import requests
import json


def magic_todo(task_name: str, spiciness: int = 3, parent_task: Optional[str] = None)->Optional[dict]:
    endpoint: str = "https://goblin.tools/api/todo/"
    data = {
        "Text": task_name,
        "Spiciness": spiciness,
        "Ancestors": [parent_task] if isinstance(parent_task, str) else []
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Content-Type": "application/json"
    }
    res = requests.post(
        endpoint,
        data=json.dumps(data),
        headers=headers
    )
    if res.status_code != 200:
        return
    res.encoding = res.apparent_encoding
    sub_task_list:list = [
        {"task": sub_task} for sub_task in res.json()
    ]
    return {
        "task_name": task_name,
        "sub_task": sub_task_list,
    }


import pprint
todo = magic_todo("カレーを作る", 4)
pprint.pprint(todo)
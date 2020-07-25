import requests
from bs4 import BeautifulSoup
import json

res = requests.get("https://stackoverflow.com/questions")

soup = BeautifulSoup(res.text,"html.parser")

question_data = {
    "questions": []
}

questions = soup.select(".question-summary")

for que in questions:
    q = que.select_one(".question-hyperlink").getText()
    vote_count = que.select_one(".vote-count-post").getText()
    views = que.select_one(".views").attrs['title']
    tags = [i.getText() for i in (que.select('.post-tag'))]
    question_data['questions'].append({
        "question": q,
        "views" :views,
        "vote_count": vote_count,
        "tags": tags
    })

json_data = json.dumps(question_data, sort_keys=True, indent=4)

print(json_data)

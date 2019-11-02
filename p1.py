#파일 이름 json으로 하면 오류남
import json

diary = {
    'id' : 3,
    'title' : '아침부터 졸려죽겠네ㅠ',
    'body' : '자고싶다 자고싶다 자고싶다...',
}

print(diary)
print(type(diary))

diary_j = json.dumps(diary)     #dumps : dictionary --> json

print(diary_j)
print(type(diary_j))

diary_b = json.loads(diary_j)

#print(diary_b) 실행이 안되네;;
print(type(diary_b))
# TODO решите задачу
import json
def task(jsond)-> float:
    sum = 0
    for flout in jsond:
        sum = sum+flout['score']*flout['weight']
    return sum

name = 'input.json'
with open(name) as file:
    funct = json.load(file)
r = round(task(funct), 3)
print(r)

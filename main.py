import requests
import time
from os import system

lnk = "zUGSpCGcin03twxF9o6fKvNO"
INPUT_NOTE = "https://textdb.online/" + str(lnk)

def loop():
    while True:
        try:
            problem = requests.get(INPUT_NOTE).text
            if len(problem) < 3 or len(problem) > 500:
                continue
            print(problem)
            if problem == "okok":
                break
            with open("examples/rzn.txt", "w", encoding='UTF-8') as f:
                f.write("rzn_1\n" + problem)
            with open("examples/rzn.txt", encoding='UTF-8') as f:
                print(f.read())
            system("python src/alphageometry.py --problems_file examples/rzn.txt --problem_name rzn_1 > output.txt")
            with open("output.txt", encoding='UTF-8') as f:
                val = f.read()
            val = val.replace("⇒", " ⇒")
            val = val.replace("&", "and")
            print(val)
            change = "https://api.textdb.online/update/?key=" + str(lnk) + "&value=" + val
            requests.get(change)
        except Exception as e:
            print("[!] Error:", e)
        time.sleep(1)

if __name__ == "__main__":
    loop()

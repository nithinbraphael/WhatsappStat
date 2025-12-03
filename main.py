import re

RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'
WHITE = '\033[97m'

chat = open(input("Enter the file path: "), "r", encoding='utf-8')
messages = chat.readlines()

users = {}
t_interval = {'00': 0, '01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0}
day = {}
words = {}

for s in messages:
    try:
        pattern = r"^([^,]+),\s*([^–-]+)\s*[-–]\s*(.*?):\s*(.*)$"
        date, time, name, message = re.match(pattern, s).groups()
        if name not in users:
            users[name] = 1
        else:
            users[name] += 1
        
        if len(time) == 8:
            time = '0'+ time
        t_interval[time[:2]] += 1

        if date in day:
            day[date] += 1
        else:
            day[date] = 1

        for i in message.split():
            if i.lower() in words:
                words[i.lower()] += 1
            else:
                words[i.lower()] = 1
    except:
        for i in s.split():
            if i.lower() in words:
                words[i.lower()] += 1
            else:
                words[i.lower()] = 1

print(f"The most messages were from {GREEN}{max(users, key=users.get)} with {max(users.values())}{RESET} messages!\nThere were a total of {GREEN}{sum(users.values())} messages. \n{RESET}")
for i in users:
    print(f"{WHITE}{i}: {GREEN}{users[i]}{RESET}")
print()

print(f"The time interval most chatted was at {GREEN}{max(t_interval, key=t_interval.get)}00 hours with {max(t_interval.values())} messages {RESET}")
print(f"The day most talked is at {GREEN}{max(day, key=day.get)} with {max(day.values())} messages. {RESET}")
print(f"There were {GREEN}{len(words)} unique words throughout the chats and a total of {sum(words.values())} words{RESET}. \n100 of the most commonly used words are listed below.")
print()
c = 0
for key, value in sorted(words.items(), key=lambda item: item[1], reverse=True):
    if c > 100:
        break
    else:
        print(f"{GREEN}{key}{RESET} with {value} occurences.")
        c += 1
# Basic Dictionary Creation
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print("Dictionary:", eng2sp)
print(eng2sp['two'])
print(len(eng2sp))
print(sorted(eng2sp))
print('one' in eng2sp)
print('five' in eng2sp)
print('uno' in eng2sp)

# Movie Dictionary
million_dollar = {"sanju": 2018, "tiger zinda hai": 2017, "dangal": 2016, "bahubali": 2017, "bajrangi bhai jaan": 2015}
bold_million_dollar = million_dollar.fromkeys(million_dollar, "10000000")
print(bold_million_dollar)
print(million_dollar.get("bahubali1"))
print(million_dollar.get("bahubali1", 2015))
print(million_dollar.keys())
print(million_dollar.values())
print(million_dollar.items())
million_dollar.update({"bahubali1":2015})
print("million_dollar = ",million_dollar)
#States Dictionary
states = {}
states.update({"hariyana": "chandigharh"})
states.update({"bihar": "patna"})
states.update({"west bengal": "kolkata"})
print("States Dictionary:", states)
for key in states:
    print(key, states[key])
del states["west bengal"]
print("states = ",states)

d1 = {'C': 92,'Java': 66,'Python': 85}

low = min(d1.values())   

for k in d1:
    if d1[k]==low:
        print(k)
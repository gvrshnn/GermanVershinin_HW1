characters = str(input())
characters = characters + ' '
string = ''
count = 0
while len(characters) > 1:
    if characters[0] == characters[1]:
        count = count + 1
        characters = characters[1:]
    else:
        count = count + 1
        string = string + characters[0] + str(count)
        count = 0
        characters = characters[1:]
print(string)
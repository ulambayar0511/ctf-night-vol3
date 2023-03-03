brainfuck_characters = [
    "[", "]", "+", "-", "." , "," , "<" , ">"
]

content = open('notdone.txt').read()

bf = []
for c in content:
    if c in brainfuck_characters:
        bf.append(c)

print(''.join(bf))
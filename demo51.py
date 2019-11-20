import sys
text=''
while 1:
    c = sys.stdin.read(1)  #need to input at terminal
    text=text + c
    if c == '\n':
        break
    #     pass
    # pass
print(f'text={text}')

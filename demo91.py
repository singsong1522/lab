file1 = open('data\\Python_introduction',
             encoding='utf8')
readme_txt = file1.read()
file1.close()
print(type(readme_txt),len(readme_txt),readme_txt[:50])

for _ in range(5):
    with open('data\\write_back','w', encoding='utf-8') as file2:
        file2.write(readme_txt)

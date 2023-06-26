import sys
def write_text_file(filename, text):
    try:
        file = open(filename,'w')
        return file.write(text)
    except:
        print("There is an error.")
    finally:
        file.close()
def text1():
    lista = []
    while True:
        text = sys.stdin.readline()
        text = text.strip()
        if text == '':
            break
        else:
            lista.append(text)
    return '\n'.join(lista)

name = sys.stdin.readline()
text = text1()
write_text_file(name, text)
with open(name, 'r') as f:
    content = f.readlines()
    for i in content:
        line = i.strip()
        print(line)
    """
    Another method
    for i in range(len(content)):
        line = content[i]
        line = line.strip()
        print(line)
    """



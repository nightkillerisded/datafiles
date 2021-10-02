fileobj=open("zen.txt")
it=iter(fileobj)
lines=[]
while True:
    try:
        line=next(it)
        line=line.strip()
        lines.append(line)
    except StopIteration:
        break
print(lines)

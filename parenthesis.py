from stack import Stack
p1 = "{({{[]}})}("
################################
map_p = {
'{' : 1,
'}' : -1,
'(' : 2,
')' : -2,
'[' : 3,
']' : -3
}
s = Stack()
for p in p1:
    if s.peek() is None:
        s.push(p)
    else:
        if map_p[p] + map_p[s.peek()] == 0:
            s.pop()
        else:
            s.push(p)
if len(s):
    print("not closed properly")

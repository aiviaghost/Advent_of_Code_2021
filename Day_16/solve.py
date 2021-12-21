from math import prod

with open("input") as f:
    data = bin(int(f.readline(), 16))[2 : ]
    data = "0" * (4 - (len(data) % 4)) + data if len(data) % 4 != 0 else data

ans1 = 0

def decode(BITS):
    global ans1

    VERSION = int(BITS[ : 3], 2)
    ans1 += VERSION
    TYPE_ID = int(BITS[3 : 6], 2)
    
    curr_expr = []
    if TYPE_ID == 4:
        LITERAL_VALUE = ""
        i = 6
        while True:
            LITERAL_VALUE += BITS[i + 1 : i + 5]
            i += 5
            if BITS[i - 5] == "0":
                break
        curr_expr.append(int(LITERAL_VALUE, 2))
    else:
        LENGTH_TYPE_ID = BITS[6]
        if LENGTH_TYPE_ID == "0":
            LEN = int(BITS[7 : 22], 2)
            i = 22
            while i - 22 < LEN:
                next_i, expr = decode(BITS[i : ])
                curr_expr.append(expr)
                i += next_i
        else:
            NUM_PACKETS = int(BITS[7 : 18], 2)
            i = 18
            for _ in range(NUM_PACKETS):
                next_i, expr = decode(BITS[i : ])
                curr_expr.append(expr)
                i += next_i
    return (i, (TYPE_ID, curr_expr))

def match_op(type_id):
    match type_id: # Python 3.10 :D
        case 0:
            return lambda *x: sum(list(x))
        case 1:
            return lambda *x: prod(list(x))
        case 2:
            return lambda *x: min(list(x))
        case 3:
            return lambda *x: max(list(x))
        case 5:
            return lambda x, y: x > y
        case 6:
            return lambda x, y: x < y
        case 7:
            return lambda x, y: x == y

def parse_expr(expr):
    if expr[0] == 4:
        return expr[1][0]
    op = match_op(expr[0])
    return op(*(parse_expr(_) for _ in expr[1]))

_, expr = decode(data)

print(ans1)
print(parse_expr(expr))

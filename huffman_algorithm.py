from queue import PriorityQueue
from collections import Counter


class Tree:
    def __init__(self,sign,right,left):
        self.sign=sign
        self.right=right
        self.left=left






def szyfr():
    TAB=[]
    with open("kod_huffmana.txt", "r") as file:
        text = file.read()
    symbol_counts = Counter(text)
    unique_symbols = set(text)
    unique_symbol_list = list(unique_symbols)
    root=kod_huffmana(unique_symbol_list,symbol_counts)

    
    def prefix(z,ROAD):
        nonlocal file,root
        if z.right==None and z.left==None:
            file.write(z.sign+" "+"".join(ROAD)+"\n")
        else:
            if z.right!=None:
                ROAD.append("1")
                prefix(z.right,ROAD)
                ROAD.pop()
            if z.left!=None:
                ROAD.append("0")
                prefix(z.left,ROAD)
                ROAD.pop()

    with open("code.txt", "w") as file:
        prefix(root,[])
    return root

    
        
def kod_huffmana(unique_symbols,symbol_counts):
    n=len(symbol_counts)
    Q=PriorityQueue()
    counter=n
    for symbol in unique_symbols:
        frequency=symbol_counts[symbol]
        ascii_code=ord(symbol)
        sign=Tree(symbol,None,None)
        Q.put((frequency,ascii_code,sign))

    while counter!=1:
        x=Q.get()
        y=Q.get()
        connected_sign=Tree("connected",x[2],y[2])
        sum=x[0]+y[0]
        Q.put((sum,counter,connected_sign))
        counter-=1

    z=Q.get()
    return z[2]

root = szyfr()

def decoding(root):
    pointer = root
    decoded_text = ""

    def get_bit(byte, position):
        return (byte >> position) & 1

    with open("bin_code.bin", "rb") as binary_file:
        byte = binary_file.read(1)
        while byte:
            for bit_position in range(7, -1, -1):
                bit = get_bit(byte[0], bit_position)
                if bit == 1 and pointer.right != None:
                    pointer = pointer.right
                elif bit == 0 and pointer.left != None:
                    pointer = pointer.left
                elif pointer.left == None and pointer.right == None:
                    decoded_text += pointer.sign
                    pointer = root
                    if bit == 1 and pointer.right != None:
                        pointer = pointer.right
                    elif bit == 0 and pointer.left != None:
                        pointer = pointer.left
            byte = binary_file.read(1)


    return decoded_text

        
        

# print(decoding(root)) You can decode your file if you have already run c++ code.

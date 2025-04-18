from typing import List, Tuple
from IPython.display import Latex
class Tensor:
    def __init__(self, symbol: str):
        self.symbol = symbol
            
    def transpose(self):
        if self.symbol[-1] == "ᵀ":
            self.symbol = self.symbol[:-1]
        else:
            self.symbol = self.symbol + "ᵀ"
    
    @property
    def T(self):
    
        newTensor = Tensor(self.symbol)
        newTensor.transpose()
        return newTensor
    
    def __repr__(self):
        return f"{self.symbol}"

    
class Number:
    def __init__(self, symbol: str):
        self.symbol = symbol
        
    def __repr__(self):
        return f"{self.symbol}"
    def __mul__(self, other):
        if self.symbol == "":
            return Number(other.symbol)
        if other.symbol == "":
            return Number(self.symbol)
        return Number(f"({self.symbol})({other.symbol})")
    def __lt__(self, other):
        return Number(f"{self.symbol}<{other.symbol}")
    def __gt__(self, other):
        return Number(f"{self.symbol}>{other.symbol}")
 
    
    


def transpose(A: List[Tensor]):
    B = A[:]
    for i in range(len(A)):
        B[i] = B[i].T
    B = B[::-1]
    return B

def tp_ut(A: List[Tensor], B:List[Tensor], C:List[Tensor], num: Number = Number("")) -> Tuple[List[Tensor], Number]:
    return A + C + B, num

def tp_lt(A: List[Tensor], B:List[Tensor], C:List[Tensor], num: Number = Number("")) -> Tuple[List[Tensor], Number]:
    return A +transpose(C) + B, num

def tp_us(A: List[Tensor], B:List[Tensor], C:List[Tensor], num: Number = Number("")) -> Tuple[List[Tensor], Number]:
    return A + C + transpose(B), num

def tp_ls(A: List[Tensor], B:List[Tensor], C:List[Tensor], num: Number = Number("")) -> Tuple[List[Tensor], Number]:
    return A + transpose(C) + transpose(B), num

def concatenate(A: List[Tensor]) -> str:
    return "".join([str(tensor) for tensor in A])

def contraction(A: List[Tensor], B:List[Tensor]) -> Number:
    a = concatenate(A)
    b = concatenate(B)
    if a< b:
        return Number(f"({concatenate(A)}):({concatenate(B)})")
    else:
        return Number(f"({concatenate(B)}):({concatenate(A)})")


def tp(A: List[Tensor], B:List[Tensor], C:List[Tensor], num: Number = Number("")) -> Tuple[List[Tensor], Number]:
    return A, contraction(B, C) * num


c = concatenate
A = [Tensor("A")]
B = [Tensor("B")]
C = [Tensor("C")]
D = [Tensor("D")]
X = [Tensor("X")]
T = transpose
ut = tp_ut
us = tp_us
lt = tp_lt
ls = tp_ls


# # Testing 

# print(*tp(A, B, *tp(C, D, X)))
# print(*tp(A, C, *tp(B, D, X)))
# print(us(C, D, X))
# print(c(ls(A, B, *ls(C, D, X))))
assert c(tp(A, B, *tp(C, D, X))) == c(tp(A, C, *tp(B, D, X)))






## Generate database



tensors = [A, B, C, D, X, transpose(A), transpose(B), transpose(C), transpose(D), transpose(X)]
tps = [tp, ut, lt, us, ls]



tensorsLen = len(tensors)
tpsLen = len(tps)

database = dict()

for i in range(tensorsLen):
    for j in range(tpsLen):
        for k in range(tensorsLen):
            for l in range(tensorsLen):
                for m in range(tpsLen):
                    for n in range(tensorsLen):
                        identifier=f"{i} {j} {k} {l} {m} {n}"
                        A = tensors[i]
                        tp1 = tps[j]
                        B = tensors[k]
                        C = tensors[l]
                        tp2 = tps[m]
                        D = tensors[n]
                        database[identifier] = c(tp1(A, B, *tp2(C, D, X)))

def maptps(name: str) -> str:
    if name == "tp":
        return "⊗"
    elif name == "tp_ut":
        return "⊗^~"
    elif name == "tp_lt":
        return "⊗_~"
    elif name == "tp_us":
        return "⊗^-"
    elif name == "tp_ls":
        return "⊗_-"


def reconstructFunctionFromIdentier(string: str) -> str:
    i, j, k, l, m, n = map(int, string.split(" "))
    A = tensors[i]
    tp1 = tps[j]
    B = tensors[k]
    C = tensors[l]
    tp2 = tps[m]
    D = tensors[n]
    return f"({str(A)[1:-1]} {maptps(tp1.__name__)} {str(B)[1:-1]})({str(C)[1:-1]} {maptps(tp2.__name__)} {str(D)[1:-1]})"


def performCheck(checkKey: str):

    for key in database.keys():
        if key == checkKey:
            continue
        if database[key] == database[checkKey]:
            print(reconstructFunctionFromIdentier(checkKey), " same as : ", reconstructFunctionFromIdentier(key))
    print("\n")

if __name__ == "__main__":

    # Example usage

    #Follows the form Tensor1 Operator1 Tensor2 Tensor3 Operator2 Tensor4
    # Example: "0 4 1 2 4 3" means A ut B C us D

    # tensors = [A, B, C, D, X]
    # tps = [tp, ut, lt, us, ls]
    # 0 = A, 4 = ls, 1 = B, 2 = C, 4 = ls, 3 = D
    #ls stands for lower straight(line), us stands for upper straight(line)
    #lt stands for lower tilde, ut stands for upper tilde
    #tp is regular tensor product




    form_to_check = "0 4 1 2 4 3"

    performCheck(form_to_check)
    # (A ⊗_- B)(C ⊗_- D)  same as :  (A ⊗^~ Bᵀ)(D ⊗^~ Cᵀ)
    # (A ⊗_- B)(C ⊗_- D)  same as :  (A ⊗^~ Bᵀ)(D ⊗^- C)
    # (A ⊗_- B)(C ⊗_- D)  same as :  (A ⊗_~ Bᵀ)(C ⊗_~ Dᵀ)
    # (A ⊗_- B)(C ⊗_- D)  same as :  (A ⊗_~ Bᵀ)(C ⊗_- D)
    # (A ⊗_- B)(C ⊗_- D)  same as :  (A ⊗^- B)(D ⊗^~ Cᵀ)
    # (A ⊗_- B)(C ⊗_- D)  same as :  (A ⊗^- B)(D ⊗^- C)
    # Which is true!


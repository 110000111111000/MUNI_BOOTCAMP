import pandas as pd

A = pd.Series(['apple', 'cherry', 'grass', 'deer', 'flower','paula'])
B = pd.Series(['orange', 'pear', 'grape', 'lilic', 'apple'])
C = pd.Series(['orange', 'pear', 'yas', 'bluberry', 'gripfruit' , 'paula'])


print("A:",len(A))
print("B:",len(B))
print("C:",len(C))

AiB = A[A.isin(B)]
print("A intersection B", len(AiB))

AiC = A[A.isin(C)]
print("A intersection C", len(AiC))

BiC = B[B.isin(C)]
print("B intersection C", len(BiC))

AiBiC = AiB[AiB.isin(C)]
print("A intersection B intersection C", len(AiBiC))

print("As concatenation:", pd.concat([A,B,C]))
AuBuC = set(pd.concat([A,B,C]))
print("and as a set:", AuBuC)
print("A union B union C", len(AuBuC))



print("In-Ex", len(A) + len(B) + len(C) - len(AiB) - len(AiC) - len(BiC) + len(AiBiC))
print("The subset that Vaji wants", AuBuC,len(AuBuC))
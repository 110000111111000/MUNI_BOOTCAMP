import pandas as pd

u = pd.Series([ 'grass','watermelon','apple', 'lilic', 'banana', 'cherry',  'deer', 'flower','paula', 'grass','orange','pear','grape' ,'yas','bluberry', 'gripfruit' ])
a = pd.Series(['apple', 'cherry', 'grass', 'deer', 'flower','paula' ])
b = pd.Series(['orange', 'pear', 'grape', 'lilic'])
c = pd.Series(['orange', 'pear', 'yas', 'bluberry', 'gripfruit' , 'paula'])

# Display Series 'a' and 'b'
#print("Series 'a':")
#print(a)

#print("Series 'b':")
#print(b)

series_a_and_b = pd.concat([a,b])
#print('series_a_and_b:',len(series_a_and_b))

# A inter B
subset_a_is_b = a[a.isin(b)]
#print('Count of a & b:',len(a)+ len(b) - len(subset_a_is_b))

# AuBuC
series_a_and_b_and_c = pd.concat([a,b,c])
#print('series_a_and_b_and_c:',len(series_a_and_b_and_c))
#print(series_a_and_b_and_c)

# A inter C
subset_a_is_c = a[a.isin(c)]
#print('len subset_a_is_c:',len(subset_a_is_c))

# B inter C
subset_b_is_c = b[b.isin(c)]
#print('len subset_b_is_c: ', len(subset_b_is_c))

subset_a_is_b_is_c = set(a).intersection(b).intersection(c)
#print('len subset_a_is_b_is_c',len(subset_a_is_b_is_c))
print('Count of a & b & c:',len(a)+ len(b) +len(c) - len(subset_a_is_b) -len(subset_b_is_c) - len(subset_a_is_c) + len(subset_a_is_b_is_c) )

subset_u1 = pd.concat([a,b ,c])
print('subset_u1',len(subset_u1), subset_u1)
print('subset_a_is_b', subset_a_is_b,len(subset_a_is_b))
print('subset_a_is_c', subset_a_is_c,len(subset_a_is_c))
print('subset_b_is_c', subset_b_is_c,len(subset_b_is_c))

subset_u2 = subset_u1[~subset_u1.isin(subset_a_is_b)]
print('subset_u2',subset_u2,len(subset_u2))
	
subset_u3 = subset_u2[~subset_u2.isin(subset_a_is_c)]
print('subset_u3', subset_u3,len(subset_u3))

subset_u4 = subset_u3[~subset_u3.isin(subset_b_is_c)]
print('subset_u4',subset_u4,len(subset_u4))

#print('series_a_and_b_and_c',subset_a_is_b_is_c)
subset_u5 = pd.concat([subset_u4, pd.Series(list(subset_a_is_b_is_c))])
print('subset_u5',subset_u5)

subset_u11 = u[~u.isin(subset_u5)] 
subset_u12 = subset_u11[~subset_u11.isin(subset_a_is_b)]
subset_u13 = subset_u12[~subset_u12.isin(subset_a_is_c)]
subset_u14 = subset_u13[~subset_u13.isin(subset_b_is_c)]
print('subset_u11', subset_u11, len(subset_u11))
print(subset_u14)


# use series.unique() function

 
# using series.unique() & set() function

seta = set(a)
print(seta)

setb = set(b)
print(setb)

setc = set(c)
print(setc)

print("seta U setb U setc :", seta.union(setb).union(setc))

subset_u = u[~u.isin(seta.union(setb).union(setc))]
print(subset_u)

#subset_a_is_b_is_c_1 = pd.Series(subset_a_is_b_is_c)
#subset_u5 = pd.concat([subset_a_is_b_is_c_1,subset_u4])

#subset_u = subset_u4 + subset_a_is_b_is_c
#subset_u = pd.concat([subset_u4, subset_a_is_b_is_c])
#print(subset_u)

#subset_u_a = u[~u.isin(a)]
#subset_u_is_a = a[a.isin(u)]

#print(subset_u_a,'len(subset_u_a):', len(subset_u_a))
#print(subset_u_is_a, 'len(subset_u_is_a):', len(subset_u_is_a))
#print(len(u)+len(a) - len(subset_u_is_a))




#subset_a = a[~a.isin(b)]
#print('subset_a:',subset_a)

#subset_a_subset_b = subset_a[~subset_a.isin(b)]
#print('subset_a_subset_b',subset_a_subset_b)

#subset_a_subset_b_subset_c = subset_a_subset_b[~subset_a_subset_b.isin(c)]
#print('subset_a_subset_b_subset_c',subset_a_subset_b_subset_c)
#print(len(subset_a_subset_b_subset_c))


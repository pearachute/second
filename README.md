# second
channel_name=list(np.array(df.iloc[:,1].tolist()))

# print(channel_name)

subscribe_num=list(np.array(df.iloc[:,3].tolist()))

subscribe_num=[i.split()[0] for i in subscribe_num]

subscribe_num=[i.rstrip('억만') for i in subscribe_num]

count=0

for i in subscribe_num:
    if '.' in i:
        subscribe_num[count]=i.replace('.','')
        count+=1

count=0

subscribe_num=[int(i) for i in subscribe_num]

for i in subscribe_num:
    count+=1
    if count ==3:
        subscribe_num[count-1]*=10
    elif count >=5:
        subscribe_num[count-1]/=100

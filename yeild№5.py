#!/usr/bin/env python
# coding: utf-8

# In[15]:


def user_connection(username):
    import random
    for i in range(random.randint(10, 20)):
        yield f"{username} message{i}"

def establish_connection(auth=True):
    import random
    id = f"{random.randint(0,100000000):010}"
    if auth:
        yield f"auth {id}"
    yield from user_connection(id)
    if auth:
        yield f"disconnect {id}"


# In[16]:


for i in establish_connection(): print(i) 


# In[17]:


for i in establish_connection(False): print(i) 


# In[18]:


def connection():
    import random
    connections = [establish_connection(True) for i in range(10)]
    connections.append(establish_connection(False))
    connections.append(establish_connection(False))
    while len(connections):
        conn = random.choice(connections)
        try:
            yield next(conn)
        except StopIteration:
            del connections[connections.index(conn)]


# In[19]:


for i in connection():
    print(i)


# In[22]:


def connect_user(input1):
    input1=input1.split()    
    if input1[0] =='aut':
        dictaut[input1[1]] = True
        with open('{}.txt'.format(input1[1]) , 'w') as f:
            f.write('создано'+'\n')
    elif input1[0] =='disconnect':
        dictaut[input1[1]] = False
    else:
        try:   
            if dictaut[input1[0]] == True:
                write_to_file(input1[1], '{}.txt'.format(inp[0]))
        except KeyError:
            return
            
def write_to_file(text,file):
    
    with open(file, 'a') as f:
        f.write(text+'\n')



            
    

    


# In[23]:


dictaut={}
for i in connection():
    connect_user(i)


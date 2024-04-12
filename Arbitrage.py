liquidity = {
    ("tokenA", "tokenB"): (17, 10),#170
    ("tokenA", "tokenC"): (11, 7),#77
    ("tokenA", "tokenD"): (15, 9),#135
    ("tokenA", "tokenE"): (21, 5),#105
    ("tokenB", "tokenC"): (36, 4),#144
    ("tokenB", "tokenD"): (13, 6),#78
    ("tokenB", "tokenE"): (25, 3),#75
    ("tokenC", "tokenD"): (30, 12),#360
    ("tokenC", "tokenE"): (10, 8),#80
    ("tokenD", "tokenE"): (60, 25),#1500
}
graph = {
    'tokenA': ['tokenB', 'tokenC', 'tokenD','tokenE'],
    'tokenB': ['tokenA', 'tokenC', 'tokenD', 'tokenE'],
    'tokenC': ['tokenA', 'tokenB', 'tokenD','tokenE'],
    'tokenD': ['tokenA', 'tokenB', 'tokenC', 'tokenE'],
    'tokenE': ['tokenA','tokenB','tokenC', 'tokenD']
}
# tokenB->tokenA->tokenD->tokenB, tokenB balance=3.770765. 5B->5.65532199A->2.45878132D->3.7707653B
# B->A->C->B 5B->5.65532199A->2.37213894C->13.3763566B

def bfs(graph, start, end):
    queue = []
    queue.append((start,['tokenB'],5))

    while queue:
        # 出队一个节点
        node_token,node_path,node_balance = queuepop(queue)
        for neighbor in graph[node_token]:
            if neighbor in node_path[1:]:
                continue
            new_path=node_path+[neighbor]
            new_balance=countbl(node_token,neighbor,node_balance)
            # 如果邻居节点为终点，返回路径
            if neighbor == end and new_balance>20:
                return new_path,new_balance
            # 将邻居节点加入队列
            queue.append((neighbor,new_path,new_balance))
    # 如果没有找到路径，返回空列表
    return []
def opt_bfs(graph, start, end):
    queue = []
    queue.append((start,['tokenB'],5))
    max_bal=0
    path_bal=[]
    while queue:
        # 出队一个节点
        node_token,node_path,node_balance = queuepop(queue)
        for neighbor in graph[node_token]:
            if neighbor in node_path[1:]:
                continue
            new_path=node_path+[neighbor]
            new_balance=countbl(node_token,neighbor,node_balance)
            # 如果邻居节点为终点，返回路径
            if neighbor == end and new_balance>max_bal and new_balance>20:
                max_bal=new_balance
                path_bal.append((new_path,new_balance))
            # 将邻居节点加入队列
            if(len(new_path)!=6):
                queue.append((neighbor,new_path,new_balance))
    # 如果没有找到路径，返回空列表
    return path_bal[-1]
def queuepop(queue):
    tmp_token,tmp_path,tmp_balance=queue[0]
    for i in range(len(queue)-1):
        queue[i]=queue[i+1]
    queue.pop()
    return tmp_token,tmp_path,tmp_balance

def countbl(from_token,to_token,value):
    p=0.997
    for i in liquidity.keys():
        if from_token in i and to_token in i:
            if from_token==i[0]:
                a,b=liquidity[i]
            else:
                b,a=liquidity[i]
            new_b=((value/a)*p)/(1+(value/a)*p)*b
            return new_b
        
# end_path,end_balance=bfs(graph,'tokenB','tokenB')
end_path,end_balance=bfs(graph,'tokenB','tokenB')
print("path: "+end_path[0],end='')

for i in end_path[1:]:
    print('->'+i,end='')
print(', tokenB balance=%f'%end_balance)

end_path,end_balance=opt_bfs(graph,'tokenB','tokenB')
print("opt_path: "+end_path[0],end='')

for i in end_path[1:]:
    print('->'+i,end='')
print(', opt_tokenB balance=%f'%end_balance)


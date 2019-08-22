#coding:utf-8
friends_lists = ['one','two','three']
print('tonight,will come {0} cunstomers,they are {1},{2},{3},but {3} not come'.format(len(friends_lists),friends_lists[0],friends_lists[1],friends_lists[2]))
friends_lists[2]='four'
print('now is exactly new list,they are is {},{},{}'.format(friends_lists[0],friends_lists[1],friends_lists[2]))

friends_lists.insert(0,'five')
friends_lists.append('six')
friends_lists.append('seven')
print('i find another table will contians another 3 peoples,now all the peoples are {}'.format(friends_lists))

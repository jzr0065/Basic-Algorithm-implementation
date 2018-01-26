# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 21:57:04 2017

apriori implementation 
@author: rjx
"""
import operator


#initial the fre_sets and records sets
def First_time(samples,new_dic,fre_list,min_support):
    #initial the records sets
    for i in range(len(samples)):
        for j in samples[i]:
            if j not in new_dic:
                fre_list.append(j)
                new_dic[j] = 1
            else:
                new_dic[j] +=1
    for x in fre_list:
        if new_dic[x] < min_support:
            del new_dic[x]
            fre_list.remove(x)
    fre_list.sort()
    print("The fre list are:")
    print(fre_list)
    print("The fre records are")
    dic_sorted = sorted(new_dic.items(), key = operator.itemgetter(0))
    print(dic_sorted)
    return (new_dic,fre_list)

def get_candidate(fre_list):
    candidates = list()
    for i in fre_list:
        for j in fre_list:
            if i == j:
                continue
            if(has_samesubset(i,j) == True):
                #do the join operation
                curitem = i + ',' + j
                curitem = curitem.split(',')
                curitem = list(set(curitem))
                curitem.sort()
                curitem = ','.join(curitem)
            else:
                continue
            if(already_contains(curitem,candidates) == True):
                #append the j to the candidates
                candidates.append(curitem)
    return candidates
    
def has_samesubset(str_1,str_2):
    same = 0
    split_1 = str_1.split(',')
    split_2 = str_2.split(',')
    for item in split_1:
        if(item in split_2):
            same = same + 1
    if(same == (len(split_1)-1)):
        return True
    else:
        return False

def already_contains(item,candidates):
    if(item in candidates):
        return False
    else:
        return True
    
def calculate_support(candidates,samples):
    dic = dict()
    for candidate in candidates:
        if(candidate not in dic):
            dic[candidate] = 0
        for sample in samples:
            ok = 1
            tem = candidate.split(',')
            for item in tem:
                if (item not in sample):
                    ok = 0
            if (ok == 1 ):
                if candidate not in dic:
                    dic[candidate] = 1
                else:
                    dic[candidate] += 1
    print("the dic is :")
    print(dic)
    return dic
    
#after pruning ,check the candidates sets,if empty,    
def pruning(dic,fre_list,min_support):
    new_list = list()
    for item in fre_list:
        if  dic.get(item) < min_support:
            del dic[item]
        else:
            new_list.append(item)
    print("after pruning,the dic is:")
    print(dic)
    print("after pruning,the fre_list is:")
    print(new_list)
    if(len(new_list) == 0):
        return (False,dic,new_list)
    else:
        return(True,dic,new_list)


def Apriori():
    samples = [  
    ["I1","I2","I5"],  
    ["I2","I4"],  
    ["I2","I3"],  
    ["I1","I2","I4"],  
    ["I1","I3"],  
    ["I2","I3"],  
    ["I1","I3"],  
    ["I1","I2","I3","I5"],  
    ["I1","I2","I3"]]
    stop = True
    min_support = 2
    min_confidence = 0.6
    fre_list = list()
    new_dic = dict()
    new_dic,fre_list = First_time(samples,new_dic,fre_list,min_support)
    final_list = list()
    while(stop == True):
        fre_list = get_candidate(fre_list)
        new_dic = calculate_support(fre_list,samples)
        stop,new_dic,fre_list = pruning(new_dic,fre_list,min_support)
        if (stop == True):
            final_list = fre_list[:]
    print("The final_list is:")
    print(final_list)        

Apriori()






# -*- coding: utf-8 -*-
"""
Created on Sat May 16 21:43:31 2020

@author: Tsai Jessica
"""

import json
import linkageCreat as sdg_link

def check_group(sdg):
    if len(sdg) == 3:
        return int(sdg[0])
    else:
        try:
            return int(sdg[0]+sdg[1])
        except:
            return int(sdg[0])


# 處理nodes
def find_nodes(sdg_target, varList):
    nodes = []  # 存放每個target的子nodes
    subNode = {}
    subNode['id'] = sdg_target
    subNode['group'] = 0
    subNode['goal'] = check_group(sdg_target)
    nodes.append(subNode)
    for i in range(len(varList)):
        subNode = {}
        subNode['id'] = str(varList[i])
        subNode['group'] = 1
        subNode['goal'] = check_group(varList[i])
        nodes.append(subNode)
		
    return nodes

# 處理links
def find_links(sdg_target, varList, valueList, attrib):
    links = []  # 存放每個target的子links
    for i in range(len(varList)):
        subLink = {}  # 暫時存放每組links
        if attrib == "cause":
            subLink['source'] = sdg_target
            subLink['target'] = str(varList[i])
            subLink['value'] = valueList[i]
            if float(valueList[i]) > 0:
                subLink['relation'] = 1  # 正關係為1
            elif float(valueList[i]) < 0 and float(valueList[i]) != -100:
                subLink['relation'] = 2  # 負關係為2
            else:
                subLink['relation'] = 0  # 無關係為0

        elif attrib == "use":
            subLink['source'] = str(varList[i])
            subLink['target'] = sdg_target
            subLink['value'] = valueList[i]
            if float(valueList[i]) > 0:
                subLink['relation'] = 1  # 正關係為1
            elif float(valueList[i]) < 0 and float(valueList[i]) != -100:
                subLink['relation'] = 2  # 負關係為2
            else:
                subLink['relation'] = 0  # 無關係為0

        links.append(subLink)

    return links


finalData_use = {}  # 匯出的json檔
finalData_cause = {}
finalData_cause["factors_cause"] = []
finalData_use["factors_use"] = []

sdg_target = ['1.1','1.2','1.3','1.4','1.5','1.a','1.b','2.1','2.2','2.3','2.4','2.5','2.a','2.b','2.c','3.1','3.2','3.3','3.4','3.5','3.6','3.7','3.8','3.9','3.a','3.b','3.c','3.d','4.1','4.2','4.3','4.4','4.5','4.6','4.7','4.a','4.b','4.c','5.1','5.2','5.3','5.4','5.5','5.6','5.a','5.b','5.c','6.1','6.2','6.3','6.4','6.5','6.6','6.a','6.b','7.1','7.2','7.3','7.a','7.b','8.1','8.2','8.3','8.4','8.5','8.6','8.7','8.8','8.9','8.10','8.a','8.b','9.1','9.2','9.3','9.4','9.5','9.a','9.b','9.c','10.1','10.2','10.3','10.4','10.5','10.6','10.7','10.a','10.b','10.c','11.1','11.2','11.3','11.4','11.5','11.6','11.7','11.a','11.b','11.c','12.1','12.2','12.3','12.4','12.5','12.6','12.7','12.8','12.a','12.b','12.c','13.1','13.2','13.3','13.a','13.b','14.1','14.2','14.3','14.4','14.5','14.6','14.7','14.a','14.b','14.c','15.1','15.2','15.3','15.4','15.5','15.6','15.7','15.8','15.9','15.a','15.b','15.c','16.1','16.2','16.3','16.4','16.5','16.6','16.7','16.8','16.9','16.10','16.a','16.b','17.1','17.2','17.3','17.4','17.5','17.6','17.7','17.8','17.9','17.10','17.11','17.12','17.13','17.14','17.15','17.16','17.17','17.18','17.19']
for i in range(len(sdg_target)):
    
    attrib = 4  # 4：cause variable, 5：use variable
    subData = {}
    factor = sdg_target[i]
    
    a = sdg_link.get_varattrib(factor, attrib)
    
    subData["sdg_target"] = factor
    subData["nodes"] = find_nodes(factor, a[0])
    subData["links"] = find_links(factor, a[0], a[1], "cause")
    
    finalData_cause["factors_cause"].append(subData)
    #if i == 0:
    #    print(len(subData["nodes"]))
    #    print(len(subData["links"]))
    
    attrib = 5  # 4：cause variable, 5：use variable
    subData = {}
    factor = sdg_target[i]
    
    a = sdg_link.get_varattrib(factor, attrib)
    
    subData["sdg_target"] = factor
    subData["nodes"] = find_nodes(factor, a[0])
    subData["links"] = find_links(factor, a[0], a[1], "use")
    
    finalData_use["factors_use"].append(subData)
    #if i == 0:
    #    print(len(subData["nodes"]))
    #    print(len(subData["links"]))
    print(i)


with open('finalData_cause.json', 'w') as outfile:
    json.dump(finalData_cause, outfile)


with open('finalData_use.json', 'w') as outfile:
    json.dump(finalData_use, outfile)
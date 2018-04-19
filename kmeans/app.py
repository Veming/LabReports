from numpy import *
import xlrd

__name__ = '__main__'

def kMeans(dataList, k):
    # 结果集
    resultList = []
    # k 的值至少大于等于 2
    if k < 2 :
        return 'error'
    
    # 获取表格中的行列数
    nrows = len(dataList)
    ncols = len(dataList[0])
    # 随机选取初始点为 质心 ，放入 质心列表 与 结果集 当中
    centroidList = []
    for i in range(0, k):
        dataID = random.randint(1,nrows-1)
        # print(i)
        # print(dataID)
        result = [dataID]
        resultList.append(result)
       
        centroidList.append(dataList[dataID][1:])
        dataList[dataID].append('Visited')
    # print(resultList)
    # for cpoint in centroidList:
    #     print(cpoint)

    # 遍历列表中的没一个点
    for i in range(1, nrows):
        if dataList[i][-1] == 'Visited':
            continue
        else:
            dataList[i].append('Visited')
        
        minDistence = getEuclideanDistance(dataList[i][1:-1],centroidList[0],ncols-1)
        cid = 0
        # 获取与该点距离最近的质心
        # print(len(centroidList))
        for j in range(1,k):
            distence = getEuclideanDistance(dataList[i][1:-1],centroidList[j],ncols-1)
            if distence < minDistence:
                minDistence = distence
                cid = j
            pass
        # print(resultList[cid][1:-1])
        # 向聚类中添加新的点
        resultList[cid].append(i)
        # print(resultList[cid])
        # 更新质心质心 
        centroidList[cid] = getCentroid(dataList,resultList[cid], ncols-1)
    return resultList    



# 计算聚类质心 
def getCentroid(dataList, pidList, n):
    centroid = []
    pList =[]
    for pid in pidList:
        pList.append(dataList[pid][1:-1])
    for i in range(0, n):
        centroid.append(0)
    for p in pList:
        for i in range(0,len(p)):
            centroid[i] += p[i]
    # print(pList)
    pListNbr = len(pList)
    for i in range(0, len(centroid)):
        centroid[i] /= pListNbr
    return centroid


# 计算两个点之间的欧式距离
def getEuclideanDistance(p, q, n):
    result = 0
    # print("n:",n)
    # print("p:",p,"\tq:",q)
    for i in range(0, n):
        # print("i:",i,"\tp:",p[i],"\tq:",q[i])
        result += round(pow(p[i]-q[i], 2),4)
        # print("result:",result)
    return pow(result,0.5)

# 导入实验数据与Datalist列表中
def importData(filePath):
    workbook = xlrd.open_workbook(filePath)
    table = workbook.sheet_by_index(0)
    nrows = table.nrows
    # ncols = table.ncols
    dataList = []
    for i in range(0,nrows):
        dataList.append(table.row_values(i))
    return dataList


# util
def showData(dataList):
    for data in dataList:
        print(data)
# end_util

def main():
    dataList = importData('wine.xlsx')
    # dataList.pop(0)
    kDataList = kMeans(dataList, 3)

    showData(kDataList)
    

if __name__ == '__main__':
    main()

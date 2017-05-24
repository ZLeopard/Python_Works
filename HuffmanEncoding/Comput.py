#-*- coding: UTF-8 -*-

import docx
import matplotlib.pyplot as plt
import numpy as np

def ReadDocx(docName):
    FullText = []
    doc = docx.Document(docName)
    paras = doc.paragraphs  # Word文档的每个段落
    for p in paras:
        FullText.append(p.text)
    return ''.join(FullText)

def CalcProbability(content):
    Result = {}
    probability = {}
    chars_freqs = {}  # 排序后字符字典
    posba = {}          # 排序后概率字典

    for i in content:
        if i.isalpha():
            if i in Result.keys():
                Result[i] += 1
            else:
                Result[i] = 1
    total = sum(Result.values())
    for j in Result.keys():
        probability[j] = round(Result[j] / total, 5)

    temp_list1 = sorted(Result.items(), key=lambda d: d[0])
    for ss in temp_list1:
        chars_freqs[ss[0]] = ss[1]
    temp_list2 = sorted(probability.items(), key=lambda d: d[0])
    for ss in temp_list2:
        posba[ss[0]] = ss[1]  # 按照字母大小进行排序
    return chars_freqs, posba       # 输出频数和概率

def PaintPie(pro):  # pro为一个字典类型-{字符：概率}
    fig = plt.figure(1, figsize=(12, 6))
    p = []
    labels = []
    for ii in pro.keys():
        p.append(pro[ii])
        labels.append(ii)
    colors = ['pink', 'coral', 'yellow', 'orange','coral',]
    ax1 = fig.add_subplot(121)
    ax1.pie(p, colors=colors, labels=labels, autopct='%1.1f%%', pctdistance=0.8, shadow=True)
    ax1.set_title('The symbol in the Word', bbox={'facecolor': '0.8', 'pad': 5})

    width = 0.4
    ind = np.linspace(0.5, 50.5, len(pro))
    ax2 = fig.add_subplot(122)
    ax2.bar(ind - width / 2, p, width, color='coral')
    ax2.set_xticks(ind)
    ax2.set_xticklabels(labels)
    ax2.set_xlabel('Symbol')
    ax2.set_ylabel('Prosibility Of Symbol')
    plt.show()

if __name__ == '__main__':
    res = {}
    pro = {}
    ss = ReadDocx('test.docx')
    res, pro = CalcProbability(ss)
    PaintPie(pro)

    print(ss)
    print(res)
    print(pro)

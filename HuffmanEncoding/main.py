

from Huffman import *
from Comput import *
import xlwt

if __name__ == '__main__':
    ii = 0
    HX = 0              # 信源熵
    code_AveLength = 0  # 平均码长
    probability = {}
    chars_freqs = {}
    title = ['信源符号', '符号频数', '符号概率', '码长', '码字', '平均码长', '符号熵', '编码效率']
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('infor', cell_overwrite_ok=True)    # 创建excel工作空间
    for index in range(len(title)):
        sheet.write(0, index, title[index])   # 写入excel标题

    content = ReadDocx('test.docx')     # 读入docx的内容
    chars_freqs, probability = CalcProbability(content)   # 统计字符个数和概率
    PaintPie(probability)
    print(chars_freqs)                # 这样数据就可以按照字母顺序输出

    # Huffman Encoding Process
    nodes = CreateNodes([chars_freqs[i] for i in chars_freqs.keys()])
    root = CreateHuffmanTree(nodes)
    codes = HuffmanEncoding(nodes, root)

    f = lambda y: abs(y*(math.log2(y)))  # 构造函数-Pi * log2(Pi)
    for tt in probability.keys():
        HX += f(probability[tt])          # 计算信源熵
        code_AveLength += probability[tt]*len(codes[ii])   # 计算平均码长
        ii += 1
    efficiency = HX/code_AveLength       # 计算Huffman编码效率

    print(probability)
    print('Huffman Encoding Efficiency is %.2f' % efficiency)
    ii = 0
    for item in chars_freqs.keys():
        print('Character:%s   freq:%-2d   encoding: %s' % (item, chars_freqs[item], codes[ii]))
        ii += 1                          # 输出Huffman编码后码字
    ii = 1        # 数据从第一行，第零列开始
    index = 0
    for tt in probability.keys():
        sheet.write(ii, index, tt)
        sheet.write(ii, index+1, chars_freqs[tt])
        sheet.write(ii, index+2, probability[tt])
        sheet.write(ii, index+3, len(codes[ii-1]))
        sheet.write(ii, index+4, codes[ii-1])
        ii += 1                   # 将数据按照字符顺序输出
    sheet.write(1, 5, code_AveLength)         # 输出平均码长
    sheet.write(1, 6, HX)                     # 输出信源熵
    sheet.write(1, 7, round(efficiency, 2))   # 输出编码效率
    book.save(r'D:\User\lenovo\Desktop\information\encode\test.xls')  # 保存文件


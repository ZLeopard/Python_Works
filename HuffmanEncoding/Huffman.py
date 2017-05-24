# Huffman Encoding

import math

class Node:
    def __init__(self, freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq

    def Is_Left(self):
        return self.father.left == self

def CreateNodes(freqs):
    return [Node(freq) for freq in freqs]

def CreateHuffmanTree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda nodes: nodes.freq)  # 按概率大小排序
        node_left = queue.pop(0)
        node_right = queue.pop(0)        # 删除要结合的两结点
        node_father = Node(node_left.freq + node_right.freq)
        node_father.right = node_right
        node_father.left = node_left
        node_right.father = node_father
        node_left.father = node_father    # 建立每个结点的逻辑关系
        queue.append(node_father)         # 添加结合后的新结点
    queue[0].father = None
    return queue[0]


def HuffmanEncoding(nodes, root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        temp_node = nodes[i]
        while temp_node != root:         # 从叶结点遍历到根结点
            if temp_node.Is_Left():      # 判断是否为左儿子
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            temp_node = temp_node.father
    return codes


if __name__ == '__main__':
    ii = 0
    chars_freqs = {'I': 2, 'l': 1, 'o': 7, 'v': 1}
    nodes = CreateNodes([chars_freqs[i] for i in chars_freqs.keys()])
    root = CreateHuffmanTree(nodes)
    codes = HuffmanEncoding(nodes, root)
    code_AveLength = len("".join(codes)) / len(codes)
    print(math.log2(8))
    for item in chars_freqs.keys():
        print('Character:%s freq:%-2d   encoding: %s' % (item, chars_freqs[item], codes[ii]))
        ii += 1
    print(code_AveLength)

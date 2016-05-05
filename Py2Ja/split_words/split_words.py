#!/usr/bin/python
# -*- coding: utf-8 -*-
import jieba
import re

chinese_pattern = re.compile(u"[0-9]|[A-Za-z]|[\u4e00-\u9fa5]|[ ]")


def remove_symbols(input_sentence):
    return chinese_pattern.findall(input_sentence, re.S)


def split_words(input_sentence, ws_dict):
    result = "".join(input_sentence).encode("utf-8").lower()
    seg_list = jieba.cut(result)

    for seg in seg_list:
        if seg not in ws_dict:
            ws_dict[seg] = 1
        else:
            ws_dict[seg] += 1
    return ws_dict

if __name__ == '__main__':

    import time

    segment_list = []
    words_dict = {}

    with open("postfile_backup.txt", "r") as fp:
        t1 = time.time()
        for line in fp.readlines():
            sentence = remove_symbols(line.decode("utf-8"))
            words_dict = split_words(sentence, words_dict)
        fp.close()
        t2 = time.time()
        tm_cost = t2-t1
        print tm_cost

    words_list = sorted(words_dict.iteritems(), key=lambda d: d[1], reverse=True)
    for j in words_list:
        print j[0].encode("utf-8")+": %d" % j[1]

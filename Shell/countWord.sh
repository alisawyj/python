#!/bin/bash
#对一个txt文件进行单词统计，并按从高到底的顺序排列输出到out.txt中
awk -F'[,. ]' '{for(i=1;i<=NF;i++)a[$i]++} END{for(j in a)print j,"\t",a[j]}' /d/code_test/countWord/test.txt | sort -nrk 2 >>/d/code_test/countWord/out.txt



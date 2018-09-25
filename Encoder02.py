#! /usr/bin/env python3
# -*- coding: utf-8 -*-

line_num = 0
import re
with open('result01.txt') as f:
    text = []
    lines = ["", "", "", ""]
    while True:
        s_line = f.readline()
        if not s_line:
            if line_num == 1:
                text.append(lines[0] + '[lc]\n')
            if line_num == 2:
                if re.search('。{1}|？{1}|！{1}', lines[0]):
                    text.append(lines[0][:-1] + '[lr]\n')
                else:
                    text.append(lines[0][:-1] + '[r]\n')
                text.append(lines[1] + '[lc]\n')
            if line_num == 3:
                if re.search('。{1}|？{1}|！{1}', lines[0]):
                    text.append(lines[0][:-1] + '[lr]\n')
                else:
                    text.append(lines[0][:-1] + '[r]\n')
                if re.search('。{1}|？{1}|！{1}', lines[1]):
                    text.append(lines[1][:-1] + '[lr]\n')
                else:
                    text.append(lines[1][:-1] + '[r]\n')
                text.append(lines[2] + '[lc]\n')
            text.append(s_line)

            break

        if s_line.find('[{1}.*?]{1}|〔{1}.*?〕{1}|〈{1}.*?〉{1}|#{1}') == -1 and re.search(r'[ぁ-ん]', s_line):
            lines[line_num] = s_line
            line_num += 1
            if line_num > 2:
                if line_num == 1:
                    text.append(lines[0][:-1] + '[lc]\n')
                if line_num == 2:
                    if re.search('。{1}|？{1}|！{1}', lines[0]):
                        text.append(lines[0][:-1] + '[lr]\n')
                    else:
                        text.append(lines[0][:-1] + '[r]\n')
                    text.append(lines[1][:-1] + '[lc]\n')
                if line_num == 3:
                    if re.search('。{1}|？{1}|！{1}', lines[0]):
                        text.append(lines[0][:-1] + '[lr]\n')
                else:
                    text.append(lines[0][:-1] + '[r]\n')
                    if re.search('。{1}|？{1}|！{1}', lines[1]):
                        text.append(lines[1][:-1] + '[lr]\n')
                    else:
                        text.append(lines[1][:-1] + '[r]\n')
                    text.append(lines[2][:-1] + '[lc]\n')

                line_num = 0
                lines = ["", "", "", ""]
        else:
            if line_num == 1:
                text.append(lines[0][:-1] + '[lc]\n')
            if line_num == 2:
                if re.search('。{1}|？{1}|！{1}', lines[0]):
                    text.append(lines[0][:-1] + '[lr]\n')
                else:
                    text.append(lines[0][:-1] + '[r]\n')
                text.append(lines[1][:-1] + '[lc]\n')
            if line_num == 3:
                if re.search('。{1}|？{1}|！{1}', lines[0]):
                    text.append(lines[0][:-1] + '[lr]\n')
                else:
                    text.append(lines[0][:-1] + '[r]\n')
                if re.search('。{1}|？{1}|！{1}', lines[1]):
                    text.append(lines[1][:-1] + '[lr]\n')
                else:
                    text.append(lines[1][:-1] + '[r]\n')
                text.append(lines[2][:-1] + '[lc]\n')

            line_num = 0
            lines = ["", "", "", ""]

            text.append(s_line)

    
with open('result02.txt', "w", encoding="utf-8") as f:
    f.writelines(text)
# coding=utf-8
import os, re
from simple_tradition import *

baseDir = r'D:\Code\Caracal\报告重做-AllInOne-Caracal-project-2017-04-17-转繁体'.decode('utf-8')
re_file = re.compile(r'\w+.resx')
re_head = re.compile(r'^[rR]es')
re_content_res = re.compile(r'\s*<data name=\"[\w\_]+\" xml:space=\"preserve\"\s*')
re_content_frm = re.compile(r'\s*<data name=\"[a-zA-Z\_$][0-9a-zA-Z\_]*.(Text|Tooltip)\" xml:space=\"preserve\"\s*')
re_filecsproj = re.compile(r'\w+.csproj')
re_content_csproj_start = re.compile(r'(\s*<EmbeddedResource Include=\"[\w\\]+)(.resx\">\s*)')
re_content_csproj_end = re.compile(r'\s*</EmbeddedResource>\s*')

if os.path.isdir(baseDir):
    for parent, dirnames, filenames in os.walk(baseDir):
        for file in filenames:
            if re_file.match(file) and 'DataBase' not in parent:
                fullname = os.path.join(parent, file)
                shortname, extension = os.path.splitext(file)
                fullnamenew = os.path.join(parent, shortname + '.zh-TW' + extension)

                if re_head.match(file):
                    # 自定义的资源文件
                    with open(fullname, 'r') as fread, open(fullnamenew, 'w') as fwrite:
                        find = False
                        for line in fread.readlines():
                            if find:
                                fwrite.write(simple2tradition(line))
                                find = False
                            else:
                                # if '<data name="' in line and 'xml:space="preserve">' in line:
                                if re_content_res.match(line):
                                    find = True
                                fwrite.write(line)
                else:
                    # 窗体或控件的资源文件
                    with open(fullname, 'r') as fread, open(fullnamenew, 'w') as fwrite:
                        find = False
                        for line in fread.readlines():
                            if find:
                                fwrite.write(simple2tradition(line))
                                find = False
                            else:
                                if re_content_frm.match(line):
                                    find = True
                                fwrite.write(line)

            if re_filecsproj.match(file) and 'DataBase' not in parent:
                fullname = os.path.join(parent, file)
                data = []
                with open(fullname, 'r') as fread:
                    find = False
                    L = []
                    for line in fread.readlines():
                        data.append(line)
                        if find:
                            L.append(line)
                            if re_content_csproj_end.match(line):
                                find = False
                                data.extend(L)
                                L = []
                        else:
                            r = re_content_csproj_start.match(line)
                            if r:
                                L.append(r.group(1) + '.zh-TW' + r.group(2))
                                find = True

                if len(data) > 0:
                    with open(fullname, 'w') as fwrite:
                        fwrite.writelines(data)

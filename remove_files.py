# coding=utf-8
import os, re, shutil

sourceDir = r'D:\Code\Caracal\报告重做-AllInOne-Caracal-project-2017-04-10'.decode('utf-8')
desDir = r'D:\Code\Caracal\报告重做-AllInOne-Caracal-project-2017-04-17-转繁体'.decode('utf-8')
re_filecsproj = re.compile(r'\w+.csproj')

for parent, dirnames, filenames in os.walk(sourceDir):
    for file in filenames:
        if re_filecsproj.match(file) and 'DataBase' not in parent:
            sourcename = os.path.join(parent, file)
            desname = os.path.join(parent.replace(u'04-10', u'04-17-转繁体'), file)
            shutil.copyfile(sourcename, desname)
            print sourcename
            print desname
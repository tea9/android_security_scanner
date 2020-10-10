#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import subprocess
import os
import shutil

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

"""
1.apktool反编译
2.执行命令
"""

def func_unpack(apkPath, filename):
    if apkPath == "":
        return
    cmd = "java -jar apktool.jar -f d "+apkPath
    if filename != "":
        cmd = cmd + " -o " +filename
    return func_run_cmd(cmd)

def func_run_cmd(cmd):
    print("-----------------------------------------")
    print(cmd);
    print("-----------------------------------------")

    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    returncode = p.poll()
    result = p.stdout.read()
    p.wait()
    p.stdout.close()
    #result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
   # while returncode is None:
    #    line = p.stdout.readline()
     #   returncode = p.poll()
      #  line = line.strip()
       # print(line)

    # print(returncode)

    return {'code':0,'result':result,'cmd':cmd}
def adb_shell(cmd):
     result = subprocess.getstatusoutput(cmd)
     return result

def invoke_apk_static(apk_path):
    """
    一、资源文件中的Apk文件
    1.apktool 反编译
    2.进入assets文件夹
    3.查询.apk文件 find . -name "*.apk"
    二、动态注册 Receiver风险
    1.apktool 反编译
    2.进入smail目录全局搜索 registerReceiver
    grep -R --include="*.smali" registerReceiver .
    三、明文数字证书风险
    1.apktool 反编译
    2.进入assets文件夹
    查找文件名为cer后缀名
    find . -name "*.cer"
    """
    func_run_cmd('cd ' + apk_path)
    result = func_run_cmd('find . -name "*.apk"')
    print(result)
    print("1.-------------------")
    result = func_run_cmd('grep -R --include="*.smali" registerReceiver .')
    print(result)
    print("2.-------------------")
    result = func_run_cmd('find . -name "*.cer"')
    print(result)
    print("3.-------------------")
    result = func_run_cmd('grep -R --include="*.js" innerHTML .')
    print(result)
    result = func_run_cmd('grep -R --include="*.html" innerHTML .')
    print(result)
    print("-------------------")


def a(argv=None):
    if argv is None:
        argv = sys.argv
    print('参数个数为:', len(sys.argv), '个参数。')
    print('参数列表:', str(sys.argv))
    filePath = argv[1]

    print("aaa")
def main():
    print("main")
    invoke_apk_static('old')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # apk()
    # adb_shell('find . -name "*.apk"')
    #cmd = 'adb shell dumpsys activity | grep "Run #"'
    #print(adb_shell('find . -name "*.apk"'))
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

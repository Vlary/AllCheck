#!/usr/bin/python

import os
import zstandard

cctx = zstandard.ZstdCompressor(level=10)

# 密码复杂度核查
def passcomp():
    rl = os.popen('cat /etc/login.defs').read()
    return rl

# 登陆失败处理和登陆超时
def loginf():
    rl = os.popen("cat /etc/pam.d/system-auth").read()
    return rl

def writezck(f, content):
    with cctx.stream_writer(f) as compressor: 
        compressor.write(content.encode())

def linuxstart():
    with open('linux.zck', 'wb') as f:
        writezck(f, passcomp() + loginf())
        f.close()

<!--
 * @Author: matiastang
 * @Date: 2022-07-26 16:54:07
 * @LastEditors: matiastang
 * @LastEditTime: 2022-07-26 17:27:50
 * @FilePath: /matias-python/md/wget.md
 * @Description: wget
-->
# wget

[wget](https://baijiahao.baidu.com/s?id=1714300855200071381&wfr=spider&for=pc)

wget 是一个从网络上自动下载文件的自由工具，支持通过 HTTP、HTTPS、FTP 三个最常见的 TCP/IP协议 下载，并可以使用 HTTP 代理。"wget" 这个名称来源于 “World Wide Web” 与 “get” 的结合。
所谓自动下载，是指 wget 可以在用户退出系统的之后在继续后台执行，直到下载任务完成。

## 安装

```
$ brew install wget
brew install wget 
Error: Cannot install under Rosetta 2 in ARM default prefix (/opt/homebrew)!
To rerun under ARM use:
    arch -arm64 brew install ...
To install under x86_64, install Homebrew into /usr/local.
```
```
$ arch -arm64 brew install wget
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles//libunistring-1.0.arm64_big_sur.bottle.tar.gz
######################################################################## 100.0%
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles//libidn2-2.3.3.arm64_big_sur.bottle.tar.gz
######################################################################## 100.0%
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles//ca-certificates-2022-07-19_1.all.bottle.tar.gz
######################################################################## 100.0%
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles//openssl%401.1-1.1.1q.arm64_big_sur.bottle.tar.gz
######################################################################## 100.0%
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles//wget-1.21.3.arm64_big_sur.bottle.tar.gz
######################################################################## 100.0%
==> Installing dependencies for wget: libunistring, libidn2, ca-certificates and openssl@1.1
==> Installing wget dependency: libunistring
==> Pouring libunistring-1.0.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libunistring/1.0: 56 files, 4.8MB
==> Installing wget dependency: libidn2
==> Pouring libidn2-2.3.3.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libidn2/2.3.3: 78 files, 1MB
==> Installing wget dependency: ca-certificates
==> Pouring ca-certificates-2022-07-19_1.all.bottle.tar.gz
==> Regenerating CA certificate bundle from keychain, this may take a while...
🍺  /opt/homebrew/Cellar/ca-certificates/2022-07-19_1: 3 files, 222.5KB
==> Installing wget dependency: openssl@1.1
==> Pouring openssl@1.1-1.1.1q.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/openssl@1.1/1.1.1q: 8,097 files, 18MB
==> Installing wget
==> Pouring wget-1.21.3.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/wget/1.21.3: 89 files, 4.2MB
==> `brew cleanup` has not been run in the last 30 days, running now...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
Removing: /Users/matias/Library/Caches/Homebrew/brotli--1.0.9.arm64_big_sur.bottle.tar.gz... (988.7KB)
Removing: /Users/matias/Library/Caches/Homebrew/c-ares--1.17.2.arm64_big_sur.bottle.tar.gz... (156.8KB)
Removing: /Users/matias/Library/Caches/Homebrew/ca-certificates--2021-09-30... (114.6KB)
Removing: /Users/matias/Library/Caches/Homebrew/gdbm--1.20.arm64_big_sur.bottle.tar.gz... (222.3KB)
Removing: /Users/matias/Library/Caches/Homebrew/icu4c--69.1.arm64_big_sur.bottle.tar.gz... (27.4MB)
Removing: /Users/matias/Library/Caches/Homebrew/jemalloc--5.2.1_1.arm64_big_sur.bottle.tar.gz... (681.7KB)
Removing: /Users/matias/Library/Caches/Homebrew/libev--4.33.arm64_big_sur.bottle.tar.gz... (148.0KB)
Removing: /Users/matias/Library/Caches/Homebrew/libidn2--2.3.2... (257.3KB)
Removing: /Users/matias/Library/Caches/Homebrew/libunistring--0.9.10... (1.4MB)
Removing: /Users/matias/Library/Caches/Homebrew/libuv--1.42.0.arm64_big_sur.bottle.tar.gz... (1.3MB)
Removing: /Users/matias/Library/Caches/Homebrew/mpdecimal--2.5.1.arm64_big_sur.bottle.tar.gz... (544.0KB)
Removing: /Users/matias/Library/Caches/Homebrew/mysql@5.7--5.7.35.arm64_big_sur.bottle.1.tar.gz... (70.9MB)
Removing: /Users/matias/Library/Caches/Homebrew/n--7.3.1.arm64_big_sur.bottle.tar.gz... (21.8KB)
Removing: /Users/matias/Library/Caches/Homebrew/nghttp2--1.44.0.arm64_big_sur.bottle.tar.gz... (938.5KB)
Removing: /Users/matias/Library/Caches/Homebrew/node--16.9.1.arm64_big_sur.bottle.tar.gz... (12.6MB)
Removing: /opt/homebrew/Cellar/openssl@1.1/1.1.1l... (8,073 files, 18MB)
Removing: /Users/matias/Library/Caches/Homebrew/openssl@1.1--1.1.1l_1... (5MB)
Removing: /Users/matias/Library/Caches/Homebrew/openssl@1.1--1.1.1l.arm64_big_sur.bottle.tar.gz... (5MB)
Removing: /Users/matias/Library/Caches/Homebrew/pipx--0.16.4.arm64_big_sur.bottle.tar.gz... (261.1KB)
Removing: /Users/matias/Library/Caches/Homebrew/pnpm--6.15.1.arm64_big_sur.bottle.tar.gz... (2.2MB)
Removing: /Users/matias/Library/Caches/Homebrew/python@3.9--3.9.7.arm64_big_sur.bottle.tar.gz... (13.6MB)
Removing: /Users/matias/Library/Caches/Homebrew/readline--8.1.arm64_big_sur.bottle.tar.gz... (559.2KB)
Removing: /Users/matias/Library/Caches/Homebrew/sqlite--3.36.0.arm64_big_sur.bottle.tar.gz... (1.9MB)
Removing: /Users/matias/Library/Caches/Homebrew/telnet--63.arm64_big_sur.bottle.tar.gz... (52.7KB)
Removing: /Users/matias/Library/Caches/Homebrew/wget--1.21.2... (1.4MB)
Removing: /Users/matias/Library/Caches/Homebrew/xz--5.2.5.arm64_big_sur.bottle.tar.gz... (416.9KB)
Removing: /Users/matias/Library/Caches/Homebrew/yarn--1.22.11.all.bottle.tar.gz... (1.2MB)
Removing: /Users/matias/Library/Caches/Homebrew/python@3.9_bottle_manifest--3.9.6... (15.4KB)
Removing: /Users/matias/Library/Caches/Homebrew/go_bottle_manifest--1.16.6... (5.9KB)
Removing: /Users/matias/Library/Logs/Homebrew/go... (64B)
Removing: /Users/matias/Library/Logs/Homebrew/gdbm... (64B)
Removing: /Users/matias/Library/Logs/Homebrew/mpdecimal... (64B)
Removing: /Users/matias/Library/Logs/Homebrew/pipx... (64B)
Removing: /Users/matias/Library/Logs/Homebrew/readline... (64B)
Removing: /Users/matias/Library/Logs/Homebrew/sqlite... (64B)
Removing: /Users/matias/Library/Logs/Homebrew/xz... (64B)
Removing: /Users/matias/Library/Logs/Homebrew/mysql@5.7... (1.6KB)
Removing: /Users/matias/Library/Logs/Homebrew/telnet... (64B)
Removing: /Users/matias/Library/Logs/Homebrew/python@3.9... (2 files, 2.5KB)
Pruned 0 symbolic links and 2 directories from /opt/homebrew
```
下载`python`版本到`~/.pyenv/cache/`
```
wget http://mirrors.sohu.com/python/3.10.5/Python-3.10.5.tar.xz -P ~/.pyenv/cache/
--2022-07-26 17:24:51--  http://mirrors.sohu.com/python/3.10.5/Python-3.10.5.tar.xz
正在解析主机 mirrors.sohu.com (mirrors.sohu.com)... 123.125.123.141
正在连接 mirrors.sohu.com (mirrors.sohu.com)|123.125.123.141|:80... 已连接。
已发出 HTTP 请求，正在等待回应... 403 Forbidden
2022-07-26 17:24:51 错误 403：Forbidden。
```
[查看python的版本](https://mirrors.sohu.com/)
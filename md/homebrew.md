<!--
 * @Author: matiastang
 * @Date: 2022-07-26 17:00:42
 * @LastEditors: matiastang
 * @LastEditTime: 2022-07-26 17:32:30
 * @FilePath: /matias-python/md/homebrew.md
 * @Description: homebrew
-->
# homebrew

[homebrew文档](http://mirrors.ustc.edu.cn/help/homebrew-bottles.html)
[镜像](http://mirrors.ustc.edu.cn/help/homebrew-bottles.html)

## 报错

```
$ brew install wget
Error: Cannot install under Rosetta 2 in ARM default prefix (/opt/homebrew)!
To rerun under ARM use:
    arch -arm64 brew install ...
To install under x86_64, install Homebrew into /usr/local.
```

则使用如下安装
```
$ arch -arm64 brew install wget
Updating Homebrew...
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles//bottles-portable-ruby/portable-ruby-2.6.8_1.arm64_big_sur.bottle.tar.gz
########################################################################################################################### 100.0%
==> Pouring portable-ruby-2.6.8_1.arm64_big_sur.bottle.tar.gz
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles//libunistring-0.9.10.arm64_big_sur.bottle.tar.gz
#=#=#    
这里报错，没有下载下来                                                                     
curl: (22) The requested URL returned error: 404 
Warning: Bottle missing, falling back to the default domain...
==> Downloading https://ghcr.io/v2/homebrew/core/libunistring/manifests/0.9.10
Already downloaded: /Users/matias/Library/Caches/Homebrew/downloads/152db94f938ae80e8c2638e27ddd2a889c56c01b723d2512073f2f605771b406--libunistring-0.9.10.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/libunistring/blobs/sha256:73cc290ebcefd6354329317266d9e110e3a5967d0a8260d2cf7d4dd
Already downloaded: /Users/matias/Library/Caches/Homebrew/downloads/b68429257038e80dad7f5e906f26422d73b1a124cafb3a4f6d4d8aad2a96419c--libunistring--0.9.10.arm64_big_sur.bottle.tar.gz
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles//libidn2-2.3.2.arm64_big_sur.bottle.tar.gz
#=#=#                                                                         
curl: (22) The requested URL returned error: 404 
Warning: Bottle missing, falling back to the default domain...
==> Downloading https://ghcr.io/v2/homebrew/core/libidn2/manifests/2.3.2
Already downloaded: /Users/matias/Library/Caches/Homebrew/downloads/b8f2405de653b6eec7b67d66be89a8aa5babeb4a79fefd07d1998040d99b02cb--libidn2-2.3.2.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/libidn2/blobs/sha256:dbaac7e6e29ffa8c7c2b5e152fd6ee0118e547f90dc4b180c7f168c2f681
Already downloaded: /Users/matias/Library/Caches/Homebrew/downloads/0c864cdf0fdabf8f11a656adb96a68df4cc168dd5780c63dc91e3dca55c49fba--libidn2--2.3.2.arm64_big_sur.bottle.tar.gz
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles//ca-certificates-2021-09-30.all.bottle.1.tar.gz
#=#=#                                                                         
curl: (22) The requested URL returned error: 404 
Warning: Bottle missing, falling back to the default domain...
==> Downloading https://ghcr.io/v2/homebrew/core/ca-certificates/manifests/2021-09-30-1
Already downloaded: /Users/matias/Library/Caches/Homebrew/downloads/6dd04846039f56f603a1f00eb98dd3f8f8dd9246a06afb89958640ccbe83f5b6--ca-certificates-2021-09-30-1.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/ca-certificates/blobs/sha256:47c9cd6ec69dbbf8a3f697e6b07df409a573c779aa86ceadc7d9
Already downloaded: /Users/matias/Library/Caches/Homebrew/downloads/1f75a2a0c129e67e1492b5aded76ae26983f65488046276a2a8815f5abe564c2--ca-certificates--2021-09-30.all.bottle.1.tar.gz
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles//openssl%401.1-1.1.1l_1.arm64_big_sur.bottle.tar.gz
#=#=#                                                                         
curl: (22) The requested URL returned error: 404 
Warning: Bottle missing, falling back to the default domain...
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/1.1/manifests/1.1.1l_1
Already downloaded: /Users/matias/Library/Caches/Homebrew/downloads/2afc290b1f48dc850bc4c1ee70efde6f32fbc5d2437e1f72e659da2a9304fb17--openssl@1.1-1.1.1l_1.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/1.1/blobs/sha256:e3d8556cec907ad1e0ea00aebd0b0b516dde06ea3bf24308290ad785
Already downloaded: /Users/matias/Library/Caches/Homebrew/downloads/3172910d41ba89a8c61d2c0b211b6360645c2c885045fc5ff46304e5018437b0--openssl@1.1--1.1.1l_1.arm64_big_sur.bottle.tar.gz
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles//wget-1.21.2.arm64_big_sur.bottle.tar.gz
#=#=#                                                                         
curl: (22) The requested URL returned error: 404 
Warning: Bottle missing, falling back to the default domain...
==> Downloading https://ghcr.io/v2/homebrew/core/wget/manifests/1.21.2
Already downloaded: /Users/matias/Library/Caches/Homebrew/downloads/4f1bc54b93b7a55f2985ec8156562ecee5fe37bc720f3d3d11ba47f7c685cb58--wget-1.21.2.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/wget/blobs/sha256:4f8b66c5f181f01064522a80bfda72eabddd47299a8b88bc7d0022c457e7259
Already downloaded: /Users/matias/Library/Caches/Homebrew/downloads/8f69d6461070918e45127e7eba47b0e690e2d3cbb22d7f0590b8fc8dce9cbb1d--wget--1.21.2.arm64_big_sur.bottle.tar.gz
==> Installing dependencies for wget: libunistring, libidn2, ca-certificates and openssl@1.1
==> Installing wget dependency: libunistring
==> Pouring libunistring-0.9.10.arm64_big_sur.bottle.tar.gz
Error: No such file or directory @ rb_sysopen - /Users/matias/Library/Caches/Homebrew/downloads/30b9bd474869f1fad00ef30f12045a47cbbb4dabef98168f99d85d677c1b681f--libunistring-0.9.10.arm64_big_sur.bottle.tar.gz
```
先更新`homebrew`
```
$ brew update
```
再下载
```
arch -arm64 brew install wget
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

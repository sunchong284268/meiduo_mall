a = 1

b = 2


设置记住密码（默认15分钟）：
git config --global credential.helper cache
如果想自己设置时间，可以这样做(1小时后失效)：
git config credential.helper 'cache --timeout=3600'
长期存储密码：
git config --global credential.helper store

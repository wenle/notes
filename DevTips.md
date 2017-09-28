1. mac上查看端口被哪个程序占用
  lsof -i tcp:8087
2. git放弃本地未commit的修改  
  git checkout branch-name
3. git放弃本地已commit的修改
  git reset --hard ORIGIN/BRANCH 
4. git本地文件被误删除后，可以通过git checkout . 来恢复本目录下的文件
### 缓冲区 Buffer

nio的读写都需要通过buffer。

1. 底层实质是一个基本数据类型的array
2. 为了协调读写，有三个位置信息：capacity、limit、position

	- capacity为buffer的容量
	- limit在写模式等同capacity；读模式代表最多可以读取到多少数据，也就是之前已经写入了多少数据
	- position是当前读写的位置

3. 操作buffer的方法

	- flip 从写模式切换到读模式
	- rewind 重新读buffer中的所有数据
	- clear 重置，准备从头写入
	- compact 将未读数据copy到buffer开头，准备append写入
	- mark标记，reset将positon移到mark地点
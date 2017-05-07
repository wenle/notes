### JDK tour

### java

#### java.io

java.lang.AutoCloseable 在java1.7后可以通过try-with-resource语句来做自动资源回收。注意1）需要调用close回收的object需要在with中声明 2）close如果抛出异常，会覆盖业务异常，业务异常作为最终抛出异常的Suppressed异常。3）无幂等要求。

java.io.Closeable继承了java.lang.AutoCloseable，有幂等性要求，即重复执行无副作用。

java.io.InputStream/OutputStream是单向字节流的抽象，基类里只有基础的逐个字节读写的功能，以及包装的基于byte数组的读写功能。

java.io.Reader/Writer是单向字符流的抽象，java中定义的字符是16位unicode字符。

FilterInputStream/FilterOutputStream是在InputStream/OutputStream上做的包装。BufferedXX在此基础上增加了byte array缓冲功能，提供mark/reset功能。


### java.util.concurrent
原子操作： 
1）除long和double之外的基本类型的赋值操作
2）所有引用reference的赋值操作
3）java.concurrent.Atomic.* 包中所有类的一切操作。

比如++操作，其赋值依赖于读取原有的值，所以必须依靠Atomic库来实现原子自增。

实现上Atomic类依靠硬件提供的CAS（compare and swap）功能来实现原子更新。但可能有aba问题。AtomicStampedReference通过增加stamp解决aba问题。








### javax
## Groovy笔记

### 语法基础

1. Groovy与Java的关系
Groovy => OOP | Script lang

作为OOP语言，先将源代码编译成JVM字节码，需要和groovy lib一起打包才能在JVM上运行。

作为脚本语言，直接在命令行执行：groovy script.groovy；另外，可以在Java中通过脚本引擎来执行groovy脚本

Groovy语法兼容大部分Java语法

2. 字符串

GString实现了java的CharSequence接口，但并没有继承java.lang.String。
GString可以在字符串中嵌入变量，变量形式为\$x或者\${x}。

单引号也能用来包裹字符串，但其内容都会被作为纯文本，不会有特殊含义。

跨行字符串使用三个双引号来包裹。

3. true/false判断

- String非空时为true
- 集合非空时为true
- 非0的数字为true
- 非null的对象引用为true
- Iterators当hasNext=true时为true

4. 操作符

object?.method 对象为null时返回null
object.method() ?: defaultValue  值判断为false时，返回默认值

5. 默认import packages
	- java.io.*
	- java.lang.*
	- java.math.BigDecimal
	- java.math.BigInteger
	- java.net.*
	- java.util.*
	- groovy.lang.*
	- groovy.util.*

6、 方法重载
Java方法重载是在编译器绑定。Groovy是在运行时绑定.
方法默认为public

7. class里field默认为private
8. ==相当于.compareTo, .is相当于Java的==

#### 闭包

def power = { int x, int y ->
  return Math.pow(x, y)
}

不写return时，默认最后一行的值为返回值

#### 集合
创建list: def list = [1,1,2,3,5]

访问元素：list[0] list[-1]从末尾开始

判断是否包含：3 in list  

循环：it是默认的闭包参数  
list.each {
  println it
}

筛选：list.findAll { it%2 == 0 }

转换：list.collect { it * it }

def upper = ["Hello", "World"]*.toUpperCase()

创建LinkedHashMap：
def aMap = [ 'key1' : 'value1', key2 : 'value2', (key) : 'value3']
默认key为字符串型，使用其他类型要加括号

空map：def map = [:]

aMap['key1'] aMap.key1 aMap.'key1'



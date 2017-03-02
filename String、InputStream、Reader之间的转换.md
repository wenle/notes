### String、InputStream、Reader之间的转换

- String为unicode(UTF-16)字符串
- InputStream用来读取字节流
- Reader用来读取字符流

#### String -> InputStream
new ByteArrayInputStream(String.getBytes(charset))
不指定字符集，按平台默认字符集转换

#### String -> Reader
new StringReader(String)

#### InputStream -> String
InputStream.read() 将字节读出来
new String(bytes, charset)

#### InputStream -> Reader
new InputStreamReader(inputStream, charset)

#### Reader -> String
new BufferedReader(reader).readLine()

#### Reader -> InputStream
Reader转为String后，String.getBytes()
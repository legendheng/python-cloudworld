# python-cloudworld
基于python3.6制作词云
##  词云的定义
  根据文本数据进行词频统计，词汇出现频率的不同，按不同比例显示出词汇，生成图片。频率高的词汇显示的大，频率低的词汇显示的小。
##  词云的种类
  中文词云和英文词云
##  准备条件(安装wordcloud、scipy库、matplotlib库、jieba库)前面三个库是中英文词云都需要用到，最后一个库是制作中文词云用的
```python
pip install wordcloud
```
```python
pip install scipy
```
```python
pip install matplotlib
```
```python
pip install jieba
```
##  词云制作的基本原理
  * 获取文本内容，统计词频
  * 读取图片
  * 从背景图片生成颜色值
  * 使图片颜色跟字体颜色一样，合并一起
  * 保存到文件

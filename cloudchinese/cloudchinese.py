import jieba
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread

data = open("cloudchinese.txt","r",encoding='utf-8').read()
cutData = jieba.cut(data, cut_all=True)
# jieba.cut 方法接受三个输入参数: 需要分词的字符串；cut_all 参数用来控制是否采用全模式；HMM 参数用来控制是否使用 HMM 模型。
word = " ".join(cutData)#把分词链接起来，加空格因为英文靠空格分词

bg_pic = imread('sucai.jpg')#读取图片
wordcloud = WordCloud(mask=bg_pic,background_color='#000000',font_path="simkai.ttf",max_words=1000,max_font_size=150,scale=1).generate(word)
image_colors = ImageColorGenerator(bg_pic)#从背景图片生成颜色值
plt.imshow(wordcloud)#使图片颜色跟字体颜色一样，合并一起

plt.axis("off")#关闭显示坐标
plt.show()
wordcloud.to_file('sucaitree.jpg')#保存到文件

from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread
text = open('cloudenglish.txt','r').read()
bg_pic = imread('sucai3.jpg')#读取图片
wordcloud = WordCloud(mask=bg_pic,background_color='white',scale=1.5).generate(text)#根据文本采用默认构造函数WordCloud().generate()生成
image_colors = ImageColorGenerator(bg_pic)#从背景图片生成颜色值
plt.imshow(wordcloud)#使图片颜色跟字体颜色一样，合并一起
plt.axis('off')#关闭显示坐标
plt.show()#展现最终效果
wordcloud.to_file('finalenglish.jpg')#保存到文件
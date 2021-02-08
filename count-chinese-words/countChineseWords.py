# encoding=utf-8
import sys
import jieba

#str = u'永和服装饰品有限公司'
str = sys.argv[1]
str_unicode = unicode(str, 'utf-8')
tokens=jieba.tokenize(str_unicode, mode='search')
count=0
for tk in tokens:
  count = count + 1
print("Number of words: ", count)

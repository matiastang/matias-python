<!--
 * @Author: matiastang
 * @Date: 2022-08-18 10:39:32
 * @LastEditors: matiastang
 * @LastEditTime: 2022-08-18 13:54:30
 * @FilePath: /matias-python/md/scrapy/scrapy传参.md
 * @Description: scrapy传参
-->
# scrapy传参

[spider-arguments](https://docs.scrapy.org/en/latest/topics/spiders.html#spider-arguments)

scrapy参数传递主要由以下几种方式：

1. 全局固定参数（setting设置）
2. 同一个spider内部的固定参数传递（custom_settings）
说明：不同组件之间可以通过from_crawler中的crawler以及open_spider，close_spider，process_item之中的spider传递，例如spider.name可以传递spider 的name
3. 跟请求有关的变量参数可以通过meta和item来传递
4. 不同spider之间的变量参数需要通过全局变量来传递

## -a传递参数
```
$ scrapy crawl myspider -a count=10
```
```py
def __init__(self, count=None, *args, **kwargs):
        super(WelfareLastSpider, self).__init__(*args, **kwargs)
        print(f'count={count}')

```

第二种方法，在用scrapyd控制spider的时候，可以向schedule.json发送-d选项加入参数，同样的，也需要在spider的构造函数里如上写法。例如：

```
$ curl http://localhost:6800/schedule.json -d project=myproject -d spider=somespider -d setting=DOWNLOAD_DELAY=2 -d arg1=val1
```
另外，如果需要在scrapy发出的request上加入参数，可以使用request的meta参数，然后就可以相应的在返回的respose对象中获得传入的参数。这在某些情况下相当有用，比如说需要确定这个url是哪个用户请求爬取的，可以先用上面两种方法之一将信息传递给spider，spider就可以把这个信息加入到request中，然后在相应的reponse中就可以将这个信息与从url的页面中获得的信息一起存入数据库。
```py
def parse_page1(self, response):
  item = MyItem()
  item['main_url'] = response.url
  request = scrapy.Request("http://www.example.com/some_page.html",
               callback=self.parse_page2)
  request.meta['item'] = item
  return request
 
def parse_page2(self, response):
  item = response.meta['item']
  item['other_url'] = response.url
  return item
```
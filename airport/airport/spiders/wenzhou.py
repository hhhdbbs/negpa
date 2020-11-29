import scrapy
from airport.items import AirportItem
import json
class WenzhouSpider(scrapy.Spider):
    name = 'wenzhou'
    allowed_domains = ['www.wzair.cn']
    start_urls = ['http://www.wzair.cn/lkfw/hbxx/jrdg/index.html?rxLoad=1&_rand=1606630337236']

    def parse(self, response):
        airport_info={}
        data=json.loads(json.dumps(airport_info))
        data={}


        node_list=response.xpath("//td[@id='hangbaoInfoBox']")
        print(node_list)
        print("__________________________________________")
        for node in node_list:
            xuhao=node.xpath("./th[0]/text()").extract()
            hangbanhao=node.xpath("./th[1]/text()").extract()
            hangkonggongsi=node.xpath("./th[2]/text()").extract()
            chufadi=node.xpath("./th[3]/text()").extract()
            jihuaqifei=node.xpath("./th[4]/text()").extract()
            shijiqifei=node.xpath("./th[5]/text()").extract()
            yujidaoda=node.xpath("./th[6]/text()").extract()
            shijidaoda=node.xpath("./th[7]/text()").extract()
            jingtingzhan=node.xpath("./th[8]/text()").extract()
            zhuangtai=node.xpath("./th[9]/text()").extract()
            beizhu=node.xpath("./th[10]/text()").extract()
            print("__________________________________________")
            content={
                'xuhao':xuhao[0],
                'hangbanhao':hangbanhao[0],
                'hangkonggongsi':hangkonggongsi[0],
                'chufadi':chufadi[0],
                'jihuaqifei':jihuaqifei[0],
                'shijiqifei':shijiqifei[0],
                'yujidaoda':yujidaoda[0],
                'shijidaoda':shijidaoda[0],
                'jingtingzhan':jingtingzhan[0],
                'zhuangtai':zhuangtai[0],
                'beizhu':beizhu[0]
            }
            data.append(content)

        item=AirportItem()
        item['info']=data
        yield(item)
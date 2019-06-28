import requests
import re
import time
import random
from lxml import etree


class WeiYi(object):
    def __init__(self):
        """初始化"""
        self.pattern_val = re.compile('name="sign".*?value="(.*?)"')
        self.pattern_time = re.compile('name="timestamp".*?value="(.*?)"')
        self.doctor_name = re.compile('.*(\w)')
        self.url = "https://www.guahao.com/commentslist/h-125336754304601000/1-0"
        self.data = "F98CADB881686C6E7DE0D78711CD6739385CC337DAEBF347934BDDB13C018E76415AE203054FBA9A"
        self.data1 = "1527943007685"
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "cookie": "_sid_=15224054212110651956551; _fp_code_=b99b3fcb2c173a2719f2157a54bcdbf3; _ipgeo=province%3A%E6%B9%96%E5%8C%97%7Ccity%3A%E6%AD%A6%E6%B1%89; _e_m=1527939221005; Hm_lvt_5697507823ecd633819db0771bb99cfb=1527939225,1527939251; _sh_ssid_=1527941695607; monitor_sid=9; mst=1527941697466; JSESSIONID=1l7g9ke10cd2t1xff1vfkifrfh; __usx__=""; __wyt__=!PVH7BIjcEnE1srkCUQ6GNbCt3O1D_EWqSk-HZOR6OraaJo1L9mCfVxYwySALHvu2K_P8lESrBnnIhXAjFPbz63ZiO_hIA4wInPOvtC3P8AD45XUMJG-6ChkCHOE2AKqRBSOxlcvtaJIqbiFW4AVuHXqvrm3jn8kkGYW9RfupMxrGI; _ci_=QgAHlxJ/u9Dbai4pGj1pAHgiYzjGt3Y20M0OwI/o+XUh5jsYkgZUR6s5/nFJXPhE; __i__=zOnom529CLgbUB/iEwNh1O7QojaVerY0y0UdHwxmNuU=; __uiu__=Qvh+0aIbdN8GEF9A6ypvhrvJ+BIz3RNey3ofkYSMf5Orm+bShvXDfA==; __up__=LpYLUy6TQ7+JzbTK2mU3H/Oc1XD2s9Wba2izLueDk1E=; _exp_=LyRgvLkJK27tn50gWWifp3FdKjsg8CiAiZ43l1RnnpE=; __p__=4/qTaUSM35f8C1pDIT7jcY3KWXX3F4yn8EQmtblko2Y4UMmKvHZ3gg==; __rf__=OWQfOTal7lck2lXGICUgbVb582rFAz6EAAT6csy3CNyHl1Thsqq6ZzwFelhTGmm4vQfIXwdE7w+ajGlWSp68hGdlS9eLY8N/jqeNOc8RrnWMv6suCWzdU+NmMoeXkfHBKjFAR4F/Pqo=; monitor_seq=24; mlt=1527943229308; Hm_lpvt_5697507823ecd633819db0771bb99cfb=1527943229",
            "referer": "https://www.guahao.com/commentslist/h-125336754304601000/1-0?pageNo=11&sign=F98CADB881686C6E7DE0D78711CD6739385CC337DAEBF347934BDDB13C018E76CABBF37CB7B6B10D&timestamp=1527942843278",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
        }
        self.params = {
            "pageNo": "1",
            "sign": self.data,
            "timestamp": self.data1,
        }

    def run(self):
        ssion = requests.session()
        end_url = ""
        for i in range(1, 5):
            time.sleep(random.uniform(1, 3))
            if i == 1:
                response = ssion.get(url=self.url, headers=self.headers, params=self.params)
                end_url = response.url
            else:
                headers = {
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "cache-control": "max-age=0",
                    "cookie": "_sid_=15224054212110651956551; _fp_code_=b99b3fcb2c173a2719f2157a54bcdbf3; _ipgeo=province%3A%E6%B9%96%E5%8C%97%7Ccity%3A%E6%AD%A6%E6%B1%89; _e_m=1527939221005; Hm_lvt_5697507823ecd633819db0771bb99cfb=1527939225,1527939251; _sh_ssid_=1527941695607; monitor_sid=9; mst=1527941697466; JSESSIONID=1l7g9ke10cd2t1xff1vfkifrfh; __usx__=""; __wyt__=!PVH7BIjcEnE1srkCUQ6GNbCt3O1D_EWqSk-HZOR6OraaJo1L9mCfVxYwySALHvu2K_P8lESrBnnIhXAjFPbz63ZiO_hIA4wInPOvtC3P8AD45XUMJG-6ChkCHOE2AKqRBSOxlcvtaJIqbiFW4AVuHXqvrm3jn8kkGYW9RfupMxrGI; _ci_=QgAHlxJ/u9Dbai4pGj1pAHgiYzjGt3Y20M0OwI/o+XUh5jsYkgZUR6s5/nFJXPhE; __i__=zOnom529CLgbUB/iEwNh1O7QojaVerY0y0UdHwxmNuU=; __uiu__=Qvh+0aIbdN8GEF9A6ypvhrvJ+BIz3RNey3ofkYSMf5Orm+bShvXDfA==; __up__=LpYLUy6TQ7+JzbTK2mU3H/Oc1XD2s9Wba2izLueDk1E=; _exp_=LyRgvLkJK27tn50gWWifp3FdKjsg8CiAiZ43l1RnnpE=; __p__=4/qTaUSM35f8C1pDIT7jcY3KWXX3F4yn8EQmtblko2Y4UMmKvHZ3gg==; __rf__=OWQfOTal7lck2lXGICUgbVb582rFAz6EAAT6csy3CNyHl1Thsqq6ZzwFelhTGmm4vQfIXwdE7w+ajGlWSp68hGdlS9eLY8N/jqeNOc8RrnWMv6suCWzdU+NmMoeXkfHBKjFAR4F/Pqo=; monitor_seq=24; mlt=1527943229308; Hm_lpvt_5697507823ecd633819db0771bb99cfb=1527943229",
                    "referer": end_url,
                    "upgrade-insecure-requests": str(i),
                    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
                }
                params = {
                    "pageNo": str(i),
                    "sign": self.data,
                    "timestamp": self.data1,
                }
                response = ssion.get(url=self.url, headers=headers, params=params)
                end_url = response.url
            # print(end_url)
            html = response.text
            self.data = self.pattern_val.findall(html)
            self.data1 = self.pattern_time.findall(html)
            print(self.data[0])
            print(self.data1[0])
            self.extract(html)
            break

    def extract(self, html):
        """因为有的医生是span，有的是在span下面，就只能对每个医生单独操作"""
        xhtml = etree.HTML(html)
        xhtml = xhtml.xpath('//*[@id="comment-list"]/li')

        for i in range(1, 6):

            name = xhtml[0].xpath('//li[%s]/div[1]/p/text()' % i)
            # print(name[0].strip())
            name = name[0].strip()
            grade = xhtml[0].xpath('//li[%s]/div[2]/p[2]/span' % i)
            # 计算出现的星号次数
            grade_num = len(grade)
            # print(grade_num)

            try:
                doctor = xhtml[0].xpath('//li[%s]/div[3]/div[2]/p/span[2]/a/text()' % i)[0]
            except Exception as e:
                doctor = xhtml[0].xpath('//li[%s]/div[3]/div[2]/p/span[2]/text()' % i)
                # print(doctor[0])
                temp = str(doctor[0])
                doctor = self.doctor_name.findall(str(temp), re.S)
                # print(temp)
                # print(doctor)

            # print(doctor[0].strip())
            comment = xhtml[0].xpath('//li[%s]/div[3]/div[1]/span/text()' % i)
            # print(comment[0].strip())
            time = xhtml[0].xpath('//li[%s]/div[3]/div[2]/p/span[1]/text()' % i)
            # print(time[0].strip())
            self.save(name, grade_num, doctor, comment, time)

    def save(self, name, grade_num, doctor, comment, time):
        print(name[0].strip())
        print(grade_num)
        print(doctor[0].strip())
        print(comment[0].strip())
        print(time[0].strip())



# with open("微医.html", "w", encoding="utf-8") as f:
#     f.write(response.content.decode("utf-8"))

if __name__ == '__main__':
    weiyi = WeiYi()
    weiyi.run()

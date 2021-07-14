import scrapy
import os
base_path = os.getcwd()
if os.path.exists("new_file.csv"):
    os.remove("new_file.csv")
else:
    pass
# os.mkdir(base_path)
import csv
class HkmaSpider(scrapy.Spider):
    name = 'hkma'
    # allowed_domains = ['https://www.hkma.gov.hk/eng/regulatory-resources/regulatory-guides/circulars/']
    start_urls = ['https://www.hkma.gov.hk/eng/regulatory-resources/regulatory-guides/circulars/']

    def parse(self, response):
        try:
            doc_name = response.xpath("//div[@class='template-index']//a[@href]/text()").getall()
            doc_url = response.xpath("//div[@class='template-index']//a/@href").getall()
            doc_date = response.xpath("//tbody[@id='circular-result']//td[2]/text()").getall()

            # yield {
            #     'Doc_Name': doc_name,
            #     'Doc_URL': doc_url,
            #     'Date': doc_date
            #     }
            with open(os.path.join(base_path,"new_file.csv"),"w",newline='',encoding='utf-8') as doc_1:
                csvwriter = csv.writer(doc_1,delimiter=',')
                csvwriter.writerow(["doc name","doc_url", "doc_date"])
                for (name,url,date) in zip(doc_name,doc_url,doc_date):
                #     csvwriter.writerow([name])
                # for item in range(len(doc_url)):
                    csvwriter.writerow([name, url, date])


                doc_1.close()


        except Exception as e:
            print("**********", e)
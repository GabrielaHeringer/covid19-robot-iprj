import scrapy
import json
import langdetect
from csv import DictReader
from app.models import Novidade, PortalBusca, Credibilidade 
from scrapping.items import WebPostItem


class CovidSearchDoctorEvidenceSpider(scrapy.Spider):
    name = 'CovidSearchDoctorEvidence2'
    allowed_domains = ['covid-search.doctorevidence.com']
    start_urls = ['https://covid-search.doctorevidence.com/']
    download_timeout = 999999999999

    def parse(self, response):
        # variável que armazena os dados do usuário
        auth_pattern = r'\bvar\s+userProfile\s*=\s*(\{.*?\})\s*;\n'
        # variável que armazena os dados de busca exibidos na página
        signals_pattern = r'\bvar\s+signals\s*=\s*(\[\{.*?\}\])\s*;'

        # Para fazer o download do conteúdo, precisamos passar um cookie com o
        # token dessa variável
        auth = response.css('script[type="text/javascript"]').re_first(auth_pattern)
        auth_token = json.loads(auth)['auth-token']

        json_data = response.css('script[type="text/javascript"]').re_first(signals_pattern)

        data = json.loads(json_data)
        lista = [3, 4, 6, 8, 10, 11, 21, 25, 29, 30, 34, 36, 37, 38, 40, 41]
        for i in lista:
                el = data[i]
                query = el['query']['query/normalized-blunt']

                request = scrapy.Request(
                    url = 'https://covid-search.doctorevidence.com/api/articles/export',
                    method = 'post',
                    body = '["^ ","~:blunt","{}","~:format","csv","~:order","new","~:order-direction","desc","~:limit",200000]'.format(query),
                    cookies = { '.ASPXAUTHSSO': auth_token },
                    callback = self.parse_file,
                    headers = { 'content-type': 'application/transit+json' },
                )
                request.meta['assunto'] = el['title']
                yield request

    def parse_file(self, response):

        for item in DictReader(response.text.splitlines()): 
            items = WebPostItem()
            dic = dict(item)

            titulo = dic['Title']
            if titulo != '':
                items['titulo'] = titulo
            else:
                continue

            try:
                idioma = langdetect.detect(dic['Title'])
            except langdetect.lang_detect_exception.LangDetectException:
                idioma = "error"
                print("This row throws and error:", dic['Title'])

            if idioma == 'en' or idioma == 'es' or idioma == 'pt':
                items['idioma'] = idioma
            else:
                continue        

            assunto = response.meta.get('assunto')
            items['resumo'] = dic['Abstract']
            items['fonte'] = dic['DocSearch url']
            items['autores'] = dic['All Authors']
            items['link_externo'] = dic['Url']
            items['categoria'] = dic['Category']
            items['data_publicacao'] = dic['Published date']
            items['subject'] = assunto
            items['portal'] = 'Doctor Evidence'

            yield items


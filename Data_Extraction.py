import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import html

links=['https://www.merchantcircle.com/pc-aspirin-east-brunswick-nj',
       'https://www.merchantcircle.com/toms-fireworks-super-center-philadelphia-ms',
       'https://www.merchantcircle.com/billo-african-arts-dealer-jamaica-ny',
       'https://www.merchantcircle.com/advanced-hypnotherapy-group-chatsworth-ca',
       'https://www.merchantcircle.com/pantry-perfection-eagle-id',
       'https://www.merchantcircle.com/manne-king-denver-co',
       'https://www.merchantcircle.com/suthin-computer-company-la-crosse-va',
       'https://www.merchantcircle.com/business/Byrne.Building.Solutions.877-341-1271',
       'https://www.merchantcircle.com/schu-marketing-associates-minneapolis-mn',
       'https://www.merchantcircle.com/elmer-door-co4-elmer-nj',
       'https://www.merchantcircle.com/ram-gadget-co-phoenixville-pa',
       'https://www.merchantcircle.com/Top.Secret.Hair.866-403-7920',
       'https://www.merchantcircle.com/business/Shaklee.Products.Whitehouse.NJ.800-274-7873',
       'https://www.merchantcircle.com/antelope-express-airport-shuttle-charter-lancaster-ca',
       'https://www.merchantcircle.com/homevestors-orlando-fl',
       'https://www.merchantcircle.com/business/Microlnk.Lincoln.NE.866-795-6565',
       'https://www.merchantcircle.com/business/LPMG.215-769-5764',
       'https://www.merchantcircle.com/pulte-homes-colorado-springs-division1-colorado-springs-co',
       'https://www.merchantcircle.com/ca-paso-robles-93446/recreation/golf',
       'https://www.merchantcircle.com/psperandeo-herbalife-branford-ct',
       'https://www.merchantcircle.com/business/Pier.17.Marine.Inc.904-387-4669',
       'https://www.merchantcircle.com/scott-f-humble-j-d-esq-p-c-olean-ny',
       'https://www.merchantcircle.com/foster-farms-dairy-san-mateo-ca',
       'https://www.merchantcircle.com/business/Opatz.Metals.Inc.320-746-2819',
       'https://www.merchantcircle.com/yelsky-lonardo1-cleveland-oh',
       'https://www.merchantcircle.com/a-us-auto-glass-bayville-nj',
       'https://www.merchantcircle.com/trugreen-somerset-pa',
       'https://www.merchantcircle.com/transparsoft-bradenton-fl',
       'https://www.merchantcircle.com/business/Off.The.Record.509-453-8652',
       'https://www.merchantcircle.com/colombia-signature-miami-beach-fl',
       'https://www.merchantcircle.com/santmyer-oil-co1-wooster-oh',
       'https://www.merchantcircle.com/dane-zynda-cmt-rochester-mi',
       'https://www.merchantcircle.com/precision-door-service1-palatine-il',
       'https://www.merchantcircle.com/a-b-c-humane-wildlife-rescue-control-prevention-palatine-il',
       'https://www.merchantcircle.com/pope-company-custom-homes2-forney-tx',
       'https://www.merchantcircle.com/The.Dieter.Company.843-237-2813',
       'https://www.merchantcircle.com/rebinding-love-spells-new-york-ny',
       'https://www.merchantcircle.com/h-m-limousine-service-dundee-il',
       'https://www.merchantcircle.com/carstens-motor-co1-breckenridge-tx',
       'https://www.merchantcircle.com/business/Patriot.Roofing.781-965-1558',
       'https://www.merchantcircle.com/a-1-mobile-tax-service3-bradenton-fl',
       'https://www.merchantcircle.com/harding-s-mobile-home-repair-council-bluffs-ia',
       'https://www.merchantcircle.com/john-deere-barnett-implement-snohomish-wa',
       'https://www.merchantcircle.com/business/United.States.Government.Social.Security.Administration.888-777-5443',
       'https://www.merchantcircle.com/trevo-kokomo-in',
       'https://www.merchantcircle.com/ca-garberville-95542/legal-and-financial/insurance',
       'https://www.merchantcircle.com/regional-medical-laboratories-battle-creek-mi',
       'https://www.merchantcircle.com/long-distance-moving-brooklyn-ny',
       'https://www.merchantcircle.com/business/Western.Driver.Services.800-929-1318',
       'https://www.merchantcircle.com/apple-fast-cash-personal-loans-wilmington-de',
       'https://www.merchantcircle.com/business/Semcil.Inc.And.Choice.Home.Care.Inc.507-285-1815',
       'https://www.merchantcircle.com/business/Floor.Systems.888-867-4105',
       'https://www.merchantcircle.com/business/Floor.Systems.207-353-6690',
       'https://www.merchantcircle.com/business/Sysco.Food.Services.of.New.Orleans.504-731-1015',
       'https://www.merchantcircle.com/volunteers-of-america-delaware-valley-oaklyn-nj',
       'https://www.merchantcircle.com/roessner-energy-products2-coldwater-oh',
       'https://www.merchantcircle.com/martins-building-plumbing2-altus-ok',
       'https://www.merchantcircle.com/business/Star.Uniforms.309-662-7144',
       'https://www.merchantcircle.com/business/Creative.Designers.LLC.888-991-4353',
       'https://www.merchantcircle.com/business/Delta.Eye.Medical.Group.Inc.209-334-5886',
       'https://www.merchantcircle.com/business/Midamerican.Energy.Company.800-747-0593',
       'https://www.merchantcircle.com/business/Honda.Superstore.of.Joliet.815-439-2222/picture/gallery',
       'https://www.merchantcircle.com/shelton-associates-pa-tupelo-ms',
       'https://www.merchantcircle.com/town-country-veterinary-associates-vernon-rockville-ct',
       'https://www.merchantcircle.com/business/AAA.Carey.Griffin.Insurance.Agency.877-392-8870',
       'https://www.merchantcircle.com/blogs/hub-city-doors-junction-city-wi/2012/2/Broken-Spring/867700',
       'https://www.merchantcircle.com/waste-management27-omaha-ne',
       'https://www.merchantcircle.com/elmore-truck-and-trailer-service-elmore-mn',
       'https://www.merchantcircle.com/pro-insulation-yucaipa-ca',
       'https://www.merchantcircle.com/cnr-estate-sale-service3-zillah-wa/neighbors',
       'https://www.merchantcircle.com/ia-grundy-center-50638/autos',
       'https://www.merchantcircle.com/century-21-moorestown-nj',
       'https://www.merchantcircle.com/myescorts4you-flushing-ny',
       'https://www.merchantcircle.com/tampa-accident-attorney-abogado-en-tampa-orlando-accident-attorney-888-420-4878-bills-redon-pa1-tampa-fl',
       'https://www.merchantcircle.com/orlando-motorcycle-accident-attorney-daytona-motorcycle-accident-attorney-consults-doug-bills-redon-attorney-at-law-winter-park-fl',
       'https://www.merchantcircle.com/the-world-famous-pie-lady-memphis-tn',
       'https://www.merchantcircle.com/white-deer-run3-allenwood-pa',
       'https://www.merchantcircle.com/business/Clemons.Courier.Services.804-672-7336',
       'https://www.merchantcircle.com/business/Hill.Plumbing.And.Electric.Co.Inc..803-733-6689',
       'https://www.merchantcircle.com/brolly-communications-dba-gobrolly-louisburg-ks',
       'https://www.merchantcircle.com/jamisons-chimney-service2-carbondale-il',
       'https://www.merchantcircle.com/business/Nanovoltaix.Inc.Phoenix.AZ.480-295-3500',
       'https://www.merchantcircle.com/northeast-financial-middlefield-ct',
       'https://www.merchantcircle.com/kohlls-pharmacy-homecare13-omaha-ne',
       'https://www.merchantcircle.com/kochers-water-pumps-tanks-bartonsville-pa',
       'https://www.merchantcircle.com/business/M.Barboza.And.Sons.Roofing.And.Sheet.Metal.Company.Incorporated.888-322-3025',
       'https://www.merchantcircle.com/httpveteransflagdepot.com',
       'https://www.merchantcircle.com/business/Sunsational.Patio.And.Sunrooms.330-425-1479',
       'https://www.merchantcircle.com/blogs/pawsitively-pawfect-park-ridge-nj/2014/11/Pawsitively-Pawfect/1207661',
       'https://www.merchantcircle.com/business/Scottys.Signs.Inc.757-245-7129',
       'https://www.merchantcircle.com/business/Route.65.Auto.724-654-6500',
       'https://www.merchantcircle.com/power-kia2-salem-or',
       'https://www.merchantcircle.com/business/McMahan.Business.Interiors.949-727-1234',
       'https://www.merchantcircle.com/marquise-equipment-leasing-metairie-la',
       'https://www.merchantcircle.com/stellar-vinyl-decals-mission-viejo-ca',
       'https://www.merchantcircle.com/business/Bigger.Log.Homes.2.888-477-5922',
       'https://www.merchantcircle.com/sylvan-learning-center-orange-city-fl',
       'https://www.merchantcircle.com/the-dust-bunnys-media-pa',
       'https://www.merchantcircle.com/charlotte-russe-cherry-hill-nj',
       'https://www.merchantcircle.com/gbw-insurance-flanders-nj']
lst=[]
for url in links:
    page = requests.get(url)
    
    soup=BeautifulSoup(page.text, 'lxml')
    
    MerchantCircle=soup.find('div', class_='info')
    name=MerchantCircle.find('h1', {'id':'business-name'}).text
    address=MerchantCircle.find('div', class_='directions').text.strip()
    website=MerchantCircle.find('a', class_='url').get('href')
    phone=MerchantCircle.find('span', class_='_business_phone').text
    df={'name':name,'address':address,'website':website,'phone':phone}
    lst.append(df)
df=pd.DataFrame(lst)

df.to_csv('/home/deva/Desktop/result.csv',index=False)
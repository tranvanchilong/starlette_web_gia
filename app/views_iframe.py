# from starlette.responses import Response
# from starlette.responses import HTMLResponse
# from starlette.routing import Route
# from starlette.responses import PlainTextResponse, JSONResponse
# from starlette.templating import Jinja2Templates


# import os
# import motor.motor_asyncio
# from bson import ObjectId
# from starlette.exceptions import HTTPException

# import json
# from db import MongoAsyncPipeline

# import time
# import datetime
# # import requests
# # import python-multipart

# import multipart   #dùng để chạy  data = await request.form() dòng 71
# # pip install python-multipart
# from settings import check_token

# MONGO_URI = "mongodb://adminmg:tM5Jngh9EbKu@139.162.28.246:27018/" #"mongodb://adminmg:tM5Jngh9EbKu@5.161.176.184:27018/"
# MONGODB_DB = 'web_gia_com'
# MONGODB_COLLECTION = "data"
# db_client = MongoAsyncPipeline(MONGO_URI, MONGODB_DB)

# templates=Jinja2Templates(directory="templates")

# async def time_page(request):
#     node= datetime.datetime.now() + datetime.timedelta(hours=-1)
#     time=f'{node.strftime("%H:%M:%S")} {node.strftime("%d/%m/%Y")}'
#     if request.method == "POST":
#         # for change in list_change2:
#         #     node=node.replace(change["remove"],change["replace"])
#         data = await request.form()
#         token = data["token"]
#         if token==check_token:
#             return HTMLResponse(time)
#     else:
#         context={"request":request, "data": node, "time":time}
#         return (templates.TemplateResponse("time.html",context))


# async def home_page(request):
#     myquery = {"path": "giavang", "name_path": "sjc-tren-toan-quoc"}
#     filter_ = None 
#     filter_ = {"_id": 1, "table": 1, "name":1, "father":1, "update_time":1} 
#     db_data = await db_client.find_one(myquery, MONGODB_COLLECTION, filter_)
    
#     # return PlainTextResponse("home")
#     list_change = [
#             { 
#             "path": "giavang"    ,   
#             "remove":"SJC",
#             "replace": '<a href="/giavang/sjc">SJC</a>'
#             },
#             { 
#             "path": "giavang"    ,   
#             "remove":"PNJ",
#             "replace": '<a href="/giavang/pnj">PNJ</a>'
#             },
#             { 
#             "path": "giavang"    ,   
#             "remove":"Phú Quý",
#             "replace": '<a href="/giavang/phu-quy">Phú Quý</a>'
#             },
#             { 
#             "path": "giavang"    ,   
#             "remove":"Mi Hồng",
#             "replace": '<a href="/giavang/mi-hong">Mi Hồng</a>'
#             },
#             { 
#             "path": "giavang"    ,   
#             "remove":"Bảo Tín Minh Châu",
#             "replace": '<a href="/giavang/bao-tin-minh-chau">Bảo Tín Minh Châu</a>'
#             }
#             ]

#     list_change2 = [
#             { 
#             "path": ""    ,   
#             "remove":"SJC",
#             "replace": '<a href="/gia-vang/sjc">SJC</a>'
#             },
#             { 
#             "path": ""    ,   
#             "remove":"PNJ",
#             "replace": '<a href="/gia-vang/pnj">PNJ</a>'
#             },
#             { 
#             "path": ""    ,   
#             "remove":"Phú Quý",
#             "replace": '<a href="/gia-vang/phu-quy">Phú Quý</a>'
#             },
#             { 
#             "path": ""    ,   
#             "remove":"Mi Hồng",
#             "replace": '<a href="/gia-vang/mi-hong">Mi Hồng</a>'
#             },
#             { 
#             "path": ""    ,   
#             "remove":"Bảo Tín Minh Châu",
#             "replace": '<a href="/gia-vang/bao-tin-minh-chau">Bảo Tín Minh Châu</a>'
#             }
#             ]
#     node= db_data["table"]
    
#     if request.method == "POST":
#         for change in list_change2:
#             node=node.replace(change["remove"],change["replace"])
#         data = await request.form()
#         token = data["token"]
#         if token==check_token:
#             return HTMLResponse(node)
#     else:
#         for change in list_change:
#             node=node.replace(change["remove"],change["replace"])
#         time=db_data["update_time"]
#         context={"request":request, "data": node, "time":time}
#         return (templates.TemplateResponse("home_iframe.html",context))

# async def blog(request):
#     context={"request":request}
#     return (templates.TemplateResponse("blog.html",context))
# async def tygia(request):
#     context={"request":request}
#     return (templates.TemplateResponse("tygia.html",context))

# async def language_page(request):
#     # page = request.path_params["page"]
    
#     path=request.path_params["path"]
#     name=request.path_params["name"]
    
#     table=[]
#     myquery = {"path": path, "name_path": name}
#     myquery2 = {"path": path}
#     filter_ = None 
#     filter_ = {"_id": 1, "table": 1, "name":1, "father":1, "update_time":1 } 
#     filter2_ = {"name":1, "name_path":1, } 
#     db_data = await db_client.find_many(myquery,MONGODB_COLLECTION, filter_)
#     record_data=[(record) for record in db_data]
#     data2 = {
#         "meta_title": record_data[0]["father"]+" - "+ record_data[0]["name"],
#         "site_name": "Long crawl"
#     }

#     data_name= await db_client.find_many(myquery2, MONGODB_COLLECTION, filter2_)
#     record_data2=[(record) for record in data_name]
#     # for cat in record_data2:
#     #     print(cat)    
#     data2.update({
#         "db_data": db_data
#         # "fathers": fathers
#     })
#     # for data in db_data:
#     #     print(data)
    
    

#     if request.method == "POST":
#         data = await request.form()
#         token = data["token"]
#         # print(record_data[0]["table"])
#         if token==check_token:
#             list_change= [
#         ##tỷ giá
#                 { 
#                 "path": "tygia",
#                 "remove":"USD",
#                 "replace": '<a href="/ngoai-te/usd">USD</a>'
#                 },
#                 { 
#                 "path": "tygia",
#                 "remove":"EUR",
#                 "replace": '<a href="/ngoai-te/eur">EUR</a>'
#                 },
#                 {
#                 "path": "tygia" ,
#                 "remove":"GBP",
#                 "replace": '<a href="/ngoai-te/gbp">GBP</a>'
#                 },
#                 { 
#                 "path": "tygia" ,   
#                 "remove":"HKD",
#                 "replace": '<a href="/ngoai-te/hkd">HKD</a>'
#                 },
#                 { 
#                 "path": "tygia"   ,  
#                 "remove":"CHF",
#                 "replace": '<a href="/ngoai-te/chf">CHF</a>'
#                 },
#                 { 
#                 "path": "tygia"   ,
#                 "remove":"JPY",
#                 "replace": '<a href="/ngoai-te/jpy">JPY</a>'
#                 },
#                 { 
#                 "path": "tygia"  , 
#                 "remove":"AUD",
#                 "replace": '<a href="/ngoai-te/aud">AUD</a>'
#                 },
#                 { 
#                 "path": "tygia"   ,    
#                 "remove":"SGD",
#                 "replace": '<a href="/ngoai-te/sgd">SGD</a>'
#                 },
#                 { 
#                 "path": "tygia"    ,   
#                 "remove":"THB",
#                 "replace": '<a href="/ngoai-te/thb">THB</a>'
#                 },
#                 { 
#                 "path": "tygia"   ,    
#                 "remove":"CAD",
#                 "replace": '<a href="/ngoai-te/cad">CAD</a>'
#                 },
#                 { 
#                 "path": "tygia"   ,    
#                 "remove":"NZD",
#                 "replace": '<a href="/ngoai-te/nzd">NZD</a>'
#                 },
#                 { 
#                 "path": "tygia"   ,    
#                 "remove":"KRW",
#                 "replace": '<a href="/ngoai-te/krw">KRW</a>'
#                 },
#                 { 
#                 "path": "tygia"    ,   
#                 "remove":"SEK",
#                 "replace": '<a href="/ngoai-te/sek">SEK</a>'
#                 },
#                 { 
#                 "path": "tygia"    ,   
#                 "remove":"TWD",
#                 "replace": '<a href="/ngoai-te/twd">TWD</a>'
#                 },
#                 { 
#                 "path": "tygia"    ,   
#                 "remove":"SAR",
#                 "replace": '<a href="/ngoai-te/sar">SAR</a>'
#                 },
#                 { 
#                 "path": "tygia"    ,   
#                 "remove":"RUB",
#                 "replace": '<a href="/ngoai-te/rub">RUB</a>'
#                 },
#                 { 
#                 "path": "tygia"    ,   
#                 "remove":"NOK",
#                 "replace": '<a href="/ngoai-te/nok">NOK</a>'
#                 },
#                 { 
#                 "path": "tygia"    ,   
#                 "remove":"MYR",
#                 "replace": '<a href="/ngoai-te/myr">MYR</a>'
#                 },
#                 { 
#                 "path": "tygia"    ,   
#                 "remove":"KWD",
#                 "replace": '<a href="/ngoai-te/kwd">KWD</a>'
#                 },
#                 { 
#                 "path": "tygia"    ,   
#                 "remove":"INR",
#                 "replace": '<a href="/ngoai-te/inr">INR</a>'
#                 },
#                 { 
#                 "path": "tygia"    ,   
#                 "remove":"CNY",
#                 "replace": '<a href="/ngoai-te/cny">CNY</a>'
#                 },
#                 { 
#                 "path": "tygia"    ,   
#                 "remove":"DKK",
#                 "replace": '<a href="/ngoai-te/dkk">DKK</a>'
#                 },
#                 ##giá vàng
#                 { 
#                 "path": ""    ,   
#                 "remove":"SJC",
#                 "replace": '<a href="/gia-vang/sjc">SJC</a>'
#                 },
#                 { 
#                 "path": ""    ,   
#                 "remove":"PNJ",
#                 "replace": '<a href="/gia-vang/pnj">PNJ</a>'
#                 },
#                 { 
#                 "path": ""    ,   
#                 "remove":"Phú Quý",
#                 "replace": '<a href="/gia-vang/phu-quy">Phú Quý</a>'
#                 },
#                 { 
#                 "path": ""    ,   
#                 "remove":"Mi Hồng",
#                 "replace": '<a href="/gia-vang/mi-hong">Mi Hồng</a>'
#                 },
#                 { 
#                 "path": ""    ,   
#                 "remove":"Bảo Tín Minh Châu",
#                 "replace": '<a href="/gia-vang/bao-tin-minh-chau">Bảo Tín Minh Châu</a>'
#                 },
#                 ##ngoại tệ
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"ABBank",
#                 "replace": '<a href="/ty-gia/abbank">ABBank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"ACB",
#                 "replace": '<a href="/ty-gia/acb">ACB</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"Agribank",
#                 "replace": '<a href="/ty-gia/agribank">Agribank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"Bảo Việt",
#                 "replace": '<a href="/ty-gia/baovietbank">Bảo Việt</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"BIDV",
#                 "replace": '<a href="/ty-gia/bidv">BIDV</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"CBBank",
#                 "replace": '<a href="/ty-gia/cbbank">CBBank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"Đông Á",
#                 "replace": '<a href="/ty-gia/donga-bank">Đông Á</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"Eximbank",
#                 "replace": '<a href="/ty-gia/eximbank">Eximbank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"GPBank",
#                 "replace": '<a href="/ty-gia/gpbank">GPBank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"HDBank",
#                 "replace": '<a href="/ty-gia/hdbank">HDBank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"Hong Leong",
#                 "replace": '<a href="/ty-gia/hlbank">Hong Leong</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"HSBC",
#                 "replace": '<a href="/ty-gia/hsbc">HSBC</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"Indovina",
#                 "replace": '<a href="/ty-gia/indovina-bank">Indovina</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"Kiên Long",
#                 "replace": '<a href="/ty-gia/kienlong-bank">Kiên Long</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"Liên Việt",
#                 "replace": '<a href="/ty-gia/lienvietpostbank">Liên Việt</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"MB",
#                 "replace": '<a href="/ty-gia/mb-bank">MB</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"MSB",
#                 "replace": '<a href="/ty-gia/maritime-bank">MSB</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"Nam Á",
#                 "replace": '<a href="/ty-gia/nam-a-bank">Nam Á</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"NCB",
#                 "replace": '<a href="/ty-gia/ncb">NCB</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"OCB",
#                 "replace": '<a href="/ty-gia/ocb">OCB</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"OceanBank",
#                 "replace": '<a href="/ty-gia/oceanbank">OceanBank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"PGBank",
#                 "replace": '<a href="/ty-gia/pgbank">PGBank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"PublicBank",
#                 "replace": '<a href="/ty-gia/public-bank">PublicBank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"PVcomBank",
#                 "replace": '<a href="/ty-gia/pvcombank">PVcomBank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"Sacombank",
#                 "replace": '<a href="/ty-gia/sacombank">Sacombank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"Saigonbank",
#                 "replace": '<a href="/ty-gia/saigonbank">Saigonbank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"SCB",
#                 "replace": '<a href="/ty-gia/scb">SCB</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"SeABank",
#                 "replace": '<a href="/ty-gia/seabank">SeABank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"SHB",
#                 "replace": '<a href="/ty-gia/shb">SHB</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"Techcombank",
#                 "replace": '<a href="/ty-gia/techcombank">Techcombank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"TPB",
#                 "replace": '<a href="/ty-gia/tpbank">TPB</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"UOB",
#                 "replace": '<a href="/ty-gia/uob">UOB</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"VIB",
#                 "replace": '<a href="/ty-gia/vib">VIB</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"VietABank",
#                 "replace": '<a href="/ty-gia/vietabank">VietABank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"VietBank",
#                 "replace": '<a href="/ty-gia/vietbank">VietBank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"VietCapitalBank",
#                 "replace": '<a href="/ty-gia/vietcapitalbank">VietCapitalBank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"Vietcombank",
#                 "replace": '<a href="/ty-gia/vietcombank">Vietcombank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"VietinBank",
#                 "replace": '<a href="/ty-gia/vietinbank">VietinBank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"VPBank",
#                 "replace": '<a href="/ty-gia/vpbank">VPBank</a>'
#                 },
#                 { 
#                 "path": "ngoaite"    ,   
#                 "remove":"VRB",
#                 "replace": '<a href="/ty-gia/vrbank">VRB</a>'
#                 },
#             ]
#             node=record_data[0]["table"]
#             for change in list_change:
#                 if change["path"]==path and (record_data[0]["name"] != "SJC hôm nay" or record_data[0]["name"] != "SJC 1 tháng" or record_data[0]["name"] != "SJC 1 năm"):
#                     node=node.replace(change["remove"],change["replace"])
#                 # elif change["path"]==path :
#                 #     node=node.replace(change["remove"],change["replace"])
                
#         # context={"request":request, "data": record_data[0]["table"], "father":record_data[0]["father"], "name":record_data[0]["name"], 'token': token}
#             return HTMLResponse(node)
#         else:
#             return HTMLResponse("token_error")
#     else:
#         list_change= [
#             ##tỷ giá
#             { 
#             "path": "tygia",
#             "remove":"USD",
#             "replace": '<a href="/ngoaite/usd">USD</a>'
#             },
#             { 
#             "path": "tygia",
#             "remove":"EUR",
#             "replace": '<a href="/ngoaite/eur">EUR</a>'
#             },
#             {
#             "path": "tygia" ,
#             "remove":"GBP",
#             "replace": '<a href="/ngoaite/gbp">GBP</a>'
#             },
#             { 
#             "path": "tygia" ,   
#             "remove":"HKD",
#             "replace": '<a href="/ngoaite/hkd">HKD</a>'
#             },
#             { 
#             "path": "tygia"   ,  
#             "remove":"CHF",
#             "replace": '<a href="/ngoaite/chf">CHF</a>'
#             },
#             { 
#             "path": "tygia"   ,
#             "remove":"JPY",
#             "replace": '<a href="/ngoaite/jpy">JPY</a>'
#             },
#             { 
#             "path": "tygia"  , 
#             "remove":"AUD",
#             "replace": '<a href="/ngoaite/aud">AUD</a>'
#             },
#             { 
#             "path": "tygia"   ,    
#             "remove":"SGD",
#             "replace": '<a href="/ngoaite/sgd">SGD</a>'
#             },
#             { 
#             "path": "tygia"    ,   
#             "remove":"THB",
#             "replace": '<a href="/ngoaite/thb">THB</a>'
#             },
#             { 
#             "path": "tygia"   ,    
#             "remove":"CAD",
#             "replace": '<a href="/ngoaite/cad">CAD</a>'
#             },
#             { 
#             "path": "tygia"   ,    
#             "remove":"NZD",
#             "replace": '<a href="/ngoaite/nzd">NZD</a>'
#             },
#             { 
#             "path": "tygia"   ,    
#             "remove":"KRW",
#             "replace": '<a href="/ngoaite/krw">KRW</a>'
#             },
#             { 
#             "path": "tygia"    ,   
#             "remove":"SEK",
#             "replace": '<a href="/ngoaite/sek">SEK</a>'
#             },
#             { 
#             "path": "tygia"    ,   
#             "remove":"TWD",
#             "replace": '<a href="/ngoaite/twd">TWD</a>'
#             },
#             { 
#             "path": "tygia"    ,   
#             "remove":"SAR",
#             "replace": '<a href="/ngoaite/sar">SAR</a>'
#             },
#             { 
#             "path": "tygia"    ,   
#             "remove":"RUB",
#             "replace": '<a href="/ngoaite/rub">RUB</a>'
#             },
#             { 
#             "path": "tygia"    ,   
#             "remove":"NOK",
#             "replace": '<a href="/ngoaite/nok">NOK</a>'
#             },
#             { 
#             "path": "tygia"    ,   
#             "remove":"MYR",
#             "replace": '<a href="/ngoaite/myr">MYR</a>'
#             },
#             { 
#             "path": "tygia"    ,   
#             "remove":"KWD",
#             "replace": '<a href="/ngoaite/kwd">KWD</a>'
#             },
#             { 
#             "path": "tygia"    ,   
#             "remove":"INR",
#             "replace": '<a href="/ngoaite/inr">INR</a>'
#             },
#             { 
#             "path": "tygia"    ,   
#             "remove":"CNY",
#             "replace": '<a href="/ngoaite/cny">CNY</a>'
#             },
#             { 
#             "path": "tygia"    ,   
#             "remove":"DKK",
#             "replace": '<a href="/ngoaite/dkk">DKK</a>'
#             },
#             ##giá vàng
#             { 
#             "path": ""    ,   
#             "remove":"SJC",
#             "replace": '<a href="/giavang/sjc">SJC</a>'
#             },
#             { 
#             "path": ""    ,   
#             "remove":"PNJ",
#             "replace": '<a href="/giavang/pnj">PNJ</a>'
#             },
#             { 
#             "path": ""    ,   
#             "remove":"Phú Quý",
#             "replace": '<a href="/giavang/phu-quy">Phú Quý</a>'
#             },
#             { 
#             "path": ""    ,   
#             "remove":"Mi Hồng",
#             "replace": '<a href="/giavang/mi-hong">Mi Hồng</a>'
#             },
#             { 
#             "path": ""    ,   
#             "remove":"Bảo Tín Minh Châu",
#             "replace": '<a href="/giavang/bao-tin-minh-chau">Bảo Tín Minh Châu</a>'
#             },
#             ##ngoại tệ
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"ABBank",
#             "replace": '<a href="/tygia/abbank">ABBank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"ACB",
#             "replace": '<a href="/tygia/acb">ACB</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"Agribank",
#             "replace": '<a href="/tygia/agribank">Agribank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"Bảo Việt",
#             "replace": '<a href="/tygia/bao-viet">Bảo Việt</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"BIDV",
#             "replace": '<a href="/tygia/bidv">BIDV</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"CBBank",
#             "replace": '<a href="/tygia/cbbank">CBBank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"Đông Á",
#             "replace": '<a href="/tygia/dong-a">Đông Á</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"Eximbank",
#             "replace": '<a href="/tygia/eximbank">Eximbank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"GPBank",
#             "replace": '<a href="/tygia/gpbank">GPBank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"HDBank",
#             "replace": '<a href="/tygia/hdbank">HDBank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"Hong Leong",
#             "replace": '<a href="/tygia/hong-leong">Hong Leong</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"HSBC",
#             "replace": '<a href="/tygia/hsbc">HSBC</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"Indovina",
#             "replace": '<a href="/tygia/indovina-bank">Indovina</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"Kiên Long",
#             "replace": '<a href="/tygia/kien-long">Kiên Long</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"Liên Việt",
#             "replace": '<a href="/tygia/lien-viet">Liên Việt</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"MB",
#             "replace": '<a href="/tygia/mbbank">MB</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"MSB",
#             "replace": '<a href="/tygia/mariatime-bank">MSB</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"Nam Á",
#             "replace": '<a href="/tygia/nam-a-bank">Nam Á</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"NCB",
#             "replace": '<a href="/tygia/ncb">NCB</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"OCB",
#             "replace": '<a href="/tygia/ocb">OCB</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"OceanBank",
#             "replace": '<a href="/tygia/oceanbank">OceanBank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"PGBank",
#             "replace": '<a href="/tygia/pgbank">PGBank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"PublicBank",
#             "replace": '<a href="/tygia/public-bank">PublicBank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"PVcomBank",
#             "replace": '<a href="/tygia/pvcombank">PVcomBank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"Sacombank",
#             "replace": '<a href="/tygia/sacombank">Sacombank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"Saigonbank",
#             "replace": '<a href="/tygia/saigonbank">Saigonbank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"SCB",
#             "replace": '<a href="/tygia/scb">SCB</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"SeABank",
#             "replace": '<a href="/tygia/seabank">SeABank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"SHB",
#             "replace": '<a href="/tygia/shb">SHB</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"Techcombank",
#             "replace": '<a href="/tygia/techcombank">Techcombank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"TPB",
#             "replace": '<a href="/tygia/tpbank">TPB</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"UOB",
#             "replace": '<a href="/tygia/uob">UOB</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"VIB",
#             "replace": '<a href="/tygia/vib">VIB</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"VietABank",
#             "replace": '<a href="/tygia/viet-a-bank">VietABank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"VietBank",
#             "replace": '<a href="/tygia/viet-bank">VietBank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"VietCapitalBank",
#             "replace": '<a href="/tygia/ban-viet">Bản Việt</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"Vietcombank",
#             "replace": '<a href="/tygia/vietcombank">Vietcombank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"VietinBank",
#             "replace": '<a href="/tygia/viettinbank">VietinBank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"VPBank",
#             "replace": '<a href="/tygia/vpbank">VPBank</a>'
#             },
#             { 
#             "path": "ngoaite"    ,   
#             "remove":"VRB",
#             "replace": '<a href="/tygia/vrbankank">VRB</a>'
#             },

#             #tiền ảo
#             { 
#             "path": "tienao"    ,   
#             "remove": "Bitcoin BTC",
#             "replace": '<a href="/tienao/btc">Bitcoin BTC</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Ethereum ETH",
#             "replace": '<a href="/tienao/eth">Ethereum ETH</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Tether USDT",
#             "replace": '<a href="/tienao/usdt">Tether USDT</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"BNB BNB",
#             "replace": '<a href="/tienao/bnb">BNB BNB</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"USD Coin USDC",
#             "replace": '<a href="/tienao/usdc">USD Coin USDC</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"XRP XRP",
#             "replace": '<a href="/tienao/xrp">XRP XRP</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Binance USD BUSD",
#             "replace": '<a href="/tienao/busd">Binance USD BUSD</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Cardano ADA",
#             "replace": '<a href="/tienao/ada">Cardano ADA</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Dogecoin DOGE",
#             "replace": '<a href="/tienao/doge">Dogecoin DOGE</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Polygon MATIC",
#             "replace": '<a href="/tienao/matic">Polygon MATIC</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Solana SOL",
#             "replace": '<a href="/tienao/sol">Solana SOL</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Polkadot DOT",
#             "replace": '<a href="/tienao/dot">Polkadot DOT</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Litecoin LTC",
#             "replace": '<a href="/tienao/ltc">Litecoin LTC</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Shiba Inu SHIB",
#             "replace": '<a href="/tienao/shib">Shiba Inu SHIB</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Avalanche AVAX",
#             "replace": '<a href="/tienao/avax">Avalanche AVAX</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Dai DAI",
#             "replace": '<a href="/tienao/dai">Dai DAI</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"TRON TRX",
#             "replace": '<a href="/tienao/trx">TRON TRX</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Uniswap UNI",
#             "replace": '<a href="/tienao/uni">Uniswap UNI</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove": "Wrapped Bitcoin WBTC",
#             "replace": '<a href="/tienao/wbtc">Wrapped Bitcoin WBTC</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Cosmos ATOM",
#             "replace": '<a href="/tienao/atom">Cosmos ATOM</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove": "Chainlink LINK",
#             "replace": '<a href="/tienao/link">	Chainlink LINK</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"UNUS SED LEO LEO",
#             "replace": '<a href="/tienao/leo">UNUS SED LEO LEO</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Monero XMR",
#             "replace": '<a href="/tienao/xmr">Monero XMR</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Ethereum Classic ETC",
#             "replace": '<a href="/tienao/etc">Ethereum Classic ETC</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Toncoin TON",
#             "replace": '<a href="/tienao/ton">Toncoin TON</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Aptos APT",
#             "replace": '<a href="/tienao/apt">Aptos APT</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Bitcoin Cash BCH",
#             "replace": '<a href="/tienao/bch">Bitcoin Cash BCH</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Stellar XLM",
#             "replace": '<a href="/tienao/xlm">Stellar XLM</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"OKB OKB",
#             "replace": '<a href="/tienao/okb">OKB OKB</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"ApeCoin APE",
#             "replace": '<a href="/tienao/ape">ApeCoin APE</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"NEAR Protocol NEAR",
#             "replace": '<a href="/tienao/near">NEAR Protocol NEAR</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Cronos CRO",
#             "replace": '<a href="/tienao/cro">Cronos CRO</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Filecoin FIL",
#             "replace": '<a href="/tienao/fil">Filecoin FIL</a>'
#             },

#             { 
#             "path": "tienao"    ,   
#             "remove":"Lido DAO LDO",
#             "replace": '<a href="/tienao/ldo">Lido DAO LDO</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Algorand ALGO",
#             "replace": '<a href="/tienao/algo">Algorand ALGO</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Quant QNT",
#             "replace": '<a href="/tienao/qnt">Quant QNT</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"VeChain VET",
#             "replace": '<a href="/tienao/vet">VeChain VET</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Hedera HBAR",
#             "replace": '<a href="/tienao/hbar">Hedera HBAR</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Internet Computer ICP",
#             "replace": '<a href="/tienao/icp">Internet Computer ICP</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Decentraland MANA",
#             "replace": '<a href="/tienao/mana">Decentraland MANA</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Fantom FTM",
#             "replace": '<a href="/tienao/ftm">Fantom FTM</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Aave AAVE",
#             "replace": '<a href="/tienao/aave">Aave AAVE</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"EOS EOS",
#             "replace": '<a href="/tienao/eos">EOS EOS</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Axie Infinity AXS",
#             "replace": '<a href="/tienao/axs">	Axie Infinity AXS</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"The Sandbox SAND",
#             "replace": '<a href="/tienao/sand">The Sandbox SAND</a>'
#             },

#             { 
#             "path": "tienao"    ,   
#             "remove":"MultiversX EGLD",
#             "replace": '<a href="/tienao/egld">MultiversX EGLD</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Theta Network THETA",
#             "replace": '<a href="/tienao/theta">Theta Network THETA</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Flow FLOW",
#             "replace": '<a href="/tienao/flow">Flow FLOW</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Tezos XTZ",
#             "replace": '<a href="/tienao/xtz">Tezos XTZ</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Terra Classic LUNC",
#             "replace": '<a href="/tienao/lunc">Terra Classic LUNC</a>'
#             },

#             { 
#             "path": "tienao"    ,   
#             "remove":"BitDAO BIT",
#             "replace": '<a href="/tienao/bit">BitDAO BIT</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"TrueUSD TUSD",
#             "replace": '<a href="/tienao/tusd">TrueUSD TUSD</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Chiliz CHZ",
#             "replace": '<a href="/tienao/chz">Chiliz CHZ</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Pax Dollar USDP",
#             "replace": '<a href="/tienao/usdp">Pax Dollar USDP</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove": "Bitcoin SV BSV",
#             "replace": '<a href="/tienao/bsv">Bitcoin SV BSV</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Huobi Token HT",
#             "replace": '<a href="/tienao/ht">Huobi Token HT</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"KuCoin Token KCS",
#             "replace": '<a href="/tienao/kcs">KuCoin Token KCS</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"The Graph GRT",
#             "replace": '<a href="/tienao/grt">The Graph GRT</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Frax Share FXS",
#             "replace": '<a href="/tienao/fxs">Frax Share FXS</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Zcash ZEC",
#             "replace": '<a href="/tienao/zec">Zcash ZEC</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"USDD USDD",
#             "replace": '<a href="/tienao/usdd">USDD USDD</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Curve DAO Token CRV",
#             "replace": '<a href="/tienao/crv">Curve DAO Token CRV</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"BitTorrent-New BTT",
#             "replace": '<a href="/tienao/btt">BitTorrent-New BTT</a>'
#             },

#             { 
#             "path": "tienao"    ,   
#             "remove":"Mina MINA",
#             "replace": '<a href="/tienao/mina">Mina MINA</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Trust Wallet Token TWT",
#             "replace": '<a href="/tienao/twt">Trust Wallet Token TWT</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Dash DASH",
#             "replace": '<a href="/tienao/dash">Dash DASH</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"eCash XEC",
#             "replace": '<a href="/tienao/xec">eCash XEC</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"PancakeSwap CAKE",
#             "replace": '<a href="/tienao/cake">PancakeSwap CAKE</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"IOTA MIOTA",
#             "replace": '<a href="/tienao/miota">IOTA MIOTA</a>'
#             },{ 
#             "path": "tienao"        ,   
#             "remove":"Maker MKR",
#             "replace": '<a href="/tienao/mkr">Maker MKR</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Klaytn KLAY",
#             "replace": '<a href="/tienao/klay">Klaytn KLAY</a>'
#             },

#             { 
#             "path": "tienao"    ,   
#             "remove":"Gemini Dollar GUSD",
#             "replace": '<a href="/tienao/gusd">Gemini Dollar GUSD</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"THORChain RUNE",
#             "replace": '<a href="/tienao/rune">THORChain RUNE</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Synthetix SNX",
#             "replace": '<a href="/tienao/snx">Synthetix SNX</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Neo NEO",
#             "replace": '<a href="/tienao/neo">Neo NEO</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"ImmutableX IMX",
#             "replace": '<a href="/tienao/imx">ImmutableX IMX</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"PAX Gold PAXG",
#             "replace": '<a href="/tienao/paxg">PAX Gold PAXG</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Optimism OP",
#             "replace": '<a href="/tienao/op">Optimism OP</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"GMX GMX",
#             "replace": '<a href="/tienao/gmx">GMX GMX</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Osmosis OSMO",
#             "replace": '<a href="/tienao/osmo">Osmosis OSMO</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"GateToken GT",
#             "replace": '<a href="/tienao/gt">GateToken GT</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Nexo NEXO",
#             "replace": '<a href="/tienao/nexo">Nexo NEXO</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Convex Finance CVX",
#             "replace": '<a href="/tienao/cvx">Convex Finance CVX</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Enjin Coin ENJ",
#             "replace": '<a href="/tienao/enj">Enjin Coin ENJ</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Loopring LRC",
#             "replace": '<a href="/tienao/lrc">Loopring LRC</a>'
#             },

#             { 
#             "path": "tienao"    ,   
#             "remove":"Zilliqa ZIL",
#             "replace": '<a href="/tienao/zil">Zilliqa ZIL</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Fei USD FEI",
#             "replace": '<a href="/tienao/fei">Fei USD FEI</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Terra LUNA",
#             "replace": '<a href="/tienao/luna">Terra LUNA</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"1inch Network 1INCH",
#             "replace": '<a href="/tienao/1inch">1inch Network 1INCH</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"EthereumPoW ETHW",
#             "replace": '<a href="/tienao/ethw">EthereumPoW ETHW</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Rocket Pool RPL",
#             "replace": '<a href="/tienao/rpl">Rocket Pool RPL</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Casper CSPR",
#             "replace": '<a href="/tienao/cspr">Casper CSPR</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Compound COMP",
#             "replace": '<a href="/tienao/comp">Compound COMP</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Gala GALA",
#             "replace": '<a href="/tienao/gala">Gala GALA</a>'
#             },

#             { 
#             "path": "tienao"    ,   
#             "remove":"Kava KAVA",
#             "replace": '<a href="/tienao/kava">Kava KAVA</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"dYdX DYDX",
#             "replace": '<a href="/tienao/dydx">dYdX DYDX</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Helium HNT",
#             "replace": '<a href="/tienao/hnt">Helium HNT</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Basic Attention Token BAT",
#             "replace": '<a href="/tienao/bat">Basic Attention Token BAT</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Stacks STX",
#             "replace": '<a href="/tienao/stx">Stacks STX</a>'
#             },
#             { 
#             "path": "tienao"    ,   
#             "remove":"Holo HOT",
#             "replace": '<a href="/tienao/hot">Holo HOT</a>'
#             },
           
#         ]
        
#         node=record_data[0]["table"]
#         for change in list_change:
#             if change["path"]==path and (record_data[0]["name"] != "SJC hôm nay" or record_data[0]["name"] != "SJC 1 tháng" or record_data[0]["name"] != "SJC 1 năm"):
#                 node=node.replace(change["remove"],change["replace"])
#         # print(record_data[0])
#         context={"request":request, "data": node, "father":record_data[0]["father"], "name":record_data[0]["name"], "data2":data2["meta_title"], "name_datas": record_data2, "path": path, "time":time}
#         return templates.TemplateResponse('content_iframe.html', context)
#     # return (templates.TemplateResponse("content.html",context))

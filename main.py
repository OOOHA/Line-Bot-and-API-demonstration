connNgrok() #ngrok connection
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage, MessageAction, TemplateSendMessage, CarouselTemplate,  CarouselColumn
)
from linebot.models import *
import requests, json, time, statistics

app = Flask(__name__)

line_bot_api = LineBotApi('Line bot channel access token')
access_token = 'Line bot channel access token'
channel_secret = 'Line bot channel secret'
code = 'Taiwan Central Weather Bureau API key'

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    try:
        line_bot_api = LineBotApi(access_token)
        handler = WebhookHandler(channel_secret)
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        json_data = json.loads(body)
        reply_token = json_data['events'][0]['replyToken']
        user_id = json_data['events'][0]['source']['userId']
        print(json_data)
        if 'message' in json_data['events'][0]:
            if json_data['events'][0]['message']['type'] == 'location':
                address = json_data['events'][0]['message']['address'].replace('台','臺')
                reply_message(f'{address}\n\n{current_weather(address)}\n\n{aqi(address)}\n\n{forecast(address)}', reply_token, access_token)
                print(address)
            if json_data['events'][0]['message']['type'] == 'text':
                text = json_data['events'][0]['message']['text']
                if text == '雷達回波圖' or text == '雷達回波':
                    reply_image(f'https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png?{time.time_ns()}', reply_token, access_token)
                elif text == '查看所有類型圖片':              
                    line_bot_api.push_message('U92d7cd8528f5cb95942ae2488bae2ce5', image_carousel_message1())
                elif text == '地震資訊' or text == '地震':              
                    msg = earth_quake()                               
                    push_message(msg[0], user_id, access_token)       
                    reply_image(msg[1], reply_token, access_token)    
                elif text == '海嘯資訊' or text == '海嘯':              
                    msg = tsunami()                               
                    push_message(msg[0], user_id, access_token)       
                elif text == '日出' or text =='日落' or text =='月球' or text =='月像' or text =='月出' or text =='月落':
                    line_bot_api.push_message('U92d7cd8528f5cb95942ae2488bae2ce5',Confirm_Template2())
                elif text == '天文' or text =='天文與潮汐':
                    line_bot_api.push_message('U92d7cd8528f5cb95942ae2488bae2ce5', Carousel_Template())
                elif text == '天氣' or text =='各地天氣' or text =='現在天氣' or text =='天氣預報':
                    line_bot_api.push_message('U92d7cd8528f5cb95942ae2488bae2ce5',buttons_message())
                elif text == '中央氣象局' or text =='中央氣象局網站' or text =='註冊會員' or text =='氣象局' or text =='中央氣象局官網' or text =='官網':
                    line_bot_api.push_message('U92d7cd8528f5cb95942ae2488bae2ce5',Confirm_Template())
                elif text == '中央氣象局在哪' or text =='中央氣象局位置' or text =='去中央氣象局' or text =='氣象局在哪' or text =='氣象局位置' or text =='去氣象局':
                    line_bot_api.push_message('U92d7cd8528f5cb95942ae2488bae2ce5',LocationSendMessage(
                                                                              title='中央氣象局',
                                                                              address='臺北市中正區公園路64號',
                                                                              latitude=25.037629514763825,
                                                                              longitude=121.51425606441754
                                                                            ))
                elif text == '標誌' or text =='氣象局標誌' or text =='中央氣象局標誌' or text =='局徽':
                      reply_message('以下為中央氣象局局徽，啟用自1993年(民國82年):', reply_token, access_token)
                      message = ImageSendMessage(
                          original_content_url= "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/ROC_Central_Weather_Bureau.svg/400px-ROC_Central_Weather_Bureau.svg.png",
                          preview_image_url= "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/ROC_Central_Weather_Bureau.svg/400px-ROC_Central_Weather_Bureau.svg.png"
                      )
                      line_bot_api.push_message('U92d7cd8528f5cb95942ae2488bae2ce5', message)
                elif text == '其他天氣網站推薦' or text =='天氣網站推薦' or text =='網站推薦' or text =='其他網站推薦' or text =='其他網站' or text =='推薦的網站':
                      print("天氣網站")
                elif text == '問卷' or text =='掰掰' or text =='問卷調查':
                      print("問卷")
                elif text == '你好棒' or text =='給我優惠卷' or text =='給我100分':
                      print("優惠卷")
                else:
                    reply_message('請使用下方命令', reply_token, access_token)
                    line_bot_api.push_message('U92d7cd8528f5cb95942ae2488bae2ce5', TemplateSendMessage(
                                                                                alt_text= text,
                                                                                    template=CarouselTemplate(
                                                                                        columns=[
                                                                                            CarouselColumn(
                                                                                                    title='圖片',
                                                                                                    text='查看雷達回波圖',
                                                                                                    actions=[
                                                                                                        MessageTemplateAction(
                                                                                                            label='點我看雷達回波圖',
                                                                                                            text='雷達回波圖'
                                                                                                        ),
                                                                                                        MessageTemplateAction(
                                                                                                            label='其他類型圖片',
                                                                                                            text='查看所有類型圖片'
                                                                                                        )
                                                                                                    ]
                                                                                                ),
                                                                                                CarouselColumn(
                                                                                                    title='天氣預報',
                                                                                                    text='查看天氣預報',
                                                                                                    actions=[
                                                                                                        MessageTemplateAction(
                                                                                                            label='點我看天氣預報',
                                                                                                            text='天氣預報'
                                                                                                        ),
                                                                                                        URITemplateAction(
                                                                                                            label='資料來源',
                                                                                                            uri='https://www.cwb.gov.tw/V8/C/'
                                                                                                        )
                                                                                                    ]
                                                                                                ),
                                                                                                CarouselColumn(
                                                                                                    title='天氣資訊',
                                                                                                    text='查看天氣資訊',
                                                                                                    actions=[
                                                                                                        MessageTemplateAction(
                                                                                                            label='現在天氣',
                                                                                                            text='現在天氣'
                                                                                                        ),
                                                                                                        URITemplateAction(
                                                                                                            label='資料來源',
                                                                                                            uri='https://www.cwb.gov.tw/V8/C/'
                                                                                                        )
                                                                                                    ]
                                                                                                ),
                                                                                                CarouselColumn(
                                                                                                    title='天文',
                                                                                                    text='查看太陽與月亮的資訊',
                                                                                                    actions=[
                                                                                                        URITemplateAction(
                                                                                                            label='查看日出時間',
                                                                                                            uri='https://www.cwb.gov.tw/V8/C/K/astronomy_day.html'
                                                                                                        ),
                                                                                                        URITemplateAction(
                                                                                                            label='查看月像',
                                                                                                            uri='https://www.cwb.gov.tw/V8/C/K/astronomy_day.html'
                                                                                                        )
                                                                                                    ]
                                                                                                ),
                                                                                                CarouselColumn(
                                                                                                    title='天災',
                                                                                                    text='查看地震與海嘯觀測',
                                                                                                    actions=[
                                                                                                        MessageTemplateAction(
                                                                                                            label='查看地震資訊',
                                                                                                            text='地震'
                                                                                                        ),
                                                                                                        MessageTemplateAction(
                                                                                                            label='查看海嘯資訊',
                                                                                                            text='海嘯'
                                                                                                        )
                                                                                                    ]
                                                                                                )
                                                                                        ]
                                                                                    )
                                                                        ))
    except:
        print('error')                       
    return 'OK'                              

if __name__ == "__main__":                       
  app.run()


def forecast(address):
    area_list = {}
    
    json_api = {"宜蘭縣":"F-D0047-001","桃園市":"F-D0047-005","新竹縣":"F-D0047-009","苗栗縣":"F-D0047-013",
            "彰化縣":"F-D0047-017","南投縣":"F-D0047-021","雲林縣":"F-D0047-025","嘉義縣":"F-D0047-029",
            "屏東縣":"F-D0047-033","臺東縣":"F-D0047-037","花蓮縣":"F-D0047-041","澎湖縣":"F-D0047-045",
            "基隆市":"F-D0047-049","新竹市":"F-D0047-053","嘉義市":"F-D0047-057","臺北市":"F-D0047-061",
            "高雄市":"F-D0047-065","新北市":"F-D0047-069","臺中市":"F-D0047-073","臺南市":"F-D0047-077",
            "連江縣":"F-D0047-081","金門縣":"F-D0047-085"}
    msg = '找不到天氣預報資訊。'    
    try:
        code = 'CWB-7F1D8D0C-CF39-4C72-BD85-74B38E085D49'
        url = f'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization={code}&downloadType=WEB&format=JSON'
        f_data = requests.get(url)   
        f_data_json = f_data.json()  
        location = f_data_json['cwbopendata']['dataset']['location']  
        for i in location:
            city = i['locationName']    
            wx8 = i['weatherElement'][0]['time'][0]['parameter']['parameterName']    
            mint8 = i['weatherElement'][1]['time'][0]['parameter']['parameterName']  
            maxt8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName']  
            ci8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName']    
            pop8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName']   
            area_list[city] = f'未來 8 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %'  
        for i in area_list:
            if i in address:        
                msg = area_list[i] 
                url = f'https://opendata.cwb.gov.tw/api/v1/rest/datastore/{json_api[i]}?Authorization={code}&elementName=WeatherDescription'
                f_data = requests.get(url)  
                f_data_json = f_data.json() 
                location = f_data_json['records']['locations'][0]['location']    
                break
        for i in location:
            city = i['locationName']   
            wd = i['weatherElement'][0]['time'][1]['elementValue'][0]['value']  
            if city in address:           
                msg = f'未來八小時天氣{wd}' 
                break
        return msg  
    except:
        return msg  

def aqi(address):
    city_list, site_list ={}, {}
    msg = '找不到空氣品質資訊。'
    try:
        url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=CWB-7F1D8D0C-CF39-4C72-BD85-74B38E085D49'
        a_data = requests.get(url)             
        a_data_json = a_data.json()            
        for i in a_data_json['records']:       
            city = i['County']                 
            if city not in city_list:
                city_list[city]=[]             
            site = i['SiteName']               
            aqi = int(i['AQI'])                
            status = i['Status']               
            site_list[site] = {'aqi':aqi, 'status':status}  
            city_list[city].append(aqi)        
        for i in city_list:
            if i in address:
                aqi_val = round(statistics.mean(city_list[i]),0)
                aqi_status = ''  
                if aqi_val<=50: aqi_status = '良好'
                elif aqi_val>50 and aqi_val<=100: aqi_status = '普通'
                elif aqi_val>100 and aqi_val<=150: aqi_status = '對敏感族群不健康'
                elif aqi_val>150 and aqi_val<=200: aqi_status = '對所有族群不健康'
                elif aqi_val>200 and aqi_val<=300: aqi_status = '非常不健康'
                else: aqi_status = '危害'
                msg = f'空氣品質{aqi_status} ( AQI {aqi_val} )。' 
                break
        for i in site_list:
            if i in address:  
                msg = f'空氣品質{site_list[i]["status"]} ( AQI {site_list[i]["aqi"]} )。'
                break
        return msg   
    except:
        return msg    

def current_weather(address):
    city_list, area_list, area_list2 = {}, {}, {} 
    msg = '找不到氣象資訊。'                         

    def get_data(url):
        w_data = requests.get(url)   
        w_data_json = w_data.json()  
        location = w_data_json['cwbopendata']['location']  
        for i in location:
            name = i['locationName']                       
            city = i['parameter'][0]['parameterValue']    
            area = i['parameter'][2]['parameterValue']     
            temp = check_data(i['weatherElement'][3]['elementValue']['value'])                       
            humd = check_data(round(float(i['weatherElement'][4]['elementValue']['value'] )*100 ,1)) 
            r24 = check_data(i['weatherElement'][6]['elementValue']['value'])                        
            if area not in area_list:
                area_list[area] = {'temp':temp, 'humd':humd, 'r24':r24}  
            if city not in city_list:
                city_list[city] = {'temp':[], 'humd':[], 'r24':[]}       
            city_list[city]['temp'].append(temp)   
            city_list[city]['humd'].append(humd)   
            city_list[city]['r24'].append(r24)     

    
    def check_data(e):
        return False if float(e)<0 else float(e)

   
    def msg_content(loc, msg):
        a = msg
        for i in loc:
            if i in address: 
                temp = f"氣溫 {loc[i]['temp']} 度，" if loc[i]['temp'] != False else ''
                humd = f"相對濕度 {loc[i]['humd']}%，" if loc[i]['humd'] != False else ''
                r24 = f"累積雨量 {loc[i]['r24']}mm" if loc[i]['r24'] != False else ''
                description = f'{temp}{humd}{r24}'.strip('，')
                a = f'{description}。' 
                break
        return a

    try:
        
        code = 'Taiwan Central Weather Bureau API key'
        get_data(f'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0001-001?Authorization={code}&downloadType=WEB&format=JSON')
        get_data(f'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0003-001?Authorization={code}&downloadType=WEB&format=JSON')

        for i in city_list:
            if i not in area_list2: 
                area_list2[i] = {'temp':round(statistics.mean(city_list[i]['temp']),1),
                                'humd':round(statistics.mean(city_list[i]['humd']),1),
                                'r24':round(statistics.mean(city_list[i]['r24']),1)
                                }
        msg = msg_content(area_list2, msg)  
        msg = msg_content(area_list, msg)   
        return msg    
    except:
        return msg    

def earth_quake():
    msg = ['找不到地震資訊','https://example.com/demo.jpg']            
    try:
        code = 'Taiwan Central Weather Bureau API key'
        url = f'https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization={code}'
        e_data = requests.get(url)                                   
        e_data_json = e_data.json()                                  
        eq = e_data_json['records']['earthquake']                    
        for i in eq:
            loc = i['earthquakeInfo']['epiCenter']['location']       
            val = i['earthquakeInfo']['magnitude']['magnitudeValue'] 
            dep = i['earthquakeInfo']['depth']['value']             
            eq_time = i['earthquakeInfo']['originTime']              
            img = i['reportImageURI']
            web = i['web']                                
            msg = [f'{loc}，芮氏規模 {val} 級，深度 {dep} 公里，發生時間 {eq_time}。更多資訊：{web}', img]
            break     
        return msg    
    except:
        return msg    

def tsunami():
    msg = ['找不到海嘯資訊','https://example.com/demo.jpg']       
    try:
        code = 'Taiwan Central Weather Bureau API key'
        url = f'https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0014-001?Authorization={code}'
        e_data = requests.get(url)                                   
        e_data_json = e_data.json()                                  
        eq = e_data_json['records']['tsunami']                    
        for i in eq:
            color = i['reportColor']
            loc = i['earthquakeInfo']['epiCenter']['location']       
            val = i['earthquakeInfo']['magnitude']['magnitudeValue'] 
            dep = i['earthquakeInfo']['depth']['value']              
            ts_time = i['earthquakeInfo']['originTime']                                             
            source = i['earthquakeInfo']['source']
            msg = [f'{loc} ， 海嘯等級顏色為：{color}， 海底地震{val}級 ， 深度{dep} 公里，發生時間 {ts_time}。  資料來源：{source}']
            break     
        return msg    
    except:
        return msg    


def push_message(msg, uid, token):
    headers = {'Authorization':f'Bearer {token}','Content-Type':'application/json'}   
    body = {
    'to':uid,
    'messages':[{
            "type": "text",
            "text": msg
        }]
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/push', headers=headers,data=json.dumps(body).encode('utf-8'))
    print(req.text)


def reply_message(msg, rk, token):
    headers = {'Authorization':f'Bearer {token}','Content-Type':'application/json'}
    body = {
    'replyToken':rk,
    'messages':[{
            "type": "text",
            "text": msg
        }]
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/reply', headers=headers,data=json.dumps(body).encode('utf-8'))
    print(req.text)


def reply_image(msg, rk, token):
    headers = {'Authorization':f'Bearer {token}','Content-Type':'application/json'}    
    body = {
    'replyToken':rk,
    'messages':[{
          'type': 'image',
          'originalContentUrl': msg,
          'previewImageUrl': msg
        }]
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/reply', headers=headers,data=json.dumps(body).encode('utf-8'))
    print(req.text)

def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='查看所有類型圖片',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url= f'https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-B0028-002.jpg?{time.time_ns()}',
                    action=URITemplateAction(
                        label="衛星雲圖",
                        uri="https://www.cwb.gov.tw/V8/C/W/OBS_Sat.html"
                    )
                ),
                ImageCarouselColumn(
                    image_url= f'https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png?{time.time_ns()}',
                    action=URITemplateAction(
                        label="雷達回波圖",
                        uri="https://www.cwb.gov.tw/V8/C/W/OBS_Radar.html"
                    )
                ),
                ImageCarouselColumn(
                    image_url= f"https://cwbopendata.s3.ap-northeast-1.amazonaws.com/DIV2/O-A0040-002.jpg?{time.time_ns()}",
                    action=URITemplateAction(
                        label="日累計雨量圖",
                        uri="https://www.cwb.gov.tw/V8/C/P/Rainfall/Rainfall_QZJ.html"
                    )
                ),
                ImageCarouselColumn(
                    image_url= f"https://cwbopendata.s3.ap-northeast-1.amazonaws.com/DIV2/O-A0038-001.jpg?{time.time_ns()}",
                    action=URITemplateAction(
                        label="溫度分布圖",
                        uri="https://www.cwb.gov.tw/V8/C/W/OBS_Temp.html"
                    )
                )
            ]
        )
    )
    return message

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='天文',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://images-assets.nasa.gov/image/PIA17669/PIA17669~small.jpg',
                    title='太陽',
                    text='日出日落資訊',
                    actions=[
                        URITemplateAction(
                            label='日出時間',
                            uri='https://www.cwb.gov.tw/V8/C/K/astronomy_day.html'
                        ),
                        URITemplateAction(
                            label='日落時間',
                            uri='https://www.cwb.gov.tw/V8/C/K/astronomy_day.html'
                        ),
                        URITemplateAction(
                            label='資料來源',
                            uri='https://www.cwb.gov.tw/V8/C/K/astronomy_day.html'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images-assets.nasa.gov/image/PIA00405/PIA00405~medium.jpg',
                    title='月球',
                    text='月相資訊',
                    actions=[
                        URITemplateAction(
                            label='今日月相',
                            uri='https://www.cwb.gov.tw/V8/C/K/astronomy_day.html'
                        ),
                        URITemplateAction(
                            label='月出月落時間',
                            uri='https://www.cwb.gov.tw/V8/C/K/astronomy_day.html'
                        ),
                        URITemplateAction(
                            label='資料來源',
                            uri='https://www.cwb.gov.tw/V8/C/K/astronomy_day.html'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://www.nasa.gov/sites/default/files/styles/full_width_feature/public/thumbnails/image/stsci-01gfnn3pwjmy4rqxkz585bc4qh.png',
                    title='太空',
                    text='天文資訊',
                    actions=[
                        URITemplateAction(
                            label='太空天氣',
                            uri='https://swoo.cwb.gov.tw/V2/'
                        ),
                        URITemplateAction(
                            label='太陽黑子',
                            uri='https://swoo.cwb.gov.tw/V2/page/Observation/Sunspot.html'
                        ),
                        URITemplateAction(
                            label='太空天氣問答',
                            uri='https://swoo.cwb.gov.tw/V2/page/Outreach/Questions.html'
                        )
                    ]
                )
            ]
        )
    )
    return message

def buttons_message():
    message = TemplateSendMessage(
        alt_text='選擇地點',
        template=ButtonsTemplate(
            thumbnail_image_url="https://cdn-icons-png.flaticon.com/512/854/854878.png",
            title="使用地圖",
            text="請使用地圖",
            actions=[
                LocationAction(
                    type ='location',
                    label="選擇位置"
                ),
                MessageTemplateAction(
                    label="取消",
                    text="其他功能"
                ),
                URITemplateAction(
                    label="前往中央氣象局網站",
                    uri = "https://www.cwb.gov.tw/V8/C/"
                )
            ]
        )
    )
    return message

def Confirm_Template():
    message = TemplateSendMessage(
        alt_text='是否前往中央氣象局網站？',
        template=ConfirmTemplate(
            text="是否前往中央氣象局網站？",
            actions=[
                URITemplateAction(
                    label="是",
                    uri = "https://www.cwb.gov.tw/V8/C/"
                ),
                MessageTemplateAction(
                    label="否",
                    text="使用其他功能"
                )
            ]
        )
    )
    return message

def Confirm_Template2():
    message = TemplateSendMessage(
        alt_text='前往中央氣象局網站查詢',
        template=ConfirmTemplate(
            text="是否前往中央氣象局天文網站查詢？",
            actions=[
                URITemplateAction(
                    label="是",
                    uri = "https://www.cwb.gov.tw/V8/C/K/astronomy_day.html"
                ),
                MessageTemplateAction(
                    label="否",
                    text="使用其他功能"
                )
            ]
        )
    )
    return message

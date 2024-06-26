import requests



#TODO:hero > image
def image_in_FlexMessage(url):
    return {"type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
            "size": "full",
            "aspect_ratio": "10:3",
            "aspect_mode": "cover",
            "action": {"type": "uri","uri": url}}

#TODO:text部分
def text_in_FlexMessage(text, flex, size, color, weight, wrap):
    return {"type": "text",
            "text": text,
            "flex": flex,
            "size": size,
            "color": color,
            "weight": weight,
            "wrap": wrap}

def title_in_FlexMessage(text):
    return text_in_FlexMessage(text, 1, "lg", "#2F4F4F", "bold", True)
#TODO:baseline
def baselinetitle_in_FlexMessage(text):
    return text_in_FlexMessage(text, 1, "md", "#D2691E", "bold", True)

def baselinecontext_in_FlexMessage(text):
    return text_in_FlexMessage(text, 6, "md", "#666666", "regular", True)

def baseline_content(title,context):
    return {"type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [baselinetitle_in_FlexMessage(title),baselinecontext_in_FlexMessage(context)]}
#TODO:BUTTON
def button_in_FlexMessage_postback(label, data, display_text):
    return {"type": "button",
            "action":{
                "type": "postback",
                "label": label,
                "data": data,
                "display_text": display_text
                },
            "style": "link",
            "color": "#066BAF",
            "height": "md"}

def button_in_FlexMessage_message(label,text):
    return {"type": "button",
            "action":{
                "type": "message",
                "label": label,
                "text": text
                },
            "style": "link",
            "adjustMode": "shrink-to-fit",
            "color": "#066BAF",
            "height": "sm"}



#TODO:主要Flex介面設定
#!指令說明部分
#查詢指令說明
def search_explain_FlexMessage():
    FlexMessage = { "type": "bubble",
                    "size": "giga",
                    "body": {   "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {"type": "text","text": "查詢指令說明:","size": "3xl","weight": "bold"},
                                {"type": "separator","margin": "md"},
                                {"type": "box","layout": "vertical","contents": [
                                    {"type": "text","text": "查詢指令:","size": "xxl","contents": []},
                                    {"type": "text","text": "一般範例如下(查:<地點名>)","size": "xl","weight": "bold","offsetStart": "xxl","color": "#0000ff"},
                                    {"type": "text","text": "查:PCDP1440","size": "xxl","align": "center"},
                                    {"type": "text","text": "查:泰隆新境","size": "xxl","align": "center"},
                                    {"type": "text","text": "查局名範例如下(查:PCTR局 or 查:樹林局)","weight": "bold","offsetStart": "xxl","color": "#0000ff"},
                                    {"type": "text","text": "查:PCGY局","size": "xxl","align": "center"},
                                    {"type": "text","text": "查:土城局","size": "xxl","align": "center"}]},
                                {"type": "box","layout": "vertical","contents": [
                                    {"type": "text","text": "若搜尋出匹配到多筆,會列出來請再點選你要查的即可","size": "sm","weight": "bold","color": "#006600"}]}]}}
    return FlexMessage


#修改指令說明
def update_explain_FlexMessage():
    FlexMessage = { "type": "bubble",
                    "size": "giga",
                    "body": {   "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {"type": "text","text": "修改指令說明:","size": "3xl","weight": "bold"},
                                {"type": "separator","margin": "md"},
                                {"type": "box","layout": "vertical","contents": [
                                    {"type": "text","text": "修改指令:","size": "xxl","color": "#ff0000","contents": []},
                                    {"type": "text","text": "範例如下","size": "xxl","weight": "bold","offsetStart": "xxl","color": "#0000ff"},
                                    {"type": "text","text": "(修改:<地點名>:<要修改項目>:<要修改成的內容>)","size": "sm","weight": "bold","align": "center","color": "#0000ff"},
                                    {"type": "text","text": "修改:御峰:地址:新北市三峽區xx路xx號","size": "lg","align": "center"},
                                    {"type": "text","text": "修改:PCTR1261:座標:25.0011384,121.425593","size": "md","align": "center"},
                                    {"type": "text","text": "修改:PCDP1440:走法:在168號車格旁","size": "lg","align": "center"},
                                    {"type": "text","text": "修改:泰隆新境:電源:AC","size": "xxl","align": "center"},
                                    {"type": "text","text": "修改:HE局:備註:無人局需借鑰匙","size": "xl","align": "center"}]},
				{"type": "separator","margin": "md"},
                                {"type": "box","layout": "vertical","contents": [
                                    {"type": "text","text": "新增指令:","size": "xxl","color": "#ff0000","contents": []},
                                    {"type": "text","text": "說明如下","size": "xxl","weight": "bold","offsetStart": "xxl","color": "#0000ff"},
                                    {"type": "text","text": "新增指令不會覆蓋原內容,會加入在原內容後","size": "md","align": "center"},
                                    {"type": "text","text": "範例如下","size": "xxl","weight": "bold","offsetStart": "xxl","color": "#0000ff"},
                                    {"type": "text","text": "假設PCDP1550的備註內容如下","size": "xl","align": "center"},
                                    {"type": "text","text": "備註:管理中心022262xxxx","size": "xl","align": "center"},
                                    {"type": "text","text": "格式(新增:<地點名>:<要新增資訊項目>:<要新增的內容>)","size": "xs","weight": "bold","align": "center","color": "#0000ff"},
                                    {"type": "text","text": "新增:PCDP1550:備註:需警衛室借鑰匙進入","size": "md","align": "center"},
                                    {"type": "text","text": "新增指令完後PCDP1550的備註會變成如下","size": "md","align": "center"},
                                    {"type": "text","text": "備註:管理中心022262xxxx需警衛室借鑰匙進入","size": "md","align": "center"},
                                    {"type": "text","text": "可看到會加在後面不會取代掉原先資訊","size": "md","align": "center"}]},
				{"type": "separator","margin": "md"},
                                {"type": "box","layout": "vertical","contents": [
                                    {"type": "text","text": "說明總結:","size": "xxl","color": "#ff0000","contents": []},
                                    {"type": "text","text": "修改指令會覆蓋原內容,但新增指令","size": "xl","weight": "bold","color": "#006600"},
                                    {"type": "text","text": "不會覆蓋原內容,會加入在原內容後","size": "xl","weight": "bold","color": "#006600"},
                                    {"type": "text","text": "指令的格式如下總結","size": "xl","weight": "bold","color": "#006600"},
                                    {"type": "text","text": "(修改:<地點名>:<要修改項目>:<要修改成的內容>)","size": "sm","weight": "bold","align": "center","color": "#0000ff"},
                                    {"type": "text","text": "(新增:<地點名>:<要新增資訊項目>:<要新增的內容>)","size": "sm","weight": "bold","align": "center","color": "#0000ff"}]}]}}
    return FlexMessage


#!操作指令部分
def address_search_FlexMessage(result):
    print(len(result))
    #?單筆查詢狀況
    if len(result) == 1:
        y = []
        for x in result[0]:
            if x == "":
                x = "*"
            y.append(x)
        result = y
        if result[2] != '@1218@':
            hero_image_url = "https://www.google.com.tw/maps/place/" + result[2].replace(" ","")
        else:
            api = "AIzaSyAzbIH-i1KVjLvspIB0cJT7Ni5GcUfY6Do"
            x = result[1].split(",")[0]
            hero_image_url = f"https://maps.googleapis.com/maps/api/geocode/json?key={api}&address={x}&sensor=false"
            hero_image_url = requests.get(hero_image_url)
            hero_image_url = hero_image_url.json()
            lat = str(hero_image_url["results"][0]["geometry"]["location"]["lat"])
            lng = str(hero_image_url["results"][0]["geometry"]["location"]["lng"])
            hero_image_url = "https://www.google.com.tw/maps/place/" + lat + "," + lng
        
        
        box_contents = {"type": "box",
                        "layout": "vertical",
                        "spacing": "md",
                        "contents": [baseline_content("地址:",result[1]),baseline_content("座標:",result[2]),baseline_content("走法:",result[3]),baseline_content("電源:",result[4]),baseline_content("備註:",result[5])]}


        body_contents = [title_in_FlexMessage(result[0]),
                        box_contents]

        footer_contents = []
        #footer_contents = [button_in_FlexMessage("修改", f"修改地點資訊:{result[0]}", "修改" + result[0] + "資訊")]

        FlexMessage = {"type": "bubble",
                    "hero": image_in_FlexMessage(hero_image_url),
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "md",
                        "contents": body_contents},
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": footer_contents}}
    #?多筆查詢狀況
    elif len(result) == 0:
        FlexMessage = {"type": "bubble",
                       "body": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "md",
                            "contents": [title_in_FlexMessage("查無該地點名")]}}
    else:
        footer_contents = []
        for x in result:
            footer_contents.append(button_in_FlexMessage_message(x[0],"查:" + x[0]))
        FlexMessage = {"type": "bubble",
                       "body": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "md",
                            "contents": [title_in_FlexMessage("搜尋到多筆資料如下:")]},
                       "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": footer_contents}}
    return FlexMessage


# def update_menu_FlexMessage(result):
#     footer_contents = [button_in_FlexMessage_postback("修改 地址", f"修改地點細項:{result}", "修改 " + result + " 地址"),
#                        button_in_FlexMessage_postback("修改 座標", f"修改地點細項:{result}", "修改 " + result + " 座標"),
#                        button_in_FlexMessage_postback("修改 走法", f"修改地點細項:{result}", "修改 " + result + " 走法"),
#                        button_in_FlexMessage_postback("修改 電源", f"修改地點細項:{result}", "修改 " + result + " 電源"),
#                        button_in_FlexMessage_postback("修改 備註", f"修改地點細項:{result}", "修改 " + result + " 備註")]


#     FlexMessage = {"type": "bubble",
#                    "hero": image_in_FlexMessage("https://www.google.com.tw/"),
#                    "body": {
#                        "type": "box",
#                        "layout": "vertical",
#                        "spacing": "md",
#                        "contents": [title_in_FlexMessage(result)]},
#                    "footer": {
#                        "type": "box",
#                        "layout": "vertical",
#                        "contents": footer_contents}}


    print(title_in_FlexMessage(result))
    return FlexMessage
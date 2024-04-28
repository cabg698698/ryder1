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
def address_search_FlexMessage(result):
    print(len(result))
    #?單筆查詢狀況
    if len(result) == 1:
        result = result[0]
        print(result)
        if (result[3] != ',') and (result[3] != '""'):
            hero_image_url = "https://www.google.com.tw/maps/place/" + result[3]
        else:
            api = "AIzaSyAzbIH-i1KVjLvspIB0cJT7Ni5GcUfY6Do"
            x = result[2].split(",")[0]
            hero_image_url = f"https://maps.googleapis.com/maps/api/geocode/json?key={api}&address={x}&sensor=false"
            hero_image_url = requests.get(hero_image_url)
            hero_image_url = hero_image_url.json()
            lat = str(hero_image_url["results"][0]["geometry"]["location"]["lat"])
            lng = str(hero_image_url["results"][0]["geometry"]["location"]["lng"])
            hero_image_url = "https://www.google.com.tw/maps/place/" + lat + "," + lng


        box_contents = {"type": "box",
                        "layout": "vertical",
                        "spacing": "md",
                        "contents": [baseline_content("地址:",result[2]),baseline_content("座標:",result[3]),baseline_content("走法:",result[4]),baseline_content("電源:",result[5])]}


        body_contents = [title_in_FlexMessage(result[1]),
                        box_contents]

        footer_contents = []
        #footer_contents = [button_in_FlexMessage("修改", f"修改地點資訊:{result[1]}", "修改" + result[1] + "資訊")]

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
    else:
        footer_contents = []
        for x in result:
            footer_contents.append(button_in_FlexMessage_message(x[1],"查 " + x[1]))
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
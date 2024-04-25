from app import line_bot_api
from linebot.models import RichMenu, RichMenuSize, RichMenuArea, RichMenuBounds,PostbackAction, URIAction
import os



RichMenu_main = RichMenu(size=RichMenuSize(width=2500, height=843),selected=False,name="Main_Tab",chat_bar_text="Main Settings",
                        areas=[RichMenuArea(bounds=RichMenuBounds(x=17, y=16, width=800, height=811),action=PostbackAction(label="查詢",display_text="查",data="主選單:查詢"))])



target_dir = "app/static/imgRichMenu/"
static_rich_menu_list = [(RichMenu_main, f"{target_dir}可用指令.png")]

def initialize_rich_menu(static_rich_menu_list=static_rich_menu_list):
    #取得使用中的圖文選單
    rich_menu_list = line_bot_api.get_rich_menu_list()

    #刪去舊的圖文選單
    for old_rich_menu in rich_menu_list:
        line_bot_api.delete_rich_menu(old_rich_menu.rich_menu_id)
    #建立新的圖文選單
    for rich_menu, image_path in static_rich_menu_list:
        rich_menu_id = line_bot_api.create_rich_menu(rich_menu)

        rich_menu_list = line_bot_api.get_rich_menu_list()
        print("------------------------")
        print(rich_menu_list)
        print("**********************************")
        print(rich_menu_id)
        # with open(image_path,"rb") as x:
        #     line_bot_api.set_rich_menu_image(rich_menu_id, "image/png", x)
    
    #指定預設圖文選單
    line_bot_api.set_default_rich_menu(rich_menu_id)



from app import handler
from app.custom_models import PhoebeTalks
from app.custom_models import PhoebeRichMenu
from linebot.models import MessageEvent,TextMessage,PostbackEvent



@handler.add(MessageEvent, message=TextMessage)
def reply_text(event):
    event.message.text = event.message.text.replace("：",":")
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        reply = False
        if not reply:
            print(event.message.text)
            if "查 " in event.message.text:
                reply = PhoebeTalks.search_record(event)#查詢資料
            if ("修改:" in event.message.text) or ("新增:" in event.message.text):
                reply = PhoebeTalks.update_record(event)#修改或新增資料
            if "增加資料:" in event.message.text:
                reply = PhoebeTalks.insert_record(event)#增加資料
            if "刪除資料" in event.message.text:
                reply = PhoebeTalks.delete_record(event)#刪除資料
            else:
                return False

@handler.add(PostbackEvent)
def handle_postback(event):
    print(event)
    PhoebeTalks.modify_address_i(event)

# PhoebeRichMenu.initialize_rich_menu()
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
            reply = PhoebeTalks.search_record(event)#查詢資料
        if not reply:
            reply = PhoebeTalks.update_record(event)#修改或新增資料
        if not reply:
            reply = PhoebeTalks.insert_record(event)#增加資料
        if not reply:
            reply = PhoebeTalks.delete_record(event)#刪除資料


@handler.add(PostbackEvent)
def handle_postback(event):
    print(event)
    PhoebeTalks.modify_address_i(event)

# PhoebeRichMenu.initialize_rich_menu()
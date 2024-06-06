from app import line_bot_api
from app.custom_models import utils, CallDatabase, PhoebeFlex
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, FlexSendMessage
from linebot.models import TemplateAction
import re

def search_record(event):
    try:
        record_list = utils.search_record(event.message.text)
        result = CallDatabase.search_record(record_list)
        output = PhoebeFlex.address_search_FlexMessage(result)
        print(output)
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="單一地點查詢", contents=output)
        )
        return True
    except:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="失敗了")
        )
        return True


def update_record(event):
    try:
        if event.message.text.count(":") == 3:
            record_list = utils.update_record(event.message.text)
            if record_list[2] == "錯誤":
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="想修改的項目輸入錯誤,請檢查是否為(地址,座標,走法,電源,備註)")
                )
            else:
                CallDatabase.update_record(record_list)
                result = CallDatabase.search_record(record_list[1])
                output = PhoebeFlex.address_search_FlexMessage(result)
                line_bot_api.reply_message(
                    event.reply_token,
                    FlexSendMessage(alt_text="單一地點查詢", contents=output)
                )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="修改輸入錯誤,範例如括弧所示(修改:PCTR9999:走法:B1右轉)")
            )
        return True
    except:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="失敗了")
        )
        return True


    # try:
    #     if "修改地點資訊" in event.message.text:
    #         record_list = utils.search_record(event.message.text)
    #         output = PhoebeFlex.update_search_FlexMessage(record_list)
    #         line_bot_api.reply_message(
    #             event.reply_token,
    #             FlexSendMessage(alt_text="單一地點查詢", contents=output)
    #         )
    #     else:
    #         record_list = utils.update_record(event.message.text)
    #         result = CallDatabase.update_record(record_list)
    #     return True
    # except:
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         TextSendMessage(text="失敗了")
    #     )
    #     return True


def insert_record(event):
    try:
        if re.split(":|：", event.message.text)[-1] == "@1218@":
            record_list = utils.insert_record(event.message.text)
            result = CallDatabase.insert_record(record_list)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=result)
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="新增地點密碼錯誤")
            )
        return True
    except:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="失敗了")
        )

        return True

def delete_record(event):
    try:
        if re.split(":|：", event.message.text)[-1] == "@1218@":
            record_list = utils.delete_record(event.message.text)
            result = CallDatabase.delete_record(record_list)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=result)
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="刪除地點密碼錯誤")
            )
        return True
    except:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="失敗了")
        )
        return True




def modify_address_i(event):
    query = event.postback.data
    judge = query.split(":")
    if judge[0] == "修改地點資訊":
        output = PhoebeFlex.update_menu_FlexMessage(judge[1])
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="單一地點查詢", contents=output)
        )


def search_explain(event):
    try:
        output = PhoebeFlex.search_explain_FlexMessage()
        print(output)
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="查詢指令說明", contents=output)
        )
        return True
    except:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="失敗了")
        )
        return True


def update_explain(event):
    try:
        output = PhoebeFlex.update_explain_FlexMessage()
        print(output)
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="修改指令說明", contents=output)
        )
        return True
    except:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="失敗了")
        )
        return True
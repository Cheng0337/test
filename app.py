from flask import Flask, request, abort
from linebot import (
LineBotApi, WebhookHandler
)
from linebot.exceptions import (
InvalidSignatureError
)
from linebot.models import (
MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)  
# 必須放上自己的Channel Access Token 
line_bot_api = LineBotApi('spkTeuGt8mnOnoIr24+CR8cvqjdD7k/mVmaG1sZNrtQNFjCM5GNbbCst/sd/miKJSmWTAPBtLBQIUwUWfdOSEP1VaDCLmZoVPSvI+1q3kFoW8FhmSTDW9ccslC8ngflvP0uUFzSSeQUryHAfog9HugdB04t89/1O/w1cDnyilFU=')  
# 必須放上自己的Channel Secret
handler = WebhookHandler('ee77d110aedac2da8f19381395006c7a')


line_bot_api.push_message('U649073284a65c59dd0f43a46c5614040    ', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request 
@app.route("/callback", methods=['POST']) 
def callback():     
    # get X-Line-Signature header value     
    signature = request.headers['X-Line-Signature']
    # get request body as text     
    body = request.get_data(as_text=True)     
    app.logger.info("Request body: " + body)      
    
    # handle webhook body     
    try:         
        handler.handle(body, signature)     
    except InvalidSignatureError:         
        abort(400)      
    return 'OK'


#訊息傳遞區塊 
##### 基本上程式編輯都在這個function ##### 
@handler.add(MessageEvent, message=TextMessage) 
def handle_message(event):     
    message = event.message.text     
    line_bot_api.reply_message(event.reply_token,TextSendMessage(message))

#主程式 
import os 
if __name__ == "__main__":    
    port = int(os.environ.get('PORT', 5000))     
    app.run(host='0.0.0.0', port=port)
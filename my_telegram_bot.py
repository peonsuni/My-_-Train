import telegram 
import time
telgm_token = '1500576267:AAGVQTUMVa-oVCvcpOr8VkZ_eZROh22Du58' 
bot = telegram.Bot(token = telgm_token)

prev_data=0
while True:
    updates = bot.getUpdates() 

    print('시작')

    for u in updates :
        print(u.message.text)


    data=u.message.text
    chat_id = u.message.chat.id
    
    #time.sleep(1)
    print("\n")
    print(data+"\n")
    
    if data=="end":
        break

    if prev_data != data :
        prev_data = data
        bot.send_message(chat_id,data)
        
print("bye")    
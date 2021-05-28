import constants as keys
from telegram.ext import*
import responses as R
import res1 as S
import requests,json 


print('Bot is starting')

def start_command(update, context):
    update.message.reply_text('Nomoskar/Hey!, Welcome to Assam Vaccine Tracker.Please provide your District id(To know Your district id write "/id") eg- 46:24-5-2021. No response mean no available slot.')

def vaccine_command(update, context):
    pin = '107'
    date = '11-5-2021'
    url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={pin}&date={date}'
    browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    print(url)
    response = requests.get(url, headers=browser_header)
    print(response)
    json_data = response.json()
    final_text = ''
    if len(json_data['sessions'])==0:
    	print("\nSlots Not Available\n")
    else:
    	for slots in json_data['sessions']:
    		final_text = final_text + "\nName: "+str(slots['name']) +'\n'+ "Available Capacity: "+str(slots['available_capacity']) +'\n' + "Min Age Limit: "+str(slots['min_age_limit']) +'\n' + "Vaccine: "+str(slots['vaccine'])+ '\n'
    		final_text = final_text + '----------------------------------------'
    update.message.reply_text(final_text)
    
def help_command(update, context):  
    update.message.reply_text('Hrishiraj')  

def handle_message(update, context):
    text = str(update.message.text).lower()
    user = update.effective_user
    #print(f'{user["username"]}: {text}')
    response = R.sample_responses(text)
    print(f'Bot: {response}')
    update.message.reply_text(response)
    


#def handle_text(update, context):
 #   text = str(update.message.text).lower()
  #  user = update.effective_user
   # #print(f'{user["username"]}: {text}')
    
   # response = R.sample_responses1(text)
    #print(f'Bot: {response}')
    #update.message.reply_text(response)

def error(update, context):
    print(f"Upadate {update} caused error {context.error}" )

def id_command(update, context):
    update.message.reply_text('district_id:46\ndistrict_name:Baksa\n\ndistrict_id:47\ndistrict_name:Barpeta\n\ndistrict_id:765\ndistrict_name:Biswanath\n\ndistrict_id:57\ndistrict_name:Bongaigaon\n\ndistrict_id:66\ndistrict_name:Cachar\n\ndistrict_id:766\ndistrict_name:Charaideo\n\ndistrict_id:58\ndistrict_name:Chirang\n\ndistrict_id:48\ndistrict_name:Darrang\n\ndistrict_id:62\ndistrict_name:Dhemaji\n\ndistrict_id:59\ndistrict_name:Dhubri\n\ndistrict_id:43\ndistrict_name:Dibrugarh\n\ndistrict_id:67\ndistrict_name:DimaHasao\n\ndistrict_id:60\ndistrict_name:Goalpara\n\ndistrict_id:53\ndistrict_name:Golaghat\n\ndistrict_id:68\ndistrict_name:Hailakandi\n\ndistrict_id:764\ndistrict_name:Hojai\n\ndistrict_id:54\ndistrict_name:Jorhat\n\ndistrict_id:49\ndistrict_name:KamrupMetropolitan\n\ndistrict_id:50\ndistrict_name:KamrupRural\n\ndistrict_id:51\ndistrict_name:Karbi-Anglong\n\ndistrict_id:69\ndistrict_name:Karimganj\n\ndistrict_id:61\ndistrict_name:Kokrajhar\n\ndistrict_id:63\ndistrict_name:Lakhimpur\n\ndistrict_id:767\ndistrict_name:Majuli\n\ndistrict_id:55\ndistrict_name:Morigaon\n\ndistrict_id:56\ndistrict_name:Nagaon\n\ndistrict_id:52\ndistrict_name:Nalbari\n\ndistrict_id:44\ndistrict_name:Sivasagar\n\ndistrict_id:64\ndistrict_name:Sonitpur\n\ndistrict_id:768\ndistrict_name:SouthSalmaraMankachar\n\ndistrict_id:45\ndistrict_name:Tinsukia\n\ndistrict_id:65\ndistrict_name:Udalguri\n\ndistrict_id:769\ndistrict_name:WestKarbiAnglong\n\n')

def main():
    updater = Updater(keys.API_KEY, use_context= True)
    dp= updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("owner", help_command))
    dp.add_handler(CommandHandler("id", id_command))
    dp.add_handler(CommandHandler("vaccine", vaccine_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    #dp.add_handler(MessageHandler(Filters.text, handle_text))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
main()

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk.events import AllSlotsReset
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['Delhi','New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']

def sendmail(Cuisine,City,Price,email):
	#TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & #(ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
	#if Price == 'Lesser than Rs. 300':  
#		TEMP = TEMP[(TEMP['Average Cost for two'] < 300)].sort_values(by=['Aggregate rating'],ascending = False)
#	elif Price == 'Rs. 300 to 700':  
#		TEMP = TEMP[(TEMP['Average Cost for two'] > 300) &  (TEMP['Average Cost for two'] <= #700)].sort_values(by=['Aggregate rating'],ascending = False)
	#elif Price == 'More than 700':  
	#	TEMP = TEMP[(TEMP['Average Cost for two'] > 700)].sort_values(by=['Aggregate rating'],ascending = False)
	TEMP = RestaurantSearch(City,Cuisine,Price)
	TEMP = TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']][:10]
	
	mail_content = TEMP.to_string(index = False)	
	sender_address = 'upgradpr@gmail.com'
	sender_pass = 'xxxxxxx'
	receiver_address = email	
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['Subject'] = 'List of Restaurant from Foodie'   	
	message.attach(MIMEText(mail_content, 'plain'))	
	session = smtplib.SMTP('smtp.gmail.com', 587) 
	session.starttls() 
	session.login(sender_address, sender_pass) 
	text = message.as_string()
	session.sendmail(sender_address, receiver_address, text)
	session.quit()
	print('Mail Sent to ', email)


def RestaurantSearch(City,Cuisine,Price):
	print(City,Cuisine,Price)
	
	TEMP = ZomatoData[(ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
	if len(TEMP) < 5:
		print('Restaurant Found :' , len(TEMP))
		return pd.DataFrame(columns = ['Restaurant Name','Address','Average Cost for two','Aggregate rating'])
	
	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
	if Price == 'Lesser than Rs. 300':	
		TEMP = TEMP[(TEMP['Average Cost for two'] < 300)].sort_values(by=['Aggregate rating'],ascending = False)
	elif Price == 'Rs. 300 to 700':	
		TEMP = TEMP[(TEMP['Average Cost for two'] > 300) &  (TEMP['Average Cost for two'] <= 700)].sort_values(by=['Aggregate rating'],ascending = False)
	elif Price == 'More than 700':	
		TEMP = TEMP[(TEMP['Average Cost for two'] > 700)].sort_values(by=['Aggregate rating'],ascending = False)
	
	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		#chk_loc = tracker.get_slot('check_resp')
		print('Inside run',loc,cuisine,price)		
		results = RestaurantSearch(City=loc,Cuisine=cuisine,Price=price)
		response=""
		if results.shape[0] == 0:
			response= "no results"
			res = False
		else:
			for restaurant in RestaurantSearch(loc,cuisine,price).iloc[:5].iterrows():
				restaurant = restaurant[1]
				response=response + F"{restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Aggregate rating']} with avg cost {restaurant['Average Cost for two']} Rs \n\n"
			res = True
		dispatcher.utter_message("-----"+response)
		return [SlotSet('check_email',res)]

class ActionConfirmEmail(Action):
	def name(self):
		return 'action_confirm_email'

	def run(self, dispatcher, tracker, domain):		
		email_confirmation = tracker.get_slot('email_confirmation')						
		print('email_confirmation', email_confirmation)		
		if email_confirmation == 'YES':							
			res = True
		else:
			res = False
		return [SlotSet('check_email',res)]
		
class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_loc'

	def run(self, dispatcher, tracker, domain):		
		loc = tracker.get_slot('location')		
		
		res = True
		if loc not in WeOperate:			
			print('Not Found', loc)			
			res = False			
		else:
			print('Found', loc)
		
		return [SlotSet('check_resp',res)]


class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):		
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		MailID = tracker.get_slot('email')		
		print(loc,cuisine,price,MailID)
		sendmail(cuisine,loc,price,MailID)	
		dispatcher.utter_message("Successfully sent mail to :"+MailID)		
		return [SlotSet('email',MailID)]
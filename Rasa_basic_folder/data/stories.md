## complete path 0
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}    
	- action_check_loc
	- slot{"check_resp":true} 
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}    
	- utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}    
    - action_search_restaurants
	- slot{"check_email":false}
	- utter_goodbye

## complete path 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}    
	- action_check_loc
	- slot{"check_resp":true} 
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}    
	- utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}    
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}
	- utter_email
* email_validator{"email": "upgradpr@gmail.com"}
	- action_send_mail
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}    
	- action_check_loc
	- slot{"check_resp":true} 
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}    
	- utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}    
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}	
    - utter_goodbye
    - export

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}    
	- action_check_loc
	- slot{"check_resp":false} 
    - utter_nonoperable_location
* restaurant_search{"cuisine": "chinese"}    
	- utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}    
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email  
* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}	
    - utter_email	
* email_validator{"email": "upgradpr@gmail.com"}
    - action_send_mail
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}    
	- action_check_loc
	- slot{"check_resp":false} 
    - utter_nonoperable_location
* restaurant_search{"cuisine": "chinese"}    
	- utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}    
    - action_search_restaurants
	- slot{"check_email":true}	
	- utter_ask_email  
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}		
    - utter_goodbye
    - export
	
## location specified 1
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}
	- utter_email
* email_validator{"email": "upgradpr@gmail.com"}
	- action_send_mail    
* affirm
    - utter_goodbye
    - export

## location specified 2
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}	    
    - utter_goodbye    

## location specified 3
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":false} 
    - utter_nonoperable_location
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}	
    - utter_email	
* email_validator{"email": "upgradpr@gmail.com"}
    - action_send_mail
    - utter_goodbye    

## location specified 4
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":false} 
    - utter_nonoperable_location
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}		
    - utter_goodbye

## complete path 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants    
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}
	- utter_email
* email_validator{"email": "upgradpr@gmail.com"}
	- action_send_mail
    - utter_goodbye        

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants    
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}	
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":false}	
    - utter_nonoperable_location
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants    
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}	
    - utter_email	
* email_validator{"email": "upgradpr@gmail.com"}
    - action_send_mail
    - utter_goodbye    
	
## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":false}	
    - utter_nonoperable_location
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants    
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}		
    - utter_goodbye

## complete path 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- action_check_loc
	- slot{"check_resp":true}	
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email
* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}
	- utter_email
* email_validator{"email": "upgradpr@gmail.com"}
	- action_send_mail    
* goodbye
    - utter_goodbye

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- action_check_loc
	- slot{"check_resp":true}	
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}	
    - utter_goodbye    
	
## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- action_check_loc
	- slot{"check_resp":false}	
	- utter_nonoperable_location
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}	
    - utter_email	
* email_validator{"email": "upgradpr@gmail.com"}
    - action_send_mail
    - utter_goodbye    
	
## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- action_check_loc
	- slot{"check_resp":false}	
	- utter_nonoperable_location
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}		
    - utter_goodbye

## complete path 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	

* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}
	- utter_email
* email_validator{"email": "upgradpr@gmail.com"}
	- action_send_mail
    - utter_goodbye
    - export



## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}	
    - utter_goodbye
    - export
	


## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":false}	
    - utter_nonoperable_location
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}	
    - utter_email	
* email_validator{"email": "upgradpr@gmail.com"}
    - action_send_mail
    - utter_goodbye    

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":false}	
    - utter_nonoperable_location
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}		
    - utter_goodbye

## interactive_story 1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_check_loc
	- slot{"check_resp":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}
	- utter_email
* email_validator{"email": "upgradpr@gmail.com"}
	- action_send_mail
* stop

## interactive_story 2
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_check_loc
	- slot{"check_resp":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email		
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}	
    - utter_goodbye    
* stop

## interactive_story 3
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_check_loc
	- slot{"check_resp":false}	
    - utter_nonoperable_location
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}	
    - utter_email	
* email_validator{"email": "upgradpr@gmail.com"}
    - action_send_mail
    - utter_goodbye    
* stop

## interactive_story 4
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_check_loc
	- slot{"check_resp":false}	
    - utter_nonoperable_location
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}		
    - utter_goodbye
* stop

## interactive_story 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_check_loc
	- slot{"check_resp":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}
	- utter_email
* email_validator{"email": "upgradpr@gmail.com"}
	- action_send_mail
    - utter_goodbye    

	
## interactive_story 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_check_loc
	- slot{"check_resp":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}	
    - utter_goodbye    

## interactive_story 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_check_loc
	- slot{"check_resp":false}	
    - utter_nonoperable_location
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}	
    - utter_email	
* email_validator{"email": "upgradpr@gmail.com"}
    - action_send_mail
    - utter_goodbye    
	
## interactive_story 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_check_loc
	- slot{"check_resp":false}	
    - utter_nonoperable_location
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}		
    - utter_goodbye

## interactive_story 1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi","price":"Lesser than Rs. 300"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":true}	
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	

* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}
	- utter_email
* email_validator{"email": "upgradpr@gmail.com"}
	- action_send_mail    
* affirm
    - utter_goodbye

## interactive_story 2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi","price":"Lesser than Rs. 300"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":true}	
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}	
    - utter_goodbye    
    
## interactive_story 3
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi","price":"Lesser than Rs. 300"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":false}	
	- utter_nonoperable_location
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}	
    - utter_email	
* email_validator{"email": "upgradpr@gmail.com"}
    - action_send_mail    
* affirm
    - utter_goodbye
	
## interactive_story 4
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi","price":"Lesser than Rs. 300"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":false}	
	- utter_nonoperable_location
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}		
    - utter_goodbye

	
## happy_path 1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai","price":"Lesser than Rs. 300"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
	- action_check_loc
	- slot{"check_resp":true}	
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	

* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}
	- utter_email
* email_validator{"email": "upgradpr@gmail.com"}
	- action_send_mail    
* affirm
    - utter_goodbye
	
## happy_path 2
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai","price":"Lesser than Rs. 300"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
	- action_check_loc
	- slot{"check_resp":true}	
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}	
    - utter_goodbye    

## happy_path 3
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai","price":"Lesser than Rs. 300"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
	- action_check_loc
	- slot{"check_resp":false}	
	- utter_nonoperable_location
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}	
    - utter_email	
* email_validator{"email": "upgradpr@gmail.com"}
    - action_send_mail        
* affirm
    - utter_goodbye
	
## happy_path 4
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai","price":"Lesser than Rs. 300"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
	- action_check_loc
	- slot{"check_resp":false}	
	- utter_nonoperable_location
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}		
    - utter_goodbye


## interactive_story 1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":true}	
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}	
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email

* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}
	- utter_email
* email_validator{"email": "upgradpr@gmail.com"}
	- action_send_mail
* affirm
    - utter_goodbye

## interactive_story 2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":true}	
	- utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}	
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}	
    - utter_goodbye
    

## interactive_story 3
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":false}	
	- utter_nonoperable_location
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}	
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}	
    - utter_email	
* email_validator{"email": "upgradpr@gmail.com"}
    - action_send_mail    
* affirm
    - utter_goodbye
	
## interactive_story 4
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":false}	
	- utter_nonoperable_location
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}	
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}		
    - utter_goodbye
	
## interactive_story 1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":true}	
    - utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}	
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	

* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}
	- utter_email
* email_validator{"email": "upgradpr@gmail.com"}
	- action_send_mail    
* affirm
    - utter_goodbye

## interactive_story 2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":true}	
    - utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}	
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}	
    - utter_goodbye    
    
## interactive_story 3
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":false}	
	- utter_nonoperable_location
    - utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}	
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "YES"}
    - action_confirm_email
	- slot{"check_email":true}	
    - utter_email	
* email_validator{"email": "upgradpr@gmail.com"}
    - action_send_mail    
* affirm
    - utter_goodbye
	
## interactive_story 4
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
	- action_check_loc
	- slot{"check_resp":false}	
	- utter_nonoperable_location
    - utter_ask_price	
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}	
    - action_search_restaurants
	- slot{"check_email":true}
	- utter_ask_email	
* email_confirmation_intent{"email_confirmation": "NO"}
    - action_confirm_email
	- slot{"check_email":false}		
    - utter_goodbye
## intent:affirm
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- hi
- hi
- hello
- hola

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- Looking out for some good [chinese](cuisine:chinese) restaurants in [chandigarh](location:Chandigarh)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate](price:mid) price range with [british](cuisine) food for [four](people:4) people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- [Chinese](cuisine:chinese)
- show me restaurants
- [mumbai](location)
- [Italian](cuisine)
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- [Dilli](location:Delhi)
- [Daily](location:Delhi)
- [Bengaluru](location:Bangalore)
- [bangalore](location:Bangalore)
- [Kolkata](location)
- [kolkata](location:Kolkata)
- [Calcutta](location:Kolkata)
- [Bombay](location:Mumbai)
- [Chennai](location)
- [Madras](location:Chennai)
- [Ahmedabad](location)
- [Ahmadabad](location:Ahmedabad)
- [Allahabad](location)
- [Prayag](location:Allahabad)
- [Prayagraj](location:Allahabad)
- [Ellahabad](location:Allahabad)
- [Coimbatore](location)
- [Kovai](location:Coimbatore)
- [Gurgaon](location)
- [Gurugram](location:Gurgaon)
- [Kochi](location)
- [koichi](location:Kochi)
- [Noida](location)
- [Gautambudh Nagar](location:Noida)
- [Puducherry](location)
- [Pondicherry](location:Puducherry)
- [Surat](location)
- [Suratha](location:Surat)
- [Vadodara](location)
- [Vadra](location:Vadodara)
- [Varanasi](location)
- [Banaras](location:Varanasi)
- [Chandigarh](location)
- [chandigarh](location:Chandigarh)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- [Lesser than Rs. 300](price)
- [Rs. 300 to 700](price)
- [More than 700](price)

## intent:email_confirmation_intent
- [YES](email_confirmation)
- [NO](email_confirmation)

## intent:email_validator
- [abc@gmail.com](email)
- [rupesh@yahoo.com](email)
- [pravin@outlook.com](email)
- Please send it to [xyz@sth.edu](email)
- [jddk.2jmd@kdl.co.in](email)
- Please send it to [ahbcdj@dkj.com](email)

## synonym:4
- four


## synonym:Delhi
- New Delhi


## synonym:bangalore
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## regex:email_validator
- ^[\\w.!#$%&'*+-=?^_`{|}~]+@[\\w]+[.][\\w]+[.]?[\\w]+$
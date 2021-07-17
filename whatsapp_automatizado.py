# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 00:33:23 2020

@author: luisn
"""

from twilio.rest import Client 
 
account_sid = 'ACf0089fb1bbd7a31ffa82483210108125' 
auth_token = '92b9e4e566524a392eee146d9c255d36' 
client = Client(account_sid, auth_token) 
def send_hellow ():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hola, soy el robot asistente de Luis.',
                              to='whatsapp:+34648279113') 
    print(message.sid)
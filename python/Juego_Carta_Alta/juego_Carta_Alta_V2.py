#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

salir= False

while(salir==False):
	
	jugador1=randint(2,14)
	jugador2=randint(2,14)
	
	palo=randint(1,4)
	
	if(palo==1):
		palo1= "Picas"
	
	if(palo==2):
		palo1= "Diamantes"

	if(palo==3):
		palo1= "Trebol"
	
	if(palo==4):
		palo1= "Corazones"
		
	palo=randint(1,4)
	
	if(palo==1):
		palo2= "Picas"
	
	if(palo==2):
		palo2= "Diamantes"

	if(palo==3):
		palo2= "Trebol"
	
	if(palo==4):
		palo2= "Corazones"
		
	if(jugador1==11):
			jugador1="J"
			
	if(jugador1==12):
			jugador1="Q"
		
	if(jugador1==13):
			jugador1="K"
				
	if(jugador1==14):
			jugador1="AS"
				
	if(jugador2==11):
			jugador2="J"
			
	if(jugador2==12):
			jugador2="Q"
			
	if(jugador2==13):
			jugador2="K"
				
	if(jugador2==14):
			jugador2="AS"
				
	if(jugador1==jugador2):
		
			print "¡Empate!"
			print "El jugador 1 tiene un", jugador1, "de", palo1
			print "EL jugador 2 tiene un", jugador2, "de", palo2
			print "HAS EMPATADO"
	else:
		if(jugador1 > jugador2):
		
			print "El jugador 1 tiene un", jugador1, "de", palo1
			print "EL jugador 2 tiene un", jugador2, "de", palo2
			print "¡Ha ganado el jugador 1!"
		else:	
			print "El jugador 1 tiene un", jugador1, "de", palo1
			print "EL jugador 2 tiene un", jugador2, "de", palo2
			print "¡Ha ganado el jugador 2!"
			
		salir=True

#Luke Ichpekov 

import pygame


pygame.init()


import random

#fonts {
myfont = pygame.font.SysFont("comicsansms", 30)
done_font = pygame.font.SysFont("comicsansms", 46)
start_font = pygame.font.SysFont("arial", 20)
text_button_start = pygame.font.SysFont("comicsansms", 14)
instruction = pygame.font.SysFont("comicsansms", 14)
telling = pygame.font.SysFont("comicsansms", 14)
again = pygame.font.SysFont("comicsansms", 18)
no = pygame.font.SysFont("comicsansms", 18)
#}


clock = pygame.time.Clock()

screen = pygame.display.set_mode((700,500))

pygame.display.set_caption(("Please give me 100% mr.Hutchison"))

#loading images{
bg = pygame.image.load("flap_back.png")

player = pygame.image.load("bird.png")

pole_bot = pygame.image.load("pole_bot.png")
pole_top = pygame.image.load("pole_top.png")
#}

#player stats{
player_x = 300
player_y = 225
player_vel = 5
#}


#pole stats{
pole_variation = 0
pole_gap = 90
pole_x = 700
pole_top_y = 0 - pole_gap 
pole_bot_y = 250 +  pole_gap 
pole_vel =5
#}



start_screen = True
game_over = False


score = 0


	


#blitting player and pole to the screen
def redraw() :

	screen.blit(bg, (0,0))	

	screen.blit(player , (player_x, player_y))	

	screen.blit(pole_top, (pole_x, pole_top_y - pole_variation))
	screen.blit(pole_bot, (pole_x, pole_bot_y - pole_variation))
	screen.blit(text, (0, 0))
	#screen.blit(text9, (300, 0))


	pygame.display.update()








#main game loop
run = True

clock.tick(60)

while run :


	for event in pygame.event.get() :

		if event.type == pygame.QUIT :

			run = False





	#all the text
	text = myfont.render("Score : " + str(score), 1, (0,0,0))

	text2 = done_font.render("GAME OVER, SCORE : " + str(score), 1, (255,0,0))

	text3 = start_font.render("WELCOME TO FLAPPY OGER", 1, (0,0,0))

	text4 = text_button_start.render("START", 1, (0,0,0))

	text5 = instruction.render("Press space to jump", 1, (0, 0, 0))

	text6 = telling.render("press start to begin", 1, (0, 0, 0))
	
	text7 = again.render("Play again", 1, (0, 0, 0))

	text8 = no.render("Quit", 1, (0, 0, 0))

	#text9 = high_score.render("Please give me 100%", 1, (0, 0, 0))
		
	#increasing score
	if pole_x == 250  :
		score += 1		

	#hit detection for the top
	if pole_x == player_x and player_y <= 50 + pole_gap - pole_variation :
		#player_y = 225
		game_over = True



	#hit detection for the bottom
	if pole_x == player_x and player_y >= 310 - pole_gap - pole_variation:
		#player_y = 0
		game_over = True



	#pole loop{
	pole_x -= pole_vel
	if pole_x <= 0 :
		pole_x = 700


	if pole_x == 700 :

		pole_variation = random.randint(-100,100)
		#}
		




	#hitting the floor
	if player_y >= 380 :
		game_over = True

		




	#input
	keys = pygame.key.get_pressed()  	
		

	if keys[pygame.K_SPACE] and player_y > 0:
		player_y -= player_vel

	elif player_y < 380 :
		player_y += 3

		#}









	#start screen loop
	while start_screen == True:

		pygame.draw.rect(screen, (255, 255, 255), (0,0,700,500))
		pygame.draw.rect(screen, (255, 0, 0), (325, 300, 50, 50))
		screen.blit(text3, (200,150))
		screen.blit(text4, (325, 310))
		screen.blit(text5, (270, 230))
		screen.blit(text6, (285, 420))
		
		
		for event in pygame.event.get() :

			if event.type == pygame.QUIT :
				pygame.quit()
			
			mouse = pygame.mouse.get_pos()

			if 375 > mouse[0] > 325 and 350 > mouse[1] > 300 and event.type == pygame.MOUSEBUTTONDOWN :
				start_screen = False
			
			pygame.display.update()



	
	#endgame loop
	while game_over == True :

		pygame.draw.rect(screen, (0,0,0), (0,0, 700, 500))		

		pygame.draw.rect(screen, (0,255,0), (200, 350, 85, 50))		

		pygame.draw.rect(screen, (255,0,0), (400,350, 50, 50))	

		screen.blit(text2, (100, 130))
		screen.blit(text7, (203, 357))
		screen.blit(text8, (405, 357))


		score = 0

		for event in pygame.event.get() :

			if event.type == pygame.QUIT :
				pygame.quit()
			
			mouse = pygame.mouse.get_pos()

			if 285 > mouse[0] > 200 and 400 > mouse[1] > 350 and event.type == pygame.MOUSEBUTTONDOWN :
				game_over = False

			if 450 > mouse[0] > 400 and 400 > mouse[1] > 350 and event.type == pygame.MOUSEBUTTONDOWN :
				pygame.quit()



		pole_x = 0

		player_y = 0

		pygame.display.update()

		



	redraw()

	






import random

def routine(Workout_type):
	"""This will return list of workouts for each type"""
	Workout = ""
	exe_list =  (['Barre', 'Cycling', 'Running', 'Abs'])
	Barre = (exe_list[0])
	Cycling = (exe_list[1])
	Running = (exe_list[2])
	Abs = (exe_list[3])

	if Workout_type == Barre:
		Barre = ["20 plies, 10 relives", "10 relives and 30 plies","10 grand plies and 30 relives"]
		Workout = random.choice(Barre) 
		
	elif Workout_type == Cycling:
		Cycling = ["30 minutes on the bike.", '15 minute bike ride.', ' 45 minutes bike ride switch intensity to level 2 half way']
		Workout = random.choice(Cycling)
	elif Workout_type == Running:
		Running = ["10 minute jog followed by 20 minute run.", '15 minute jog followed by 40 minute run', ' 10 minute jog followed by 50 minute run']
		Workout = random.choice(Running)
	elif Workout_type == Abs:
		Abs = ["10 crunches, 1 minute plank, 20 minute bycycle" , " 20 crunches, 2 minute plank, 20 byclycle kicks" , "30 crunches, 5 minute plank, 30 byclycle kicks"]
		Workout = random.choice(Abs)
	else: Workout = "Please try again."
	return Workout


print(f"Your Daily Workout")

repeat = True

while repeat:
	


	print(f"Hello, welcome to work out in 30 minutes a day.  Please choose your workout.")  
	userinput = input("Chose your workout: Barre, Cycling, Running, Abs\n")
	#workout = routine(workout_type)
	
	Workout_type = userinput
	Workout = routine(userinput)
	print (Workout)

	again = input("\nWould you like to do another workout? (y/n)?")
	if again =='n' :
		repeat = False
	print(f"Keep working towards your goal!  Goodbye.")

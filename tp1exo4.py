minutes_ecoulees = int(input("Entrez le nombre de minutes écoulées depuis le début du mois : "))

jour = (minutes_ecoulees // 60) // 24 
heure = (minutes_ecoulees // 60) % 24  
minute = minutes_ecoulees % 60  

print(f"La date associée est : Jour {jour}, Heure, {heure}, Minute:{minute}")

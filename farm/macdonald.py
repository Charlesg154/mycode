#!/usr/bin/env python3 
 
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]}, 
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]}, 
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}] 
 
produce = ["carrots","celery"] 
 
def main(): 
    locations = [] 
    for l in farms: 
        locations.append((l ["name"]).upper()) 
  
    choice = input(f"Choose a farm: {locations}\n>").upper() 
 
    if choice in locations: 
        print("Old MacDonald had a farm!  EE-YAI-EE-YAI-OO!") 
        for l in farms: 
            if l["name"].upper() == choice: 
                for animals in l["agriculture"]: 
                    if animals not in produce: 
                        print(f"And on that farm he had a {animals.capitalize().strip('s')}!  EE-YAI-EE-YAI-OO!") 
        print("Old MacDonald had a farm!  EE-YAI-EE-YAI-OO!")         
         
 
 
if __name__ == "__main__": 
    main() 

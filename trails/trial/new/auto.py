import pyautogui as auto
import time 

movie_list = [
    "  "
    "Iron Man 2008",
    "The Incredible Hulk 2008",
    "Iron Man 2 2010",
    "Thor 2011",
    "Captain America: The First Avenger 2011",
    "Marvel’s The First Avengers 2012",

   

    "Iron Man 3 2013",
    "Thor: The Dark World 2013",
    "Captain America: The Winter Soldier 2014",
    "Guardians of the Galaxy 2014",
    "Avengers: Age of Ultron 2015",
    "Ant-Man 2015",

    

    "Captain America: Civil War 2016",
    "Doctor Strange 2016",
    "Guardians of the Galaxy Vol. 2 2017",
    "Spider-Man: Homecoming 2017",
    "Thor: Ragnarok 2017",
    "Black Panther 2018",
    "Avengers: Infinity War 2018",
    "Ant-Man and the Wasp 2018",
    "Captain Marvel 2019",
    "Avengers: Endgame 2019",
    "Spider-Man: Far From Home 2019",

  

    "Black Widow 2021",
    "Shang-Chi and the Legend of the Ten Rings 2021",
    "Eternals 2021",
    "Spider-Man: No Way Home 2021",
    "Doctor Strange in the Multiverse of Madness 2021",
    "Thor: Love and Thunder 2022",
    "Black Panther: Wakanda Forever 2022",

 

    "Ant-Man and the Wasp: Quantumania 2023",
    "Guardians of the Galaxy Vol. 3 2023",
    "The Marvels 2023",
]

print(movie_list)


    

# Print the list of track names
for track in movie_list:


    auto.write(track)
    time.sleep(4)
    auto.press('enter')        
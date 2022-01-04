#dictionary
current_movies = {"Superman":"11:00AM",
                  "Batman":"1:00PM",
                  "Flash":"3:00PM",
                  "Godzilla":"5:00PM"}

print ("We're showing the following movies:")
for key in current_movies:
    print(key)

movie = input("What Movie would you like the showtime for ?\n")

showtime = current_movies.get(movie)
if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie, "is playing at " + showtime)
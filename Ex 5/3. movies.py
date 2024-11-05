class Movie:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def __str__(self):
        return f"{self.name} : {self.genre}"

class MovieList:
    def __init__(self, genre):
        self.movielist = []
        self.genre = genre

    def append(self, movie):
        if self.genre == movie.genre:
            self.movielist.append(movie)
        else:
            raise ValueError('Invalid genre')

    def __gt__(self, other):
        if len(self.movielist) > len(other.movielist):
            return self
        else:
            return other

    def __str__(self):
        return f"Movies in {self.genre}: {[str(movie) for movie in self.movielist]}"

if __name__ == "__main__":
    # Driver code
    movie1 = Movie("Movie1", "thriller")
    movie2 = Movie("Movie2", "comedy")
    movie3 = Movie("Movie3", "thriller")
    movie4 = Movie("Movie4", "comedy")
    
    print(movie1)
    print(movie2)
    print(movie3)
    print(movie4)

    thriller_list = MovieList("thriller")
    comedy_list = MovieList("comedy")

    thriller_list.append(movie1)
    comedy_list.append(movie2)
    thriller_list.append(movie3)
    comedy_list.append(movie4)
    
    print("the thriller movie list is: ", thriller_list)
    print("the comedy movie list is: ",comedy_list)

    larger_list = thriller_list > comedy_list
    print(larger_list)  # Output: "Movies in thriller: [Movie1 : thriller, Movie3 : thriller]"

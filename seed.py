import model
import csv

def load_users(session):
    input_file = open("seed_data/u.user")

    for line in input_file:
        line = line.rstrip()
        entry = line.split("|")
        id = int(entry[0])
        age = int(entry[1])
        gender = str(entry[2]) #unused because we are gender neutral 
        occupation = str(entry[3]) #unused on purpose
        zipcode = str(entry[4])

        user = model.User(id = id, age = age, zipcode = zipcode)
        session.add(user)
    session.commit()


def load_movies(session):
    input_file = open("seed_data/u.item")

    for line in input_file:
        line = line.rstrip()
        entry = line.split("|")
        id = int(entry[0])
        title = entry[1].split('(') #splitting date in parens off of title
        title = str(title[0]).decode("latin-1")
        release_date = entry[2]
        if not release_date:
            release_date = None
        else:
            release_date = model.datetime.datetime.strptime(release_date, '%d-%b-%Y')
        imdb_url = str(entry[4])

        movie = model.Movie(id = id, title = title, release_date = release_date, 
            imdb_url = imdb_url)
        session.add(movie)
    session.commit()

def load_ratings(session):
    input_file = open("seed_data/u.data")
    
    for line in input_file:
        line = line.rstrip()
        entry = line.split()
        user_id = int(entry[0])
        movie_id = int(entry[1])
        rating = int(entry[2])

        data = model.Data(user_id=user_id, movie_id=movie_id, rating=rating)
        session.add(data)
    session.commit()

def main(session):
    load_users(session)
    load_movies(session)
    load_ratings(session)

    
if __name__ == "__main__":
    s= model.connect()
    main(s)

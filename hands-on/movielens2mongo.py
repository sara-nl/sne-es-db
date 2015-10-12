#!/usr/bin/env python

import json

def parse_movie(line):
    mapping = ['title', 'release_date', 'video_release_date', 'imdb_url']
    genre_list = ["unknown", "Action", "Adventure", "Animation", "Children's",
            "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir",
            "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller",
            "War", "Western"]
    line = line.decode('latin-1').encode("utf-8")
    fields = line.strip().split('|', 23)
    key = fields[0]
    movie = dict(zip(mapping, fields[1:4]))
    del movie['video_release_date']
    movie['genres'] = [x[1] for x in zip(fields[5:], genre_list) if x[0] == '1']
    return (key, movie)

def parse_user(line):
    mapping = ['age', 'gender', 'occupation', 'zip']
    fields = line.strip().split('|', 5)
    key = fields[0]
    user = dict(zip(mapping, fields[1:]))
    user['age'] = int(user['age'])
    return (key, user)

def process_file(filename, parse_func):
    with open(filename, 'r') as f:
        d = {k: v for (k, v) in [parse_func(line) for line in f]}
        return d

def process_ratings(in_file, out_file, movies, users):
    mapping = ['user', 'movie', 'rating', 'timestamp']
    with open(in_file, 'r') as fin, open(out_file, 'w') as fout:
        for line in fin:
            fields = line.strip().split('\t', 4)
            rating = dict(zip(mapping, fields))
            rating['user'] = users[rating['user']]
            rating['movie'] = movies[ rating['movie']]
            rating['timestamp'] = int(rating['timestamp'])
            rating['rating'] = int(rating['rating'])
            fout.write(json.dumps(rating)+'\n')

if __name__ == '__main__':
    movies = process_file('u.item', parse_movie)
    users = process_file('u.user', parse_user)
    process_ratings('u.data', 'ratings.json', movies, users)

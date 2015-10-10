# SNE Essential Skills - DB guest lecture

## Assignment

### 1. Introduction

For this assignment, you can work in groups of two. 

You will be using the [MovieLens 100K Dataset][1-1], a dataset containing
100,000 movie ratings from the MovieLens website. You will create an
[entity-relationship model][1-2] for the data, load the dataset in a SQL-server
([PostgreSQL][1-3]) and a NoSQL document store ([MongoDB][1-4]) and perform
some queries on the database.
 
First, download the 100K dataset (don't forget to validate the download with
the checksum). You will only need the following files from the archive:

 - u.data
 - u.item
 - u.genre
 - u.user
 - u.occupation

[1-1]: http://grouplens.org/datasets/movielens/100k/
[1-2]: https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model
[1-3]: http://www.postgresql.org
[1-4]: https://www.mongodb.org

### 2. Entity-relationship model

Create a data model for this data set.  

### 3. PostgreSQL

#### 3.1 Installation

Install the PostgreSQL database on your machine.

#### 3.2 Loading the data

Load the data in the database according to the ER model. Some preprocessing of
the data might be needed.

#### 3.3 Simple queries

Write and perform SQL queries that answer the following questions:

 - What is the average rating for the movie 'Star Wars'?
 - What is the name and age of the user that has given the most ratings?

### 4. MongoDB

#### 4.1 Installation

Install MongoDB on your machine.

#### 4.2 Loading the data

Store the data in a single collection where every document contains a rating.
The user and movie information is stored in subdocuments. 

First convert the data to a single json file with this structure using your
favorite text processing tool (Python, Awk, etc.). If you don't know how to
approach this, use the following hint:

Ernq va gur h.hfre naq h.vgrz qngn naq fgber gurfr va gjb ybbxhc gnoyrf
(unfuznc, qvpgvbanel). Gura ernq gur h.qngn svyr naq hfr gur ybbxhc gnoyrf gb
bhgchg gur qrabeznyvmrq qngn.

If you are still stuck after this hint, use our Python `movielens2mongo.py`
program in this repository. 

#### 4.3 Simple queries

Repeat the queries from 3.3, but on the MongoDB database using its [own query
language][4-1].

[4-1]: http://docs.mongodb.org/manual/tutorial/query-documents/

### 5. Optional: more complex queries

If you want to practice some more advanced queries, try answering the following
questions:

 - What is the most controversial movie (has the highest variance in its
   ratings)?

### 6. Related material

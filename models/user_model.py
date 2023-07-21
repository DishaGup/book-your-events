from flask_pymongo import ObjectId

class User:
    collection = 'users'

    @classmethod
    def create(cls, user_data):
        from app import mongo
       
        user = {
            'username': user_data['username'],
            'user_status': user_data.get('user_status', True),
            'email': user_data['email'],
            'gender': user_data.get('gender', 'Other'),
            'membership_type': user_data.get('membership_type', 'Regular'),
            'bio': user_data.get('bio', ''),
            'date_of_birth': user_data.get('date_of_birth'),
            'location': user_data['location'],
            'role': user_data.get('role', 'user'),
             'password' :user_data.get('password')
        }
        return mongo.db[cls.collection].insert_one(user)

    @classmethod
    def get_all(cls):
        from app import mongo
        return list(mongo.db[cls.collection].find())

    @classmethod
    def get_by_username(cls, username):
        from app import mongo
        return mongo.db[cls.collection].find_one({'username': username})

    @classmethod
    def update(cls, username, updates):
        from app import mongo
        mongo.db[cls.collection].update_one({'username': username}, {'$set': updates})

    @classmethod
    def delete(cls, username):
        from app import mongo
        mongo.db[cls.collection].delete_one({'username': username})


class Movie:
    collection = 'movies'

    @classmethod
    def create(cls, movie_data):
        from app import mongo
        return mongo.db[cls.collection].insert_one(movie_data)

    @classmethod
    def get_all(cls):
        from app import mongo
        return list(mongo.db[cls.collection].find())

    @classmethod
    def get_by_title(cls, title):
        from app import mongo
        return mongo.db[cls.collection].find_one({'title': title})

    @classmethod
    def update(cls, title, updates):
        from app import mongo
        mongo.db[cls.collection].update_one({'title': title}, {'$set': updates})

    @classmethod
    def delete(cls, title):
        from app import mongo
        mongo.db[cls.collection].delete_one({'title': title})


class Show:
    collection = 'shows'

    @classmethod
    def create(cls, show_data):
        from app import mongo
        return mongo.db[cls.collection].insert_one(show_data)

    @classmethod
    def get_all(cls):
        from app import mongo
        return list(mongo.db[cls.collection].find())

    @classmethod
    def get_by_movie(cls, movie):
        from app import mongo
        return list(mongo.db[cls.collection].find({'movie': movie}))

    @classmethod
    def update(cls, show_id, updates):
        from app import mongo
        mongo.db[cls.collection].update_one({'_id': ObjectId(show_id)}, {'$set': updates})

    @classmethod
    def delete(cls, show_id):
        from app import mongo
        mongo.db[cls.collection].delete_one({'_id': ObjectId(show_id)})


class Event:
    collection = 'events'

    @classmethod
    def create(cls, event_data):
        from app import mongo
        return mongo.db[cls.collection].insert_one(event_data)

    @classmethod
    def get_all(cls):
        from app import mongo
        return list(mongo.db[cls.collection].find())

    @classmethod
    def get_by_name(cls, name):
        from app import mongo
        return mongo.db[cls.collection].find_one({'name': name})

    @classmethod
    def update(cls, event_id, updates):
        from app import mongo
        mongo.db[cls.collection].update_one({'_id': ObjectId(event_id)}, {'$set': updates})

    @classmethod
    def delete(cls, event_id):
        from app import mongo
        mongo.db[cls.collection].delete_one({'_id': ObjectId(event_id)})


class Participant:
    collection = 'participants'

    @classmethod
    def create(cls, participant_data):
        from app import mongo
        return mongo.db[cls.collection].insert_one(participant_data)

    @classmethod
    def get_all(cls):
        from app import mongo
        return list(mongo.db[cls.collection].find())

    @classmethod
    def get_by_name(cls, name):
        from app import mongo
        return mongo.db[cls.collection].find_one({'name': name})

    @classmethod
    def update(cls, participant_id, updates):
        from app import mongo
        mongo.db[cls.collection].update_one({'_id': ObjectId(participant_id)}, {'$set': updates})

    @classmethod
    def delete(cls, participant_id):
        from app import mongo
        mongo.db[cls.collection].delete_one({'_id': ObjectId(participant_id)})

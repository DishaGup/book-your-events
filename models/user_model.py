from bson import ObjectId

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



class Show:
    collection = 'shows'
   
    @classmethod

    def create(cls, show_data):
        from app import mongo
        # Extract the movie title from the show data
        result = mongo.db[cls.collection].insert_one(show_data)
        show_data['_id'] = result.inserted_id
        return show_data
    
    @classmethod
    def get_all(cls):
        from app import mongo
        return list(mongo.db[cls.collection].find())

    @classmethod
    def get_by_movie(cls, movie_id):
        from app import mongo
        return list(mongo.db[cls.collection].find({'movie': ObjectId(movie_id)}))

    @classmethod
    def update(cls, show_id, updates):
        from app import mongo
        mongo.db[cls.collection].update_one({'_id': ObjectId(show_id)}, {'$set': updates})

    @classmethod
    def delete(cls, show_id):
        from app import mongo
        mongo.db[cls.collection].delete_one({'_id': ObjectId(show_id)})


class Movie:
    collection = 'movies'
     
    @classmethod
    
    def create(cls, movie_data):
        from app import mongo
        result = mongo.db[cls.collection].insert_one(movie_data)
        return
        

    @classmethod
    def get_all(cls):
        from app import mongo
        return list(mongo.db[cls.collection].find())
    

    @classmethod
    def add_show(cls, movie_id, show_id):
        from app import mongo
        mongo.db[cls.collection].update_one(
            {'_id': ObjectId(movie_id)},
            {'$push': {'shows': ObjectId(show_id)}}
     )

    @classmethod
    def get_by_id(cls, event_id):
        from app import mongo
        return mongo.db[cls.collection].find_one({'_id': ObjectId(event_id)})

    @classmethod
    def get_by_title(cls, title):
        from app import mongo
        return mongo.db[cls.collection].find_one({'title': title})

    @classmethod
    def update(cls, movie_id, updates):
        from app import mongo
        mongo.db[cls.collection].update_one({'_id': ObjectId(movie_id)}, {'$set': updates})

    @classmethod
    def delete(cls, movie_id):
        from app import mongo
        mongo.db[cls.collection].delete_one({'_id': ObjectId(movie_id)})

class Event:
    collection = 'events'

    @classmethod
    def create(cls, event_data):
        from app import mongo

        # Create the event as usual
        event={
           "eventName" : event_data.get('eventName'),
           "eventDate" : event_data.get('eventDate'),
           "category" :event_data.get('category'),
           "venue" : event_data.get('venue'),
           "ticket_price" : event_data.get('ticket_price'),
           "location" : event_data.get('location'),
           "participants" : event_data.get('participants', []),
        }
        
       
        mongo.db[cls.collection].insert_one(event)
       # event.save()

        # Associate the event with participants, if any
        participants = event_data.get('participants', [])
        if participants:
            for participant in participants:
                participant_obj = Participant.objects(name=participant).first()
                if participant_obj:
                    participant_obj.add_event(event.id)
                else:
                    # If participant doesn't exist, create a new one and associate it with the event
                    participant_data = {
                        'name': participant,
                        # Add other participant data as needed...
                        'events': [event.id]
                    }
                    participant_obj = Participant(**participant_data)
                    participant_obj.save()

        return event
    
    @classmethod
    def get_all(cls):
        from app import mongo
        return list(mongo.db[cls.collection].find( {}, {'_id': True, 'eventName': True, 'eventDate': True, "category": True,'venue': True,
                                                         'ticket_price': True, 'location': True, "participants": True}))

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
    @classmethod
    def get_by_id(cls, event_id):
        from app import mongo
        return mongo.db[cls.collection].find_one({'_id': ObjectId(event_id)})

class Participant:
    collection = 'participants'

    @classmethod
    def create(cls, participant_data):
        from app import mongo
        result = mongo.db[cls.collection].insert_one(participant_data)
        # After inserting the participant, fetch and return the created document
        participant_data['_id'] = result.inserted_id
        return participant_data
    
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

    @classmethod
    def add_event(self, event_id):
        # Add the event to the events field of the Participant document
        self.events.append(event_id)
        
    @classmethod
    def book_show(cls, participant_id, show_id):
        from app import mongo
        mongo.db[cls.collection].update_one(
            {'_id': ObjectId(participant_id)},
            {'$push': {'booked_shows': show_id}}
        )
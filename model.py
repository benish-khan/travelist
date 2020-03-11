""" Models and database functions for TravelList Project. """

from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

######################################################################
# Model definitions

class User(db.Model):
    """User of TravelList website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        """ Provide helpful representation when printed. """

        return "<User: name={} => email={}>".format(self.name, self.email)

class UserTrip(db.Model):
    """ Common Table for User and Trip tables. """

    __tablename__ = "user_trips"

    user_trip_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.trip_id'))
    #Tie together UserTrip and User here. Use pk for Users which is user_id
    user = db.relationship("User",
                                backref=db.backref("users", order_by=user_id))
    #Tie together UserTrip and Trip here. Use pk for Trips which is trip_id
    trip = db.relationship("Trip",
                                backref=db.backref("trips", order_by=trip_id))

    def __repr__(self):
        """ Provide helpful representation when printed. """

        return "<UserTrip: user_id={} => trip_id={}>".format(self.user_id, self.trip)


class Trip(db.Model):
    """Trip on TravelList website."""

    __tablename__ = "trips"

    trip_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    city = db.Column(db.String(25), nullable=True)
    state = db.Column(db.String(25), nullable=True)
    #Tie together Trip and Activity here. Use pk for Trips which is trip_id
    activities = db.relationship("Activity",
                                backref=db.backref("trips"))


    def __repr__(self):
        """ Provide helpful representation when printed. """

        return "<Trip: trip_id={} city={} state={}>".format(self.trip_id,
                                                        self.city, self.state)


class Activity(db.Model):
    """ Activities during Trip on TravelList website."""

    __tablename__ = "activities"

    activity_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.trip_id'))
    category = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(250), nullable=True)


    def __repr__(self):
        """ Provide helpful representation when printed. """

        return "<Trip: trip_id={} activity_id={} category={} description={}>".format(self.trip_id,
                                                        self.activity_id, self.category, self.description)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///travellist'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

def example_data():
    """Create some sample data."""
#users table example data

    kanye = User(name='Kanye', email='kanye@gmail.com', password='test')
    djkhalid = User(name='DJ Khalid', email='dj@gmail.com', password='test')
    snoop = User(name='Snoop Dog', email='snoop@gmail.com', password='test')


    new_york = Trip(city='New York', state='New York') # Kanye's trip
    san_francisco = Trip(city='San Francisco', state='California') # DJ Khalid's trip
    oregon = Trip(city='Portland', state='Oregon') # Snoop Dog's trip

    db.session.add_all([new_york, san_francisco, oregon])
    db.session.flush()


    kanyes_trip = UserTrip(user=kanye, trip=new_york)
    dj_khalid = UserTrip(user=djkhalid, trip=san_francisco)
    snoop_dog = UserTrip(user=snoop, trip=oregon)

#activity table example data

    #new_york activities for Kanye
    ny_activity_one = Activity(trip_id=new_york.trip_id, category='Eat', description='Pizza in NYC')
    ny_activity_two = Activity(trip_id=new_york.trip_id, category='Buy', description='Whatever I want!')
    ny_activity_three = Activity(trip_id=new_york.trip_id, category='Visit', description='Statue of Liberty')

#san_francisco activities for DJ Khalid

    sf_activity_one = Activity(trip_id=san_francisco.trip_id, category='Eat', description='eat dumplings')
    sf_activity_two = Activity(trip_id=san_francisco.trip_id, category='Blay', description='play at Urban Putt')
    sf_activity_three = Activity(trip_id=san_francisco.trip_id, category='Visit', description='Visit SFMOMA')

#oregon_based_activities for Snoop Dog

    or_activity_one = Activity(trip_id=oregon.trip_id, category='Eat', description='eat at Le Pigeon')
    or_activity_two = Activity(trip_id=oregon.trip_id, category='Buy', description='visit and play Washington Park')
    or_activity_three = Activity(trip_id=oregon.trip_id, category='Visit', description='visit OMSI')

    db.session.add_all([kanye, djkhalid, snoop, ny_activity_one, ny_activity_two, ny_activity_three,
                         sf_activity_one, sf_activity_two, sf_activity_three, 
                         or_activity_one, or_activity_two, or_activity_three])
    
    db.session.commit()

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."


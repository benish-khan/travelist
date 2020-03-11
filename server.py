"""Travellist."""
from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, UserTrip, Trip, Activity


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/register', methods=['GET'])
def register_form():
    """Show form for user signup."""

    return render_template("register.html")
    # return redirect('/login')

@app.route('/register', methods=['POST'])
def register_process():
    """Process registration."""

    # taking user email and password from form
    user_email = request.form.get("email")
    user_password = request.form.get("password")
    user_name = request.form.get("name")

    # checking to see if user already exists in db.
    check_email = User.query.filter_by(email=user_email).first()
    #indexing into the form.

    if check_email:
        flash('Email already exists!')
        return redirect('/login')
        
    # if no user exists add to database.
    else:
        new_user = User(name=user_name, email=user_email, password=user_password) 
        #add user
        db.session.add(new_user)
        #commit this change
        db.session.commit()   

        flash("User {} added. Going forward please user your {} and password to login".format(user_name, user_email))
#should eventually be routed to /user page to create/view trips and activites
    # return render_template('user.html', user=new_user)
    return redirect('/login')

@app.route('/login', methods=['GET'])
def login_form():
        """Show login form."""
        return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_process():
    """Process login."""

    email = request.form["email"]
    password = request.form["password"]

    # Query for email address in db
    user = User.query.filter_by(email=email).first()
    # check_user_password = User.quesy.filter_by(password=user_password).first()

    if not user:
        flash("No account exists!")
        return redirect("/register")
  
    if user.password != password:
        flash("Incorrect credentials. Please try again.")
        return redirect("/login")

#create a session for this user.
    session["user_id"] = user.user_id
    #flash message to inform user they are logged in.
    flash("Successfully Logged In!")
    #once logged in, the user should be directed to their personal users page.
    return render_template("homepage.html", user=user)

@app.route('/trip-map', methods=['GET'])
def trips_map_view():
    """Shows map with markers for user's trip."""

    return render_template("trip-map.html")    

@app.route('/logout', methods=['GET'])
def logout():
    """Log user out of current session."""

    del session["user_id"]
    flash("Logged Out.")
    return render_template("logout.html")


@app.route('/user', methods=['GET'])
def view_trip():
    """View all trips for single user."""
    user_id = session.get("user_id")
    user_trips = UserTrip.query.filter_by(user_id=user_id).all()

    print user_trips
    print len(user_trips)
    trips = []
    for user_trip in user_trips:
        trips.append(user_trip.trip)

    print trips

    for item in trips:
        print "User trips listing: ", item

    if not user_id:
        return redirect("/login")
    else:
        return render_template("user.html", trips=trips)

@app.route('/trip-map-data', methods=['GET'])
def populate_map_iteratively():
    """Display trips on maps."""
    user_id = session.get("user_id")
    user_trips = UserTrip.query.filter_by(user_id=user_id).all()
    list_of_city_states = []
    for user_trip in user_trips:
        list_of_city_states.append((user_trip.trip.city + ", " + user_trip.trip.state))

    dict = {'locations': list_of_city_states}    

    return jsonify(dict)

    #ABOVE IS THE TRIP API route

@app.route('/user/<int:trip_id>', methods=['GET'])
def user_trip_detail_view(trip_id): 
    """Show unique trip activities."""

    activity_by_trip = Activity.query.filter_by(trip_id=trip_id).all()

    return render_template("activity.html", activities=activity_by_trip, trip_id=trip_id)  

@app.route('/activities/<int:trip_id>', methods=['POST'])
def user_trip_add_activity(trip_id):
    """Allow user to add activities for a unique trip."""
    
    user_id = session.get("user_id")
    user_trip_to_update = UserTrip.query.filter_by(trip_id=trip_id).first()
    print "This is the trip: ", user_trip_to_update

    if user_id and user_trip_to_update:

        if request.form:
            new_activity = Activity(category=request.form.get("category"), description=request.form.get("description"), trip_id=trip_id)
            db.session.add(new_activity)
            db.session.commit()
            flash('You have successfully added an activity to this trip.')
            print "Trip activity has been committed to db", new_activity

    return redirect("/user/"+str(trip_id)) 

@app.route('/activities/update/<int:trip_id>', methods=['POST'])
def user_trip_update_activity(trip_id):
    """Allow user to update an activity for a unique trip."""

    user_id = session.get("user_id")
    user_trip_to_update = UserTrip.query.filter_by(trip_id=trip_id).first()
    print "This is the trip: ", user_trip_to_update

    if user_id and user_trip_to_update:

        if request.form:
            print request.form.get("category")
            old_trip_activity_query = Activity.query.filter_by(category=request.form.get("category"), description=request.form.get("description")).first()
            print "This is the old activity via query: ", old_trip_activity_query
            old_trip_activity_query.category = (request.form.get("category"))
            print "This is the old category: ", old_trip_activity_query.category
            old_trip_activity_query.description = (request.form.get("description"))
            print "This is the old description: ", old_trip_activity_query.description
            new_activity = Activity(category=request.form.get("category"), description=request.form.get("description"), trip_id=trip_id)
            db.session.add(new_activity)
            db.session.commit()
            flash('You have successfully updated an activity for this trip.')
            print "Trip activity update has been committed to db", new_activity

    return redirect("/user/"+str(trip_id)) 

@app.route('/activities/delete/<int:trip_id>', methods=['POST'])
def user_trip_delete_activity(trip_id):
    """Allow user to delete an activity for a unique trip."""

    user_id = session.get("user_id")
    user_trip_to_update = UserTrip.query.filter_by(trip_id=trip_id).first()
    print "This is the trip: ", user_trip_to_update

    if user_id and user_trip_to_update:

        if request.form:
            old_trip_activity_query = Activity.query.filter_by(category=request.form.get("category"), description=request.form.get("description")).first()
            print "This is the activity to delete via query: ", old_trip_activity_query
            old_trip_activity_query.category = (request.form.get("category"))
            print "This is the old category: ", old_trip_activity_query.category
            old_trip_activity_query.description = (request.form.get("description"))
            print "This is the old description: ", old_trip_activity_query.description
            
            db.session.delete(old_trip_activity_query.category)
            db.session.delete(old_trip_activity_query.description)

            db.session.commit()
            flash('You have successfully deleted an activity for this trip.')
            print "Trip activity update has been committed to db", old_trip_activity_query.category, old_trip_activity_query.description

    return redirect("/user/"+str(trip_id))     
    

@app.route('/add-trip', methods=['GET'])
def add_trip_page_view():
    """Fetches the page for user to add trip.""" 

    return render_template('add-trip.html') 
        

@app.route('/add-trip', methods=['POST'])
def add_trip():
    """Add a trip."""

    if request.form:
        city = request.form.get("city")
        state = request.form.get("state")
        print city
        print state
        new_trip = Trip(city=city, state=state)
        db.session.add(new_trip)
        db.session.flush()
        user = User.query.get(session["user_id"])
        user_trip = UserTrip(user_id=user.user_id, trip_id=new_trip.trip_id)
        
        db.session.add(user_trip)

        db.session.commit()
        # print "Trip has been committed to db", new_trip
        # flash("Trip has been committed to db!")

    return jsonify({"state":state, "city": city}, trip_id=trip_id)

@app.route('/update-trip', methods=['GET']) #need to walk through this function with Katie!
def update_trip_page_view():
    """Fetches the page for user to update trip.""" 
    return render_template('update-trip.html')     

@app.route('/update-trip', methods=['POST']) # NEED HELP WITH THIS ONE!!!***
def update_trip():
    """Search for existing trip to update."""
#make sure for multiple users that you put in logic to handle that user must be associated to the specific trip.id.

    if request.form:
    #for the user in this session we would like to update trip
        user = User.query.get(session["user_id"])
        print "THIS IS THE USER WHOSE TRIP WE WANT TO UPDATE: ", user
    #getting the data from form
    #     # update_trip = Trip(city=request.form.get("city"), state=request.form.get("state"))
    # #printing the values to see what is being given by form
    #     print "Values to update old trip with: ", update_trip
    #Trip query by city and state
        old_trip_query = Trip.query.filter_by(city=request.form.get("city"), state=request.form.get("state")).first()
    #printing to confirm what is returned in this query is expected. Also that the trip exists for user to update.
        print " This is the old trip via query: ", old_trip_query
    #setting old trip city value to new value
        old_trip_query.city = (request.form.get("new_city"))
        print "What is being updated for the new_city value: ", old_trip_query.city
    #setting old trip state value to new value
        old_trip_query.state = (request.form.get("new_state"))
        print "What is being updated for the new_state value: ", old_trip_query.state
    #setting commit function here to move forward with update to db.
        db.session.commit()
        
        return redirect("/user")

    return render_template("update-trip.html", old_trip_query=old_trip_query, update_trip=update_trip)   


@app.route('/delete-trip', methods=['GET'])
def delete_page_view():
    """Fetches the page for user to delete trip.""" 
    return render_template('delete-trip.html') 
        

@app.route('/delete-trip', methods=['POST'])
def delete_trip():
    """Delete a trip."""
    if request.form:
        trip_lookup = Trip.query.filter_by(city=request.form.get("city"), state=request.form.get("state")).first()

        user = User.query.get(session["user_id"])

        user_trip_middle = UserTrip.query.filter_by(user_id=user.user_id, trip_id=trip_lookup.trip_id).delete()
        db.session.commit()

        user_trip_main = Trip.query.filter_by(trip_id=trip_lookup.trip_id).delete()
        db.session.commit()

        

    return render_template("delete-trip.html", trip_lookup=trip_lookup) 



     
                  
if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug
    connect_to_db(app)
    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.run(port=5000, host='0.0.0.0')                

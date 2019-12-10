# Squirrel_Tracker
  
![Track Squirrels]("https://www.mentalfloss.com/article/586488/squirrel-census-counts-2373-squirrels-in-central-park")

## Track Squirrels with Ease!
Squirel Tracker is a web application to keep track of all the known squirrels within The Central Park in New york. The application is based on 2018 Central Park Squirrel Census data and the users 
can add, update, and view squirrel data.
## Data Source
Users can import the 2018 Central Park Squirrel Census data by using the command:
`python manage.py import_squirrel_data /path/to/file.csv`
Also, users can export the data in csv format with this command:
`python manage.py export_squirrel_data /path/to/file.csv`
## Functions
Map (App - 1)
url: /map
The map displays the location of squirrel sightings. You can see locations of around 1000 squirrels on the map.
Sightings (App - 2)
url: /sightings
Lists all squirrel sightings with data about each sightings and  links to edit each sighting.
Updation
url: sightings/<unique_squirrel_id>
To view, edit and update a particular squirrel sighting.
Adding a new Squirrel
url: sightings/add
Creates a new squirrel sighting. This gives the user an option to add specific details like location, actions and other squirrel charachteristics.
Stats
url: sightings/stats
Show general stats(Primary Fur Color, Shifts, Location) about the sightings
### Group Information
Project Group 41, Section 2
Uni = [ok2294, msb2231]
### Link To App

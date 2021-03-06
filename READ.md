#About the project

This app is a 3-tier music browser and player. By using Django’s built-in database features I was able to implement organization on the model structure of artist -> album -> song. 

During the creation of The Music Explorer, I intended to store a small amount of audio files in the app project folder to demonstrate a proof of concept for managing non-text data but this turned out to be too cumbersome for the Heroku deployment server. In lieu of not being able to store actual music, I opted for simulating this function with embedded Spotify URLs. Although the audio files themselves are not stored in the database, all of the other expected functionality of a music organizer is present here. Music can also be added/removed to the database using the admin interface, and instructions for this feature can be found on the “manage music” page.

https://module7-music-site.herokuapp.com/
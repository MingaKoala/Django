# Documentation

  
this documentation is about the Django project that we both did. Srdjan was increasingly in the frontend area and Benedikt took over the backend. The idea was to create a simple poll page which then displays the results.




## Procedure

The first thing to do was to install Django on Windows. After this was completed and Python still works in VS code, we were able to start our project.



It started with:

-   creating the polls and choice in the admin area
	> with the command http://127.0.0.1:8000/admin/ you can login
-   Then the views were created
- URLs
- Migrations
- Models 
- Migrate
- Some Functions
- Messages
- and CSS

## Functions
  
We have a few different options:
- at **What is your favorite programming language?** you have already voted and once you have voted it is no longer possible to vote for it again. But you can still see the result
- At **How old are you?** no answer options were given in the admin area and this is also displayed accordingly
- at **Which season do you like the most?** There are different answer options if you don't select one and press the button, an error message appears that indicates that you have to select something. If you have done this, you will be forwarded to the current result.
- at **Color** the survey has already expired. The polls are saved when they are created and expire after 7 days. If they have expired, they appear in **completed polls** where you can then only see the result

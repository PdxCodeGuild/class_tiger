Project Overview:
    RunawayNext is a social media site that allows users to mark the places they have been on a map so that other users can see and ask specific questions about those locations for their next trip. This would mean that users will be able to create their own profiles that have individualized maps. Those that view the profiles will be able to comment on those places listed in order to gain first-hand information for a potential upcoming trip. Ideally, the user will be able to add a brief description of the place that would pop up when a pin is selected. This is what will show up on the home page for people to scroll through as locations are added. It would be a fairly basic set up using Django, Javascript, HTML and probably a REST API with Django for the map. I also prefer to do my own styling with CSS.

User Stories:
    As a user, I want to be able to show places I've visited and a few things I did (or maybe didn't) enjoy while I was there. I also want to be able to ask questions to those that have been to a place that I would like to visit. 


Features:
    The home page will list newly added locations plus their descriptions and the user that shared it; Other users will also be able to comment here.

    The profile will be the users individualized maps. Comments will also be allowed here.

    A log in page will also be necessary for users to create their own maps.

Data Model:
    I will need several models for this project: Users, Posts(username, date_posted, date_updated, post_text), Maps(location, pin, posts, add). Most of my Models will be one to one, although the maps on user profiles will be one to many. 

Schedule:
    I would like to set aside at least the first week to get the map portion of the project working. 
        6/10 - 6/11 find the api and figure out how to work with it/write the appropriate code.

        6/12 and 6/13 to figure out how to add pins to locations with pop ups.

        6/14-6/15 figure out how to set up the map to only be edited when called. 

    The next week would be to add features similar to other social media sites while implementing the maps.
        6/18 - 6/19 start working on a homepage that will list updates to maps (Not the maps themselves), showing usernames, the newly added location, and the update itself, plus date and times the change was posted/edited. 

        6/20 set up log in info and connect that to profiles. Make sure things cannot be edited or deleted unless that specific user is the one logged in. 

        6/21-6/24 begin work on profiles. I would like to keep this simple at first, focusing on getting maps set up. The username would be displayed, perhaps some quick info (current residence, very brief "tagline" bios), and allow for comments on the page. 

    I hope that the final week will be for catch up and styling.
        6/25 add styling to page so that it may be easier to see how everything interacts.

        6/26-6/28 fix glitches and anything that I may not have thought of in planning. If all seems to be going well start working on adding more features, such as images, although that is not a main focus of mine for presentations

MVP:
    At the very least I would like to have users be able to log in and add locations to their own map with a short description of their time there. My next step is to have a home page with those descriptions that appear when added. After that comments would be important because the whole idea behind the site isn't to brag about where the user has been but to give advice on what there is to do in a place. This is what I would like to complete for the presentation, but after that I would like to add images if possible. It would also be nice to add a search option for both usernames and locations. 




        

    






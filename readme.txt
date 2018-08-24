Name: Jimmy Chan

What are the highlights of your logic/code writing style?

The programming language that is used to develop this application in Python
I used threading and concurrency method to develop this problem solution.
I constructed a function called TheBrewerySensor ():
This function contains a loop that loops through 5 if and elif statements for each beer situation, with their specific allocated temperature set
The used of loops, threading and concurrency methods let the sensor check continuously for a change temperature with respect to the environmental conditions in Sydney.
In the logic of my code the program will continuously invoking each beer every 20 secs.
If the temperature of the beer is outside the range it will pop up an alert box and invokes the print the message "Beer X temperature is outside the range"

A main functions is invoked to run the applications and notifies when the application has started and ended, since the program continously runs
Hint: To exit the program you must close the entire program, as it's a concurrency/threading method which continously runs.
Hint: there maybe a pop up alert box behind the program if you cannot see it, this happens if temeprature is outside the range

What could have been done in a better way?
I could change the programming langauge. Since Python is a simple language
I could of think of a more feasible solution than the current implementation of this solution, if real time data was used and updates in a period of time, so that 
I could use methods to compare both values, if the temperature in Sydney is above the normal temperature then the temperature of the beer changes
where as in this implementation I have used randint to generate a random number which is equivalent to a random temperature.

Any other notes you feel relevant for the evaluation of your solution:

1) based on this implementation is based on assumptions in terms of mock data but can be based in real life application if it was implemented in a better way.
2) during this implementation it got me thinking a lot of things that could be done in a different way where I keep continuously debugging my code every time I think something isn’t right
or can be done simpler but match the requirement.




# Random Event Attendance :performing_arts:

This Python program chooses a number of people from a given text file of names. 

It was motivated by my own experiences as a Resident Assistant at Duke University, where I had to choose 10 people to attend a dinner talk with a Nobel Prize Laureate, Professor Paul Modrich of Duke Medicine. Due to popular demand and a limited number of seats, I created a simple Python program to help me make a fair, unbiased choice.

It also helped me learn how to write a simple Python program :smiley:

### Requirements

This program takes in a text file that contains a list of names, with each name separated by a newline character (\n).

Once compiled and running, the program will first ask for name of the file that contains the potential attendees. Next, the program will ask for the number of seats available for the event.

The program will throw errors for erroneous inputs, nonexistent file names, and number of seats that are larger than the number of attendees.

### Compile & Running

```
python main.py
Please input the filename: example.txt 
How many people will be attending the event? 4
```
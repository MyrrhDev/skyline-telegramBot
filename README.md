# SkylineBot

El proyecto SkylineBot per GEI-LP (primavera 2020).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need to install the requirements.txt before you can continue. I suggest creating a python environment in which you can install these dependencies.

Create a python environment:

Open a terminal
Windows
Open the Windows Command Prompt (show path via Start menu and keyboard shortcuts)

Mac OS / Linux
Open the Terminal program. This is usually found under Utilities or Accessories.

```
pip install virtualenv

```

```
virtualenv mynewenvironment

```
Activate the virtual environment
You can activate the python environment by running the following command:

Mac OS / Linux
```
source mynewenvironment/bin/activate
```
Windows
```
mynewenvironment\Scripts\activate

```

When you're done you can just deactivate the environment using the following command:
```
deactivate

```

### Installing

After you've created the python environment or if you've chosen not to, you can now install the dependencies from requirements.txt

Navigate to the folder in the command prompt

```
pip install -r requirements.txt (Python 2)

pip3 install -r requirements.txt (Python 3)

```

To run this bot, you need to run:

```
python3 bot.py
```

And then open up Telegram

## Testing the bot

You need to add the bot to your telegram account by going to:

[skylineBot](t.me/lp_skylineBot)

## Bot commands

* /start: start the conversation with the Bot.
* /help: the Bot shows you a list of all possible commands and brief information of their purpose and use.
* /author: the Bot writes the full name of the author of the project and his official e-mail of the faculty.
* /lst: shows you the defined identifiers and their corresponding area.
* /clean: clears all defined identifiers.
* /save id: must save a skyline defined with the name id.sky.
* /load id: must upload a skyline from the id.sky file.


### Some command examples

The commands /start , /author, and /help:

![commands](/outputs/commands1.png)


### Some examples of Skylines

Here are some unit tests done to test the functionality of this bot according to the specification and the graphic result of it.

Some basic examples:

```
a := (1,2,3)

```
![commands](/outputs/skybasic1.png)

```
a := a + (3,4,6)

```
![commands](/outputs/skybasic2.png)

```
a := a * 3

```
![commands](/outputs/skybasic3.png)


```
-a

```
![commands](/outputs/skybasic4.png)


```
[(1, 2, 3), (3, 4, 6)]

```
![commands](/outputs/skybasic5.png)


```
{100000,20,3,1,10000}

```
![commands](/outputs/skycom6.png)


A bit more complex cases:

```
e:= (1,2,3) + (2,6,5) + (4,3,10)

```
![commands](/outputs/skycom7.png)


```
((-(e*2)) + 4) * (18,3,25)

```
![commands](/outputs/skycom8.png)


```
((((-(e*2)) + 4) * b) * 2) - 8

```
![commands](/outputs/skycom9.png)


```
(-(((((-(e*2)) + 4) * b) * 2)) - 8) + 4

```
![commands](/outputs/skycom10.png)


```
f:= (((-( [(1,2,3) ,(2,6,5) , (4,3,10)] *2)) + 4) * b) * 2
```
![commands](/outputs/skycom11.png)


## Bot commands

* /start: start the conversation with the Bot.
* /help: the Bot shows you a list of all possible commands and brief information of their purpose and use.
* /author: the Bot writes the full name of the author of the project and his official e-mail of the faculty.
* /lst: shows you the defined identifiers and their corresponding area.
* /clean: clears all defined identifiers.
* /save id: must save a skyline defined with the name id.sky.
* /load id: must upload a skyline from the id.sky file.


### Some command examples

The commands /start , /author, and /help:

![commands](/outputs/commands1.jpg)



## Libraries used:

* matplotlib [Matplotlib](https://matplotlib.org/) - to plot the graphs
* [pickle](https://docs.python.org/3.6/library/pickle.html) - Python object serialization. Python Software Foundation, 2019.
* [python-telegram-bot](https://python-telegram-bot.org/) - to interact with Telegram


## Authors

* **Mayra Pastor Valdivia** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


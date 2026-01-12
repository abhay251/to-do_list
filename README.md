# to-do_list
A menu driven to do list made in python. 

## About this project
This is a very basic python project I made just to get a good grasp over the language and understand it's flow. It is a menu-driven to-do list which runs on the terminal. There are some out of the box things I did in this project, such as
- Making a fail safe `getValidInt()` function which would keep running until it gets an interger value, this prevents the app to crase due to unsupported type of data.
- using `os` module to clear the terminal whenever a new menu is opened, to overcome the mess in the flow of the program.
- Using `json` module to save the data into a `listStack.json` file, so that the data is saved when the program shuts down and restarts again.
- I tried to make it failsafe at every step so that it doesn't crash unsupposedly. If incase it does, your commits and reviews are always welcomed :)


## How to run the program
1. Fork the repository in your local machine
2. **Make sure all of the files are contained inside a single folder** (for ease of access and smooth functioning of program)
3. run ` main.py `

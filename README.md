# sp24-lab10
Materials for week 10 lab in CS-370.

_April 2, 2024_

Organization:
* mvc-timer: The MVC example application developed by Prof Davis

## Team Members for Part 1
Enter your names here

## Team Roles for Part 1
Who will start out as
* DRIVER: _Driver's name_
* NAVIGATOR: _Navigator's name_

You will switch halfway through this activity.

## Part 1 Documentation

_Write your answers to the questions below._

* What were the main ideas from the pre-lab reading?
* What questions did you have about this material? What did you find confusing?

### Exercise 0: Run the tests and the application
View the README file in the mvc-timer directory. Run the tests and the application.

_If you have any trouble running the application or tests, please note it here._

### Exercise 1: Read the code
Read the code to understand what happens when you run the text timer application, starting from timer.py. 

Then read the code to understand what happens when you run the GUI application, set the time, and start the timer.

What questions do you have? _Write them here. If you need to know, ask Prof Davis since she wrote the code!_

### Exercise 2: Patterns and principles
_Answer the following questions to the best of your ability._
* Which concrete classes implement the Observer and Observable roles?
* The ThreadTimerModel class implements the Observable roles by keeping an array of observable items and calling their respective notification
* methods. The TimerController class implements the Observer roles and waits for a notification from the ThreadTimerModel.
* How do the model, controller, and view classes gain references to each other? What style of dependency injection does the application use: constructor, method, or property injection?
* The controller gets a general skeleton Model Class passed to it in the as a constructor injection. The model inherets timerView from the Model instead of getting an injection from the looks of it. The model also inherits the subject from the observer class in order to subscribe and unsubscribe from the Observer pattern notification system. The model is then passed to the different view which is assigned bassed on an argument in the timer class. This is then passed to the preffered GUI using what looks like also constructor injection, since it is assigning an entire model object, this then also acts as the observer assignment.

### Exercise 3: Extending the code
Extend the text or GUI application to play a sound when the timer is done.

As time permits, try other exercises from the README in the `mvc-timer` directory.

_Record here: What extensions did you implement or attempt to implement?_

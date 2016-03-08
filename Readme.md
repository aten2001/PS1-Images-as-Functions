#Problem Set 1: Images as Functions (really, arrays or matrices of numbers)

##Description
The purpose of this problem set is to make sure you can have setup your development environment and can load an image, manipulate the values, produce some output, and submit the code along with the report.

##Setup
If you have not already done so, please follow the instructions in the file `Installation.md` to setup your development environment.

In addition to script files provided in this repository, you will need to import some dependencies from another git repository.  Running

<pre>
	<code>
		git submodule init
		git submodule update
	</code>
</pre>

should do the trick.

##Instructions
First, follow the installation guide in the Installation.md file.  If you have questions, please post them to Piazza.

Next, find two interesting images to use. They should be color and rectangular in shape (NOT square). Pick one that is wide and one tall.  You might find some classic vision examples [here](http://sipi.usc.edu/database/database.php?volume=misc), or you may use your own. The image width or height each should not exceed 512 pixels.  Place them in the `input` folder.

Implement the functions given in the file `ps1.py` as described their docstrings.  You may use any of the functions built into the numpy or the cv2 python packages.  It may help you to consult the experiment.py file to see how the functions are to be used.  

Submit your code to the automatic grader using the command `python submit.py.`  This will run a few test and provide you with feedback on your code.  You may submit as many times as you like.  Your last submission before the deadline will be used to determine your grade.

Lastly, run the experiment.py file and use them to help you complete a report on the problem set.  A report template along with the relevant questions can be found [here](https://docs.google.com/presentation/d/1He0lQBj3p0rsRIUkjmyusZS6_2ZtdVpPVE3csuPcDfg/edit?usp=sharing).  Export your report to a pdf format (no other format will be accepted) and submit it via T-square.





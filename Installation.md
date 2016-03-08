#Installation
For all projects in this course, your code will need to run on the course’s official VirtualBox virtual image so that we can properly evaluate it.  Although it is possible to set up other suitable development environments for the course, this is the only process that will be supported by the course TAs.

1. Download the latest [Vagrant binary](https://www.vagrantup.com/downloads.html) for your native platform.  This should also automatically download Virtualbox, which we will use as our provider.
2. From the top-level directory that you plan to use for the course, e.g.

:

* CS6476/
	* oms-cv-ps01/
		* bonnie/
		* experiment.py
		* input_images/		
		* ps1.py
		* output_images/
	* oms-cv-ps02/
	* oms-cv-ps03/

run

<pre>
	<code>
		vagrant init scbrubaker02/compphoto
	</code>
</pre>

Once this completes, from any subdirectory, you should be able to start your virtual machine with just the command `vagrant up` and connect to it with just `vagrant ssh`.  See the [Vagrant documentation](https://www.vagrantup.com/docs/getting-started/) for more details.

## Native Installation
If you prefer run your code natively on your machine, you will need to install opencv....More to come...

To would like to submit your code to the automatic grader using your native environment, you may have to install python's requests library.  The command `pip install requests` should do the trick.  If you haven't installed pip yet, you may do so by following the instructions [here](https://pip.pypa.io/en/stable/installing/).


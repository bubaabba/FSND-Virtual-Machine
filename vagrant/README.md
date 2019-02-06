# Item Catalog
The objective of the Item Catalog project is to build a website with Flask, SQLAlchemy, third party OAuths and API endpoints.

![Screenshot](catalogScreenshots.png)

## Running the project!

### Configure VM & Database

**Step 1:** Download and install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org). We’ll need these tools to setup and manage the Virtual Machine (VM). 


**Step 2:** Run the virtual machine!
Using the terminal, change directory to catalog using the command cd catalog,then type vagrant up to launch your virtual machine.
Once it is up and running, type vagrant ssh. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type exit at the shell prompt. To turn the virtual machine off (without deleting anything), type vagrant halt. If you do this, you'll need to run vagrant up again before you can log into it.

Now that you have Vagrant up and running type vagrant ssh to log into your VM. Change directory to the /vagrant directory by typing cd /vagrant. This will take you to the shared folder between your virtual machine and host machine.

Type ls to ensure that you are inside the directory that contains catalogapp.py, items_catalogModel.py, and two directories named 'templates' and 'static'

Type python catalogapp.py to run the Flask web server. In your browser visit http://localhost:5000 to view the item catalog app.  

### Project Rubric

1. The project implements a JSON endpoint that serves the same information as displayed in the HTML endpoints for an arbitrary item in the catalog.

2. The website read category and item information from a database.

3. The website include a form allowing users to add new items and correctly processes these forms.

4. The website include a form to update a record in the database and correctly processes this form.

5. The website include a way to delete an item from the catalog.

6. Create, delete and update operations do consider authorization status prior to execution.

7. Page implements a third-party authentication & authorization service.

8. There is a 'Login' and 'Logout' button/link in the project.

9. Code is compliant with the Python [PEP 8]
10. Comments are present and effectively explain longer code procedures

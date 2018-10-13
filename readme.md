# Log-Analysis

### How to Run?

#### PreRequisites:
  * [Python3](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)

#### Setup Project:
  1. Install Vagrant(1.9.2) and VirtualBox(5.1.38) (or newer virsion)
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
  4. Unzip this file after downloading it. The database file is called newsdata.sql.
  5. Copy the newsdata.sql file and content of this current repository, by either downloading or cloning it from
  [Here](https://github.com/xu1jia2qi3/Log)
  
#### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```
  3. Change directory to /vagrant by cd /vagrant
  
#### Setting up the database :

  1. Load the data in local database using the command:
  
  ```
    psql -d news -f newsdata.sql
  ```
  
  2. Use `psql -d news` to connect to database.
  
  3. check the database tables by /dt
  
#### Running the queries:
  1. From the vagrant directory inside the virtual machine,run logs.py using:
  ```
    $ python3 logs.py
  ```
  
#### FAQ's: [here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/b2ff9cba-210e-463e-9321-2605f65491a9)

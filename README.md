# Item-Catalog-App
A simple web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. Integrates third party user registration and authentication(Google/Facebook Auth). 
Authenticated users have the ability to post, edit, and delete their own items.

## Usage

### Prerequisites
* Python 2.7
* Vagrant
* VirtualBox

### 
## Set Up
1. Install VirtualBox and Vagrant
2. Clone this repo or download, Unzip and place the Item Catalog folder in your Vagrant directory
3. Launch Vagrant
```
$ Vagrant up 
```
4. Login to Vagrant
```
$ Vagrant ssh
```
5. Change directory to `/vagrant`
```
$ cd /vagrant
```
5. Change directory to `/Item Catalog `
```
$ cd /Item Catalog 
```
5. Run database_setup 
```
$ python database_setup.py
```
5. Populate database with data items
```
$ python fakeitems.py
```

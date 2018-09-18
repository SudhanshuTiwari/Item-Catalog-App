# Item-Catalog-App
A simple web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. Integrates third party user registration and authentication(Google/Facebook Auth). 
Authenticated users have the ability to post, edit, and delete their own items.
Implement CSRF protection on your all CRUD operations.

## Usage

### Prerequisites
* Python 2.7
* Vagrant
* VirtualBox
* Create a Google OAuth credentials. [Integrating GSignIn(SSO)](https://developers.google.com/identity/sign-in/web/sign-in).

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
6. Download client_secrets.json of your Google oAUth.

7.  Replace data-clientid with client_id value in login.html

8. Run the app
```
$ python application.py
```

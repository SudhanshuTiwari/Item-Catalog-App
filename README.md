# Item-Catalog-App
A simple web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. Integrates third party user registration and authentication(Google/Facebook Auth). 
Authenticated users have the ability to post, edit, and delete their own items.
Implements CSRF protection on all CRUD operations.

## Usage

#### Prerequisites
* Python 2.7
* Vagrant
* VirtualBox
* Create a Google OAuth credentials. [Integrating GSignIn(SSO)](https://developers.google.com/identity/sign-in/web/sign-in).

#### Set Up
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
6. Change directory to `/Item Catalog `
```
$ cd /Item Catalog 
```
7. Run following command to download dependencies
```
pip install -r requirements.txt
```
8. Run database_setup 
```
$ python database_setup.py
```
9. Populate database with data items
```
$ python fakeitems.py
```
10. Download client_secrets.json of your Google oAUth.

11.  Replace data-clientid with client_id value in login.html

12. Run the app
```
$ python application.py
```
13. Open http://localhost:5000 in browser


#### Accessing data in JSON format for item catalog REST API's used in applucation:
* User can access JSON data of each API by simply appending JSON as suffix.

###### Example
* Get All items categories - [GET]
 
 Request URL: http://localhost:5001/catalog/JSON

 Response 200 (application/json)

           {
              "categories": [
                {
                  "id": 1, 
                  "name": "Arts & Photography"
                }, 
                {
                  "id": 2, 
                  "name": "Biographies & Memoirs"
                }, 
                {
                  "id": 3, 
                  "name": "Business & Investing"
                }, 
                {
                  "id": 4, 
                  "name": "Literature & Fiction"
                }
              ]
            }
        
  

#### Screenshot: All Items of Category Arts and Photography.
![image](https://user-images.githubusercontent.com/22967893/45753342-187e8200-bc36-11e8-81c6-292051ee3839.png)



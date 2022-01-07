from flask import Flask, render_template, redirect, url_for
from models import UsersModel

class Pages:
    def __init__(self):
        self.users = UsersModel.Users()
    
    def index(self, req):
        allUsers = self.users.find({})
        return render_template('index.html', users=allUsers)
    
    def new_user(self, req):
        try:
            firstName = req.form.get('firstName')
            lastName = req.form.get('lastName')
            
            
            # if not firstName or not lastName:
            #     return redirect(url_for('pages.new_user'))
            
        except Exception as e:
            print(e)
        
        return render_template('new_user.html')
    
            

      
    def edit_user(self, req):
        
        return render_template('edit_user.html')
    
    def delete_user(self, req):
        
        
        redirect(url_for('pages.index'))
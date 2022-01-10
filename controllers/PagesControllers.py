from bson.objectid import ObjectId
from flask import Flask, render_template, redirect, url_for
from models import UsersModel

class Pages:
    def __init__(self):
        self.users = UsersModel.Users()
    
    def index(self, req):
        allUsers = self.users.find({})
        return render_template('index.html', users=allUsers)
    
    def new_user(self, req):
        if req.method == 'GET':
            return render_template('new_user.html')
        elif req.method == 'POST': 
            try:
                firstName = req.form.get('firstName')
                lastName = req.form.get('lastName')
                try:
                    if not firstName or not lastName:
                        return redirect(url_for('pages.new_user'))

                    data = {
                        'nome':firstName, 
                        'sobrenome': lastName    
                    }
                    
                    self.users.create(data)
                    return redirect(url_for('pages.index'))  
                except Exception as e:
                    print(e)  
                
            except Exception as e:
                print(e)
            
    def edit_user(self, req, idx):
        if req.method == 'GET':
            
            user = self.users.find_by_id(idx)
            if not user:
                redirect(url_for('pages.index'))
                
            print(user)
            
            return render_template('edit_user.html', users=user)
        elif req.method == 'POST':
            try:
                firstName = req.form.get('firstName')
                lastName = req.form.get('lastName')
            
                if not firstName or not lastName:
                    return redirect(url_for('pages.new_user'))
                else:
                    data = {
                            'nome':firstName, 
                            'sobrenome': lastName    
                    }
                    
                    self.users.update({'_id':idx}, data)
            except Exception as e:
                print(e)
            
        return redirect(url_for('pages.index'))
        
    def delete_user(self, req, idx):
        if req.method=='GET':
            self.users.delete({'_id':idx})
            
        
        return redirect(url_for('pages.index'))
        
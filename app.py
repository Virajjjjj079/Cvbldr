from flask import Flask, render_template, request, make_response, redirect, send_file, session,url_for
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from flask import render_template, make_response
from io import BytesIO
from flask_mysqldb import MySQL
import creds

 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = creds.MYSQL_HOST
app.config['MYSQL_USER'] = creds.MYSQL_USER
app.config['MYSQL_PASSWORD'] = creds.MYSQL_PASSWORD
app.config['MYSQL_DB'] = creds.MYSQL_DB
 
mysql = MySQL(app)







user_data = []





@app.route('/')
def student():
   return render_template('home.html')


@app.route('/success')
def success():
    return render_template('congrats.html')

@app.route('/jc', methods = ['POST', 'GET'])  
def jobcreation():
    if request.method == 'GET':
        return render_template('homeeex.html')
     
    if request.method == 'POST':
        role = request.form['role']
        company = request.form['company']
        location = request.form['loc']
        salary = request.form['sal']
        connect = request.form['connect']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO employees(job,name,location,salary,email)VALUES(%s,%s,%s,%s,%s)''',(role,company,location,salary,connect))
        mysql.connection.commit()
        cursor.close()
        return render_template('congrats.html')

@app.route('/student')
def select():
      
      return render_template('student.html')

@app.route('/hello', methods=['POST','GET'])
def hello():
    '''fields_added = request.form.get('fields_added',0)
    fields_added2 = request.form.get('fields_added2',0)
    fields_added3 = request.form.get('fields_added3',0)'''

    fields_added = int(request.form.get('fields_added', 0))  # Convert to integer
    fields_added2 = int(request.form.get('fields_added2', 0))  # Convert to integer
    fields_added3 = int(request.form.get('fields_added3', 0))  # Convert to integer
    if request.method == 'GET':
        return render_template('cv.html')



    if fields_added==0 and fields_added2 == 0 and fields_added3 == 0:
        name=request.form['yourname']
        email=request.form['youremail']
        contact=request.form['contact']
        link=request.form['link']
        git=request.form['git']
        address=request.form['address']
    
        dob=request.form['dob']
        lang=request.form['lang']
        company=request.form['company']
        cp=request.form['cp']
        cl=request.form['cl']
        cy=request.form['cy']
        gb=request.form['gb']
        gm=request.form['gm'] 
        cgpa=request.form['cgpa']
        gp=request.form['gp']
        gs=request.form['gs']
        projects=request.form['projects']
        links=request.form['links']
        skills=request.form['skills']
        return render_template('cv.html', name=name, email=email,contact=contact,link=link,git=git,dob = dob, lang = lang, address = address,company=company,cp=cp,cl=cl,cy=cy,gp=gp,gs=gs,cgpa=cgpa,gm=gm,gb=gb,projects=projects,links=links, skills = skills)
    
    
    elif fields_added == 1 and fields_added2 == 0 and fields_added3 == 0:
        name=request.form['yourname']
        email=request.form['youremail']
        contact=request.form['contact']
        link=request.form['link']
        git=request.form['git']
        address=request.form['address']
    
        dob=request.form['dob']
        lang=request.form['lang']
        company=request.form['company']
        cp=request.form['cp']
        cl=request.form['cl']
        cy=request.form['cy']
        gb=request.form['gb']
        gm=request.form['gm'] 
        cgpa=request.form['cgpa']
        gp=request.form['gp']
        gs=request.form['gs']
        projects=request.form['projects']
        links=request.form['links']
        skills=request.form['skills']
        newField0=request.form['newField0'] 
        newField1=request.form['newField1'] 
        newField2=request.form['newField2'] 
        newField3=request.form['newField3'] 
        newField4=request.form['newField4'] 
        return render_template('cv.html', name=name, email=email,contact=contact,link=link,git=git,dob = dob, lang = lang, address = address,company=company,cp=cp,cl=cl,cy=cy,gp=gp,gs=gs,cgpa=cgpa,gm=gm,gb=gb,projects=projects,links=links, skills = skills,newField0=newField0,newField1=newField1,newField2=newField2,newField3=newField3,newField4=newField4)
    

    elif fields_added == 0 and fields_added2 == 1 and fields_added3 == 0:
        name=request.form['yourname']
        email=request.form['youremail']
        contact=request.form['contact']
        link=request.form['link']
        git=request.form['git']
        address=request.form['address']
    
        dob=request.form['dob']
        lang=request.form['lang']
        company=request.form['company']
        cp=request.form['cp']
        cl=request.form['cl']
        cy=request.form['cy']
        gb=request.form['gb']
        gm=request.form['gm'] 
        cgpa=request.form['cgpa']
        gp=request.form['gp']
        gs=request.form['gs']
        projects=request.form['projects']
        links=request.form['links']
        skills=request.form['skills']
        newjob0=request.form['newjob0']
        newjob1=request.form['newjob1']
        newjob2=request.form['newjob2']
        newjob3=request.form['newjob3']
        return render_template('cv.html', name=name, email=email,contact=contact,link=link,git=git,dob = dob, lang = lang, address = address,company=company,cp=cp,cl=cl,cy=cy,gp=gp,gs=gs,cgpa=cgpa,gm=gm,gb=gb,projects=projects,links=links, skills = skills,newjob0=newjob0,newjob1=newjob1,newjob2=newjob2,newjob3=newjob3)
    
    elif fields_added == 0 and fields_added2 == 0 and fields_added3 == 1:
        name=request.form['yourname']
        email=request.form['youremail']
        contact=request.form['contact']
        link=request.form['link']
        git=request.form['git']
        address=request.form['address']
    
        dob=request.form['dob']
        lang=request.form['lang']
        company=request.form['company']
        cp=request.form['cp']
        cl=request.form['cl']
        cy=request.form['cy']
        gb=request.form['gb']
        gm=request.form['gm'] 
        cgpa=request.form['cgpa']
        gp=request.form['gp']
        gs=request.form['gs']
        projects=request.form['projects']
        links=request.form['links']
        skills=request.form['skills']
        newp0=request.form['newp0']
        newp1=request.form['newp1']
        return render_template('cv.html', name=name, email=email,contact=contact,link=link,git=git,dob = dob, lang = lang, address = address,company=company,cp=cp,cl=cl,cy=cy,gp=gp,gs=gs,cgpa=cgpa,gm=gm,gb=gb,projects=projects,links=links, skills = skills,newp0=newp0,newp1=newp1)

    elif fields_added==1 and fields_added2 == 1 and fields_added3==0:
        name=request.form['yourname']
        email=request.form['youremail']
        contact=request.form['contact']
        link=request.form['link']
        git=request.form['git']
        address=request.form['address']
    
        dob=request.form['dob']
        lang=request.form['lang']
        company=request.form['company']
        cp=request.form['cp']
        cl=request.form['cl']
        cy=request.form['cy']
        gb=request.form['gb']
        gm=request.form['gm'] 
        cgpa=request.form['cgpa']
        gp=request.form['gp']
        gs=request.form['gs']
        projects=request.form['projects']
        links=request.form['links']
        skills=request.form['skills']
        newField0=request.form['newField0'] 
        newField1=request.form['newField1'] 
        newField2=request.form['newField2'] 
        newField3=request.form['newField3'] 
        newField4=request.form['newField4'] 
        newjob0=request.form['newjob0']
        newjob1=request.form['newjob1']
        newjob2=request.form['newjob2']
        newjob3=request.form['newjob3']
        print(f"fields_added value: {fields_added} {fields_added2}")
        return render_template('cv.html', name=name, email=email,contact=contact,link=link,git=git,dob = dob, lang = lang, address = address,company=company,cp=cp,cl=cl,cy=cy,gp=gp,gs=gs,cgpa=cgpa,gm=gm,gb=gb,projects=projects,links=links, skills = skills,newField0=newField0,newField1=newField1,newField2=newField2,newField3=newField3,newField4=newField4 ,newjob0=newjob0,newjob1=newjob1,newjob2=newjob2,newjob3=newjob3)
    
    elif fields_added == 1 and fields_added2 == 0 and fields_added3==1:
        name=request.form['yourname']
        email=request.form['youremail']
        contact=request.form['contact']
        link=request.form['link']
        git=request.form['git']
        address=request.form['address']
    
        dob=request.form['dob']
        lang=request.form['lang']
        company=request.form['company']
        cp=request.form['cp']
        cl=request.form['cl']
        cy=request.form['cy']
        gb=request.form['gb']
        gm=request.form['gm'] 
        cgpa=request.form['cgpa']
        gp=request.form['gp']
        gs=request.form['gs']
        projects=request.form['projects']
        links=request.form['links']
        skills=request.form['skills']
        newjob0=request.form['newjob0']
        newjob1=request.form['newjob1']
        newjob2=request.form['newjob2']
        newjob3=request.form['newjob3']
        newp0=request.form['newp0']
        newp1=request.form['newp1']
        return render_template('cv.html', name=name, email=email,contact=contact,link=link,git=git,dob = dob, lang = lang, address = address,company=company,cp=cp,cl=cl,cy=cy,gp=gp,gs=gs,cgpa=cgpa,gm=gm,gb=gb,projects=projects,links=links, skills = skills,newjob0=newjob0,newjob1=newjob1,newjob2=newjob2,newjob3=newjob3,newp0=newp0,newp1=newp1)



    
 
    elif fields_added == 0 and fields_added2 == 1 and fields_added3==1:
        name=request.form['yourname']
        email=request.form['youremail']
        contact=request.form['contact']
        link=request.form['link']
        git=request.form['git']
        address=request.form['address']
    
        dob=request.form['dob']
        lang=request.form['lang']
        company=request.form['company']
        cp=request.form['cp']
        cl=request.form['cl']
        cy=request.form['cy']
        gb=request.form['gb']
        gm=request.form['gm'] 
        cgpa=request.form['cgpa']
        gp=request.form['gp']
        gs=request.form['gs']
        projects=request.form['projects']
        links=request.form['links']
        skills=request.form['skills']
        newField0=request.form['newField0'] 
        newField1=request.form['newField1'] 
        newField2=request.form['newField2'] 
        newField3=request.form['newField3'] 
        newField4=request.form['newField4'] 
        newp0=request.form['newp0']
        newp1=request.form['newp1']
        return render_template('cv.html', name=name, email=email,contact=contact,link=link,git=git,dob = dob, lang = lang, address = address,company=company,cp=cp,cl=cl,cy=cy,gp=gp,gs=gs,cgpa=cgpa,gm=gm,gb=gb,projects=projects,links=links, skills = skills,newField0=newField0,newField1=newField1,newField2=newField2,newField3=newField3,newField4=newField4,newp0=newp0,newp1=newp1)
    



    
    
    

    elif fields_added==1 and fields_added2 == 1 and fields_added3 == 1:
        name=request.form['yourname']
        email=request.form['youremail']
        contact=request.form['contact']
        link=request.form['link']
        git=request.form['git']
        address=request.form['address']
    
        dob=request.form['dob']
        lang=request.form['lang']
        company=request.form['company']
        cp=request.form['cp']
        cl=request.form['cl']
        cy=request.form['cy']
        gb=request.form['gb']
        gm=request.form['gm'] 
        cgpa=request.form['cgpa']
        gp=request.form['gp']
        gs=request.form['gs']
        projects=request.form['projects']
        links=request.form['links']
        skills=request.form['skills']
        newField0=request.form['newField0'] 
        newField1=request.form['newField1'] 
        newField2=request.form['newField2'] 
        newField3=request.form['newField3'] 
        newField4=request.form['newField4'] 
        newjob0=request.form['newjob0']
        newjob1=request.form['newjob1']
        newjob2=request.form['newjob2']
        newjob3=request.form['newjob3']
        newp0=request.form['newp0']
        newp1=request.form['newp1']
        return render_template('cv.html', name=name, email=email,contact=contact,link=link,git=git,dob = dob, lang = lang, address = address,company=company,cp=cp,cl=cl,cy=cy,gp=gp,gs=gs,cgpa=cgpa,gm=gm,gb=gb,projects=projects,links=links, skills = skills,newField0=newField0,newField1=newField1,newField2=newField2,newField3=newField3,newField4=newField4,newjob0=newjob0,newjob1=newjob1,newjob2=newjob2,newjob3=newjob3,newp0=newp0,newp1=newp1)
    

    
    else:
        name=request.form['yourname']
        email=request.form['youremail']
        contact=request.form['contact']
        link=request.form['link']
        git=request.form['git']
        address=request.form['address']
    
        dob=request.form['dob']
        lang=request.form['lang']
        company=request.form['company']
        cp=request.form['cp']
        cl=request.form['cl']
        cy=request.form['cy']
        gb=request.form['gb']
        gm=request.form['gm'] 
        cgpa=request.form['cgpa']
        gp=request.form['gp']
        gs=request.form['gs']
        projects=request.form['projects']
        links=request.form['links']
        skills=request.form['skills']
        # No fields were added, handle accordingly
        return render_template('cv.html', name=name, email=email,contact=contact,link=link,git=git,dob = dob, lang = lang, address = address,company=company,cp=cp,cl=cl,cy=cy,gp=gp,gs=gs,cgpa=cgpa,gm=gm,gb=gb,projects=projects,links=links, skills = skills)
    
    


       










"""@app.route('/hello', methods=['POST'])
def hello():
    fields_added = request.form.get('fields_added', 0)  # Default to 0 if not present
    fields_added2 = request.form.get('fields_added2', 0)
    fields_added3 = request.form.get('fields_added3', 0)

    data = {
    'name': request.form['yourname'],
    'email': request.form['youremail'],
    'contact': request.form['contact'],
    'link': request.form['link'],
    'git': request.form['git'],
    'address': request.form['address'],
    'dob':request.form['dob'],
    'lang':request.form['lang'],
    'company':request.form['company'],
    'cp':request.form['cp'],
    'cl':request.form['cl'],
    'cy':request.form['cy'],
    'gb':request.form['gb'],
    'gm':request.form['gm'], 
    'cgpa':request.form['cgpa'],
    'gp':request.form['gp'],
    'gs':request.form['gs'],
    'projects':request.form['projects'],
    'links':request.form['links'],
    'skills':request.form['skills'],
        # ... other existing data
    }

    # Conditional data addition based on fields_added values
    if fields_added == 1:
        data.update({
        'newField0': request.form['newField0'],
        'newField1': request.form['newField1'],
        'newField2': request.form['newField2'],
        'newField3': request.form['newField3'],
        'newField4': request.form['newField4'],
            # ... other new fields for fields_added
        })
    elif fields_added2 == 1:
        data.update({
        'newjob0': request.form['newjob0'],
        'newjob1': request.form['newjob1'],
        'newjob2': request.form['newjob2'],
        'newjob3': request.form['newjob3'],
            # ... other new fields for fields_added2
        })
    elif fields_added3 == 1:
        data.update({
        'newp0': request.form['newp0'],
        'newp1': request.form['newp1'],
            # ... other new fields for fields_added3
        })

    return render_template('cv.html', data=data)"""
@app.route('/contact')
def contact():
    return render_template("contact.html")

#addon sectionnnn
@app.route('/joblist')
def job_list():
    cursor = mysql.connection.cursor()
    
    # Execute an SQL query to retrieve data from the database
    cursor.execute("SELECT * FROM employees")
    
    # Fetch all rows from the result set
    data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()

    return render_template('preview.html',data=data)


   

#
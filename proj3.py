import flask
from flask import render_template
import os 
from flask import send_from_directory  
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from forms import searchform
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

app=flask.Flask(__name__)
app.secret_key = 'bruh'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'ww2'

mysql=MySQL(app)


@app.route('/index/')
def index():
    return 'Routed to index()'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        #print(account)
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['ID']
            session['username'] = account['USERNAME']
            # Redirect to home page
            return redirect('/login/'+username, code=302)
            #return render_template('name.html', name=username)
        elif password=="" or username=="":
            pass
            #return render_template('home.html', inc="Please sign in again!", inc2="")
        else:
            # Account doesnt exist or username/password incorrect
            return render_template('home.html', inc="Incorrect username or password!", inc2="")

    if request.method == 'POST' and 'regusername' in request.form and 'regpassword' in request.form and 'regemail' in request.form:
        # Create variables for easy access
        username = request.form['regusername']
        password = request.form['regpassword']
        email = request.form['regemail']
        cfmpassword = request.form['confirm-password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            return render_template('home.html', inc="", inc2="Account already exists!")
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return render_template('home.html', inc="", inc2="Invalid email address!")
        elif not re.match(r'[A-Za-z0-9]+', username):
            return render_template('home.html', inc="", inc2="Username must only contain characters or numbers!")
        elif not username or not password or not email:
            return render_template('home.html', inc="", inc2="Please fill up the form!")
        elif password != cfmpassword:
            return render_template('home.html', inc="", inc2="Passwords do not match!")
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            return render_template('home.html', inc="", inc2="You have successfully registered!")
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        return render_template('home.html', inc="", inc2="Please fill up the form!")
            
    return render_template('home.html', inc="", inc2="")
#registration use flask flash to display success msg
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))

   #fetch database table if select=update, table=table
   #load database table by PK=red cell, nonPK=green cell, make nonPK editable (popup?)
   #for (row in result)
   # for column in nonPK
   #  cursor.execute update table set {}={} where {}={}.format(col,colval,PKtuple,PKtupleval)
   #   mysql.connection.commit()
   #jquery ajax, but need php file and thus php server :(

@app.route('/login/<name>/', methods=['GET', 'POST'])
def home(name, result=[]):
    comcols=['Name', 'Rank', 'Country']
    comvar=['NAME', 'COMRANK', 'CNAME']
    battcols=['ID', 'Name', 'Description', 'Armor Lost, Axis', 'Aircraft Lost, Axis', 'Carriers Lost, Axis', 'Battleships Lost, Axis', 
            'Cruisers Lost, Axis', 'Destroyers Lost, Axis', 'Submarines Lost, Axis', 'Casualties, Axis', 'Armor Lost, Allies', 'Aircraft Lost, Allies',
            'Carriers Lost, Allies', 'Battlehsips Lost, Allies', 'Cruisers Lost, Allies', 'Destroyers Lost, Allies', 'Submarines Lost, Allies',
            'Casualties, Allies', 'Part Of (ID)']
    battvar=['ID', 'NAME', 'DESCR', 'AXISNUMARMORL', 'AXISNUMAIRCRAFTL', 'AXISNUMCVL', 'AXISNUMBBL', 'AXISNUMCL', 'AXISNUMDDL', 'AXISNUMSSL',
            'AXISCASUALTY', 'ALLIEDNUMARMORL', 'ALLIEDNUMAIRCRAFTL', 'ALLIEDNUMCVL', 'ALLIEDNUMBBL', 'ALLIEDNUMCL', 'ALLIEDNUMDDL', 'ALLIEDNUMSSL',
            'ALLIEDCASUALTY', 'PARTOF']
    milcols=['Country', 'Name', 'Type']
    milvar=['CNAME', 'NAME', 'TYPE']
    shipcols=['Name', 'Type', 'Country', 'Sunk By', 'Sunk Date']
    shipvar=['NAME', 'TYPE', 'CNAME', 'SUNKBY', 'SUNKDATE']
    countrycols=['Name', 'Max Ground Strength', 'No. of Carriers', 'No. of Battleships', 'No. of Cruisers', 'No. of Destroyers', 'No. of Submarines',
        'No. of Fighters', 'No. of Bombers', 'Armor Lost', 'Aircraft Lost', 'Carriers Lost', 'Battleships Lost', 'Cruisers Lost', 'Destroyers Lost',
        'Submarines Lost', 'Military Casualties', 'Civilian Casualties']
    countryvar=['NAME', 'MAXGSTR', 'NUMCV', 'NUMBB', 'NUMC', 'NUMDD', 'NUMSS', 'NUMFIGHT', 'NUMBOMB', 'NUMARMORL', 'NUMAIRCRAFTL', 'NUMCVL',
        'NUMBBL', 'NUMCL', 'NUMDDL', 'NUMSSL', 'MCASUALTY', 'CCASUALTY']
    surrendercols=['Surrendering country', 'Country accepting surrender', 'Date of surrender']
    surrendervar=['C1', 'C2', 'DDATE']
    warcols=['Country declaring war', 'Country being declared war on', 'Date of declaration']
    warvar=['C1', 'C2', 'DDATE']
    eventcols=['ID', 'Country 1 involved', 'Country 2 involved', 'Date', 'Description']
    eventvar=['ID', 'C1', 'C2', 'SDATE', 'DESCR']
    placecols=['Place', 'Country']
    placevar=['NAME', 'CNAME']
    commandmcols=['Commander', 'Country', 'Military name', 'Start Date', 'End Date']
    commandmvar=['COMNAME', 'MCNAME', 'MNAME', 'SDATE', 'EDATE']
    hascols=['ID', 'Place', 'Axis armies ID', 'Allied armies ID', 'Start Date', 'End Date']
    hasvar=['ID', 'PNAME', 'AXISKEY', 'ALLIEDKEY', 'SDATE', 'EDATE']
    hasscols=['Ship', 'Country', 'Military name', 'Start Date', 'End Date']
    hassvar=['SHIP', 'MCNAME', 'MNAME', 'SDATE', 'EDATE']
    colsdictionary={'Battle':battcols, 'Commander':comcols, 'COMMANDM':commandmcols, 'Country':countrycols, 'Event':eventcols, 'has':hascols, 'hass':hasscols, 'Military':milcols, 'Place':placecols, 'Ship':shipcols, 'Surrender':surrendercols, 'War':warcols}
    vardictionary={'Battle':battvar, 'Commander':comvar, 'COMMANDM':commandmvar, 'Country':countryvar, 'Event':eventvar, 'has':hasvar, 'hass':hassvar, 'Military':milvar, 'Place':placevar, 'Ship':shipvar, 'Surrender':surrendervar, 'War':warvar}
    PKdictionary={'Battle':battvar[0:1], 'Commander':comvar[0:1], 'COMMANDM':commandmvar[0:3], 'Country':countryvar[0:1], 'Event':eventvar[0:1], 'has':hasvar[0:4], 'hass':hassvar[0:3], 'Military':milvar[0:2], 'Place':placevar[0:1], 'Ship':shipvar[0:1], 'Surrender':surrendervar[0:1], 'War':warvar[0:2]}
    labelsdictionary={'Battle':'Battle', 'Commander':'Commander', 'COMMANDM':'Military under Command', 'Country':'Country', 'Event':'Event', 'has':'Battle Info', 'hass':'Ship Info', 'Military':'Military', 'Place':'Place', 'Ship':'Ship', 'Surrender':'Surrender', 'War':'War'}
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT ID,NAME FROM BATTLE')
    results=cursor.fetchall()
    battlelist=[str(x['ID'])+": "+str(x['NAME']) for x in results]
    cursor.execute('SELECT NAME FROM COUNTRY')
    results=cursor.fetchall()
    countrylist=[x['NAME'] for x in results]
    countryvariablenames=['Max Ground Strength', 'No. of Carriers', 'No. of Battleships', 'No. of Cruisers', 'No. of Destroyers', 'No. of Submarines',
        'No. of Fighters', 'No. of Bombers', 'Armor Lost', 'Aircraft Lost', 'Carriers Lost', 'Battleships Lost', 'Cruisers Lost', 'Destroyers Lost',
        'Submarines Lost', 'Military Casualties', 'Civilian Casualties']
    countryvariable=['MAXGSTR', 'NUMCV', 'NUMBB', 'NUMC', 'NUMDD', 'NUMSS', 'NUMFIGHT', 'NUMBOMB', 'NUMARMORL', 'NUMAIRCRAFTL', 'NUMCVL',
        'NUMBBL', 'NUMCL', 'NUMDDL', 'NUMSSL', 'MCASUALTY', 'CCASUALTY']
    cols, var, PK=[], [], []
    tablename=''
    #print(request.form)
    if request.method=='POST' and 'search' in request.form:
        search=request.form['search']
        cat=request.form.get('cat')
        by=request.form.get('by')
        params=[search, cat, by]
        return search_results(name, 1, params, battlelist, countrylist, countryvariablenames, countryvariable)
    elif request.method=='POST' and 'tables' in request.form:
        table = request.form.getlist('tables')
        sort = request.form.getlist('sort')
        order = request.form.getlist('order')
        params=[table, sort, order]
        return search_results(name, 2, params, battlelist, countrylist, countryvariablenames, countryvariable)
    elif request.method=='POST' and 'stats' in request.form and 'countries' in request.form:
        stats=request.form.getlist('stats')
        countries=request.form.getlist('countries')
        params=[stats, countries]
        return search_results(name, 3, params, battlelist, countrylist, countryvariablenames, countryvariable)
    elif request.method=='POST' and 'countries2' in request.form and 'variables' in request.form:
        countries=request.form.getlist('countries2')
        variables=request.form.getlist('variables')
        params=[countries, variables]
        return search_results(name, 4, params, battlelist, countrylist, countryvariablenames, countryvariable)
    elif request.method=='POST' and 'comparebatt' in request.form:
        battle=request.form.getlist('comparebatt')
        params=[battle]
        return search_results(name, 5, params, battlelist, countrylist, countryvariablenames, countryvariable)
    elif request.method=='POST' and 'tables2' in request.form:
        tables2=request.form.get('tables2')
        cursor.execute('SELECT * FROM {}'.format(tables2))
        result=cursor.fetchall()
        cols=colsdictionary[tables2]
        var=vardictionary[tables2]
        #print(result)
        tablename=labelsdictionary[tables2]
        PK=PKdictionary[tables2]
        return render_template('name3.html', name=name, battlelist=battlelist, numBattle=len(battlelist), countrylist=countrylist, numCountry=len(countrylist), countryvariablenames=countryvariablenames, countryvariable=countryvariable, numCountryVariable=len(countryvariable), result=result, numResult=len(result), cols=cols, var=var, numCols=len(var), tablename=tablename, PK=PK)
    elif request.method=='POST' and 'alldata' in request.form:
        edits=request.form['alldata']
        #print(edits)
        params=[edits]
        return search_results(name, 6, params, battlelist, countrylist, countryvariablenames, countryvariable)
    return render_template('name3.html', name=name, battlelist=battlelist, numBattle=len(battlelist), countrylist=countrylist, numCountry=len(countrylist), countryvariablenames=countryvariablenames, countryvariable=countryvariable, numCountryVariable=len(countryvariable), result=result, numResult=len(result), cols=cols, var=var, numCols=len(var), tablename=tablename, PK=PK)

@app.route('/login/<name>/search/', methods=['GET', 'POST'])
def search_results(name, tab, params, battlelist, countrylist, countryvariablenames, countryvariable):
    comcols=['Name', 'Rank', 'Country']
    comvar=['NAME', 'COMRANK', 'CNAME']
    battcols=['ID', 'Name', 'Description', 'Armor Lost, Axis', 'Aircraft Lost, Axis', 'Carriers Lost, Axis', 'Battleships Lost, Axis', 
            'Cruisers Lost, Axis', 'Destroyers Lost, Axis', 'Submarines Lost, Axis', 'Casualties, Axis', 'Armor Lost, Allies', 'Aircraft Lost, Allies',
            'Carriers Lost, Allies', 'Battlehsips Lost, Allies', 'Cruisers Lost, Allies', 'Destroyers Lost, Allies', 'Submarines Lost, Allies',
            'Casualties, Allies', 'Part Of (ID)']
    battvar=['ID', 'NAME', 'DESCR', 'AXISNUMARMORL', 'AXISNUMAIRCRAFTL', 'AXISNUMCVL', 'AXISNUMBBL', 'AXISNUMCL', 'AXISNUMDDL', 'AXISNUMSSL',
            'AXISCASUALTY', 'ALLIEDNUMARMORL', 'ALLIEDNUMAIRCRAFTL', 'ALLIEDNUMCVL', 'ALLIEDNUMBBL', 'ALLIEDNUMCL', 'ALLIEDNUMDDL', 'ALLIEDNUMSSL',
            'ALLIEDCASUALTY', 'PARTOF']
    milcols=['Country', 'Name', 'Type']
    milvar=['CNAME', 'NAME', 'TYPE']
    shipcols=['Name', 'Type', 'Country', 'Sunk By', 'Sunk Date']
    shipvar=['NAME', 'TYPE', 'CNAME', 'SUNKBY', 'SUNKDATE']
    countrycols=['Name', 'Max Ground Strength', 'No. of Carriers', 'No. of Battleships', 'No. of Cruisers', 'No. of Destroyers', 'No. of Submarines',
        'No. of Fighters', 'No. of Bombers', 'Armor Lost', 'Aircraft Lost', 'Carriers Lost', 'Battleships Lost', 'Cruisers Lost', 'Destroyers Lost',
        'Submarines Lost', 'Military Casualties', 'Civilian Casualties']
    countryvar=['NAME', 'MAXGSTR', 'NUMCV', 'NUMBB', 'NUMC', 'NUMDD', 'NUMSS', 'NUMFIGHT', 'NUMBOMB', 'NUMARMORL', 'NUMAIRCRAFTL', 'NUMCVL',
        'NUMBBL', 'NUMCL', 'NUMDDL', 'NUMSSL', 'MCASUALTY', 'CCASUALTY']
    surrendercols=['Surrendering country', 'Country accepting surrender', 'Date of surrender']
    surrendervar=['C1', 'C2', 'DDATE']
    warcols=['Country declaring war', 'Country being declared war on', 'Date of declaration']
    warvar=['C1', 'C2', 'DDATE']
    eventcols=['ID', 'Country 1 involved', 'Country 2 involved', 'Date', 'Description']
    eventvar=['ID', 'C1', 'C2', 'SDATE', 'DESCR']
    placecols=['Place', 'Country']
    placevar=['NAME', 'CNAME']
    commandmcols=['Commander', 'Country', 'Military name', 'Start Date', 'End Date']
    commandmvar=['COMNAME', 'MCNAME', 'MNAME', 'SDATE', 'EDATE']
    hascols=['ID', 'Place', 'Axis armies ID', 'Allied armies ID', 'Start Date', 'End Date']
    hasvar=['ID', 'PNAME', 'AXISKEY', 'ALLIEDKEY', 'SDATE', 'EDATE']
    hasscols=['Ship', 'Country', 'Military name', 'Start Date', 'End Date']
    hassvar=['SHIP', 'MCNAME', 'MNAME', 'SDATE', 'EDATE']
    colsdictionary={'Battle':battcols, 'Commander':comcols, 'COMMANDM':commandmcols, 'Country':countrycols, 'Event':eventcols, 'has':hascols, 'hass':hasscols, 'Military':milcols, 'Place':placecols, 'Ship':shipcols, 'Surrender':surrendercols, 'War':warcols}
    vardictionary={'Battle':battvar, 'Commander':comvar, 'COMMANDM':commandmvar, 'Country':countryvar, 'Event':eventvar, 'has':hasvar, 'hass':hassvar, 'Military':milvar, 'Place':placevar, 'Ship':shipvar, 'Surrender':surrendervar, 'War':warvar}
    labelsdictionary={'Battle':'Battle', 'Commander':'Commander', 'COMMANDM':'Military under Command', 'Country':'Country', 'Event':'Event', 'has':'Battle Info', 'hass':'Ship Info', 'Military':'Military', 'Place':'Place', 'Ship':'Ship', 'Surrender':'Surrender', 'War':'War'}
    
    PKdictionary={'Battle':battvar[0:1], 'Commander':comvar[0:1], 'COMMANDM':commandmvar[0:3], 'Country':countryvar[0:1], 'Event':eventvar[0:1], 'has':hasvar[0:4], 'hass':hassvar[0:3], 'Military':milvar[0:2], 'Place':placevar[0:1], 'Ship':shipvar[0:1], 'Surrender':surrendervar[0:1], 'War':warvar[0:2]}
    
    viewtables={}
    results = []
    result1, result2, result3, result4 = [], [], [], []
    colsplotted=[]
    imgs=[]
    cols=[]
    PK=[]
    var=[]
    tablestats=[]
    tablestatscols=['No. of Users', 'No. of Countries', 'No. of Places', 'No. of Commanders', 'No. of Militaries', 'No. of Ships', 'No. of Events', 'No. of Battles']
    #battlelist=[]
    #fill selectors dynamically instead of hardcode
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if tab==1:
        search, cat, by=params[0], params[1], params[2]
        by=int(by)
        cols=colsdictionary[cat]
        var=vardictionary[cat]
        if cat=='Battle':
            if by==1: #country involved
                cursor.execute('SELECT * FROM {},HAS,AXISFORCE,ALLIEDFORCE WHERE {}.ID=HAS.ID AND AXISFORCE.AXISKEY=HAS.AXISKEY AND ALLIEDFORCE.ALLIEDKEY=HAS.ALLIEDKEY AND (AXISFORCE.MCNAME LIKE {} OR ALLIEDFORCE.MCNAME LIKE {}) GROUP BY {}.ID'.format(cat, cat, '\'%'+search+'%\'', '\'%'+search+'%\'', cat))
            elif by==2: #date
                cursor.execute('SELECT * FROM {},HAS WHERE {}.ID=HAS.ID AND (CAST({} AS DATE) BETWEEN HAS.SDATE AND HAS.EDATE)'.format(cat, cat, '\''+search+'\''))
            elif by==3: #description
                cursor.execute('SELECT * FROM {} WHERE DESCR LIKE {}'.format(cat, '\'%'+search+'%\''))
            elif by==4: #military
                cursor.execute('SELECT * FROM {},HAS,AXISFORCE,ALLIEDFORCE WHERE {}.ID=HAS.ID AND AXISFORCE.AXISKEY=HAS.AXISKEY AND ALLIEDFORCE.ALLIEDKEY=HAS.ALLIEDKEY AND (AXISFORCE.MNAME LIKE {} OR ALLIEDFORCE.MNAME LIKE {}) GROUP BY {}.ID'.format(cat, cat, '\'%'+search+'%\'', '\'%'+search+'%\'', cat))
            elif by==5: #name
                cursor.execute('SELECT * FROM {} WHERE NAME LIKE {}'.format(cat, '\'%'+search+'%\''))
            else: #place
                cursor.execute('SELECT * FROM {},HAS WHERE {}.ID=HAS.ID AND HAS.PNAME LIKE {}'.format(cat, cat, '\'%'+search+'%\''))
        elif cat=='Commander':
            if by==1: #country
                cursor.execute('SELECT * FROM {} WHERE CNAME LIKE {}'.format(cat, '\'%'+search+'%\''))
            elif by==2: #name
                cursor.execute('SELECT * FROM {} WHERE NAME LIKE {}'.format(cat, '\'%'+search+'%\''))
            else: #rank
                cursor.execute('SELECT * FROM {} WHERE COMRANK LIKE {}'.format(cat, '\'%'+search+'%\''))
        elif cat=='Military': #search by battles
            if by==1: #commander
                cursor.execute('SELECT * FROM {},COMMANDM WHERE COMMANDM.MCNAME={}.CNAME AND COMMANDM.MNAME={}.NAME AND COMNAME LIKE {}'.format(cat, cat, cat, '\'%'+search+'%\''))
            elif by==2: #country
                cursor.execute('SELECT * FROM {} WHERE CNAME LIKE {}'.format(cat, '\'%'+search+'%\''))
            elif by==3: #date this retutrns militaries existing on a certain date, what about if we want to check by year? or month?
                cursor.execute('SELECT * FROM {},COMMANDM WHERE COMMANDM.MCNAME={}.CNAME AND COMMANDM.MNAME={}.NAME AND (CAST({} AS DATE) BETWEEN COMMANDM.SDATE AND COMMANDM.EDATE)'.format(cat, cat, cat, '\''+search+'\'')) 
            elif by==4: #name
                cursor.execute('SELECT * FROM {} WHERE NAME LIKE {}'.format(cat, '\'%'+search+'%\''))
            else: #type
                cursor.execute('SELECT * FROM {} WHERE TYPE LIKE {}'.format(cat, '\'%'+search+'%\''))
        else: #order by, filter columns sort by 2+ columns
            if by==1: #country
                cursor.execute('SELECT * FROM {} WHERE CNAME LIKE {}'.format(cat, '\'%'+search+'%\''))
            elif by==2: #name
                cursor.execute('SELECT * FROM {} WHERE NAME LIKE {}'.format(cat, '\'%'+search+'%\''))
            else: #type
                cursor.execute('SELECT * FROM {} WHERE TYPE LIKE {}'.format(cat, '\'%'+search+'%\''))
        results = cursor.fetchall()
        #remove <br> tags and use padding/margin instead
    elif tab==2: #select/filter by columns? show only certain columns? need another variable + how to do that?
        table, sort, order = params[0], params[1], params[2]
        cols=colsdictionary[table[0]]
        var=vardictionary[table[0]]
        #sorts = cols[int(sort[0])-1]
        sorts = var[int(sort[0])-1]
        #orders = var[cols.index(order[0])]
        cursor.execute('SELECT * FROM {} ORDER BY {} {}'.format(table[0], sorts, order[0]))
        results = cursor.fetchall()
    elif tab==3: #show stats by combined variables instead of only 1 varibale? eg max(ships) instead of max(cv) or max(bb); does stats refer to return country with max/min of that stat? or just return max/min of all stats (what we r doing now) (i.e. disregard country)? need to specify which variable to max/min by? but then avg sum doesnt make sense
        cols=countrycols
        var=countryvar
        stats, countries=params[0], tuple(params[1])
        cursor.execute('SELECT * FROM COUNTRY WHERE NAME IN {}'.format(countries))
        results = cursor.fetchall()
        if 'Average' in stats:
            cursor.execute('SELECT COUNT(*) AS NAME, AVG(MAXGSTR) AS MAXGSTR, AVG(NUMCV) AS NUMCV, AVG(NUMBB) AS NUMBB, AVG(NUMC) AS NUMC, AVG(NUMDD) AS NUMDD, AVG(NUMSS) AS NUMSS, AVG(NUMFIGHT) AS NUMFIGHT, AVG(NUMBOMB) AS NUMBOMB, AVG(NUMARMORL) AS NUMARMORL, AVG(NUMAIRCRAFTL) AS NUMAIRCRAFTL, AVG(NUMCVL) AS NUMCVL, AVG(NUMBBL) AS NUMBBL, AVG(NUMCL) AS NUMCL, AVG(NUMDDL) AS NUMDDL, AVG(NUMSSL) AS NUMSSL, AVG(MCASUALTY) AS MCASUALTY, AVG(CCASUALTY) AS CCASUALTY FROM COUNTRY WHERE NAME IN {}'.format(countries))
            result1 = cursor.fetchall()
            result1[0]['NAME']='Average'
        if 'Max' in stats:
            cursor.execute('SELECT COUNT(*) AS NAME, MAX(MAXGSTR) AS MAXGSTR, MAX(NUMCV) AS NUMCV, MAX(NUMBB) AS NUMBB, MAX(NUMC) AS NUMC, MAX(NUMDD) AS NUMDD, MAX(NUMSS) AS NUMSS, MAX(NUMFIGHT) AS NUMFIGHT, MAX(NUMBOMB) AS NUMBOMB, MAX(NUMARMORL) AS NUMARMORL, MAX(NUMAIRCRAFTL) AS NUMAIRCRAFTL, MAX(NUMCVL) AS NUMCVL, MAX(NUMBBL) AS NUMBBL, MAX(NUMCL) AS NUMCL, MAX(NUMDDL) AS NUMDDL, MAX(NUMSSL) AS NUMSSL, MAX(MCASUALTY) AS MCASUALTY, MAX(CCASUALTY) AS CCASUALTY FROM COUNTRY WHERE NAME IN {}'.format(countries))
            result2 = cursor.fetchall()
            result2[0]['NAME']='Max'
        if 'Min' in stats:
            cursor.execute('SELECT COUNT(*) AS NAME, MIN(MAXGSTR) AS MAXGSTR, MIN(NUMCV) AS NUMCV, MIN(NUMBB) AS NUMBB, MIN(NUMC) AS NUMC, MIN(NUMDD) AS NUMDD, MIN(NUMSS) AS NUMSS, MIN(NUMFIGHT) AS NUMFIGHT, MIN(NUMBOMB) AS NUMBOMB, MIN(NUMARMORL) AS NUMARMORL, MIN(NUMAIRCRAFTL) AS NUMAIRCRAFTL, MIN(NUMCVL) AS NUMCVL, MIN(NUMBBL) AS NUMBBL, MIN(NUMCL) AS NUMCL, MIN(NUMDDL) AS NUMDDL, MIN(NUMSSL) AS NUMSSL, MIN(MCASUALTY) AS MCASUALTY, MIN(CCASUALTY) AS CCASUALTY FROM COUNTRY WHERE NAME IN {}'.format(countries))
            result3 = cursor.fetchall()
            result3[0]['NAME']='Min'
        if 'Sum' in stats:
            cursor.execute('SELECT COUNT(*) AS NAME, SUM(MAXGSTR) AS MAXGSTR, SUM(NUMCV) AS NUMCV, SUM(NUMBB) AS NUMBB, SUM(NUMC) AS NUMC, SUM(NUMDD) AS NUMDD, SUM(NUMSS) AS NUMSS, SUM(NUMFIGHT) AS NUMFIGHT, SUM(NUMBOMB) AS NUMBOMB, SUM(NUMARMORL) AS NUMARMORL, SUM(NUMAIRCRAFTL) AS NUMAIRCRAFTL, SUM(NUMCVL) AS NUMCVL, SUM(NUMBBL) AS NUMBBL, SUM(NUMCL) AS NUMCL, SUM(NUMDDL) AS NUMDDL, SUM(NUMSSL) AS NUMSSL, SUM(MCASUALTY) AS MCASUALTY, SUM(CCASUALTY) AS CCASUALTY FROM COUNTRY WHERE NAME IN {}'.format(countries))
            result4 = cursor.fetchall()
            result4[0]['NAME']='Sum'
    # add more countries,  why didnt put date in battles
    #make proper page refresh, compare countries tab4? events tab5
    #use view to reduce duplicate query typing
    #make ui, formatting better, esp of image grid click zoom , dropdown selector
    #show/hide columns possible?
    #maybe dont do tab 5 since no time
    elif tab==4:
        cols=countrycols
        var=countryvar
        countries, variables = tuple(params[0]), params[1]
        labels = params[0]
        plotted = []
        imgs = []
        for v in variables:
            cursor.execute('SELECT {} FROM COUNTRY WHERE NAME IN {}'.format(v, countries))
            result = cursor.fetchall()
            data = [x[v] for x in result]
            #we exclude 0 and None values also for readability of the chart
            data2 = [x if x is not None else 0 for x in data]
            sizes = [float(x)/sum(data2) for x in data2]
            s = np.array(sizes)
            l = np.array(labels)
            df = pd.DataFrame({'label':l, 'size':s})
            df2 = df.dropna()
            df3 = df2.loc[df2['size']>0]
            
            if not df3.empty:
                plotted.append(v)
                fig,ax=plt.subplots()
                ax.pie(df3['size'], labels=df3['label'], autopct='%1.2f%%') 
                ax.axis('equal')
                dt = datetime.today()
                seconds = dt.timestamp()
                hashed = hash(str(seconds))
                filename = 'plots/'+str(hashed)+'.svg'
                imgs.append('../../static/'+filename)
                plt.savefig(os.path.join(app.root_path, 'static/', filename), transparent=True, bbox_inches='tight')
                plt.clf()
                #plt.show()

            #print(result)
        #print(countries, variables)
        colsplotted = [cols[x] for x in [var.index(y) for y in plotted]]
    #fix remember me
    #fix stats, max() will return max of every individual column, must specify which col is max to sort by

    #event lists, surrender war,format stats data, table width, create checkbox 'all',
    elif tab==5: #include compare country also maybe
        battlevars=[x[4:] for x in battvar[3:11]]
        #countryvars=[]
        #cols=battcols
        #var=battvar
        battle=params[0]
        cursor.execute('SELECT * FROM BATTLE WHERE BATTLE.ID={}'.format(int(battle[0].split(" ")[0][:-1])))
        tempresult=cursor.fetchall()[0]
        axisvar=[x for x in tempresult.keys() if 'AXIS' in x]
        axisresult=[tempresult[x] for x in axisvar]
        alliedvar=[x for x in tempresult.keys() if 'ALLIED' in x]
        alliedresult=[tempresult[x] for x in alliedvar]
        alliedresult=['Allies']+alliedresult
        axisresult=['Axis']+axisresult
        battlevars=['Data']+battlevars
        alliedcolor=['']
        axiscolor=['']
        for r in range(1,len(battlevars)):
            if isinstance(alliedresult[r], int) and isinstance(axisresult[r], int):
                if alliedresult[r]>axisresult[r]:
                    alliedcolor.append('green')
                    axiscolor.append('red')
                elif alliedresult[r]<axisresult[r]:
                    alliedcolor.append('red')
                    axiscolor.append('green')
                else:
                    alliedcolor.append('yellow')
                    axiscolor.append('yellow')
            else:
                alliedcolor.append('yellow')
                axiscolor.append('yellow')

        print(battlevars, axisresult, alliedresult)
        print(alliedcolor, axiscolor)
    elif tab==6:
        alldata = params[0]
        #print(alldata)
        alldata=alldata.split(',')
        cols=colsdictionary[alldata[0]]
        var=vardictionary[alldata[0]]
        PK=PKdictionary[alldata[0]]
        K=[i for i in var if i not in PK]
        num=len(var)+1

        for i in range(1,len(alldata),num):
            data=alldata[i:i+num-1]
            changeddata=[]
            s=''
            temp=alldata[i:i+num]
            #print(temp)
            if temp[-1]=='0001': #nochange
                #nothing here
                pass
            elif temp[-1]=='0011': #update
                for j in data:
                    k = j.replace('_', ',')
                    try:
                        k=int(k)
                        changeddata.append(str(k))
                    except:
                        changeddata.append('\''+k+'\'')
                #print(changeddata)
                for j in range(len(changeddata)):
                    if changeddata[j]=='\'None\'':
                        changeddata[j]='NULL'
                pkdata=[changeddata[i] for i in range(len(changeddata)) if var[i] in PK]
                kdata=[changeddata[i] for i in range(len(changeddata)) if var[i] not in PK]
                
                wherestatement='('
                for p in PK:
                    wherestatement+=p
                    wherestatement+=','
                wherestatement=wherestatement[:-1]+')=('
                for p in pkdata:
                    wherestatement+=p
                    wherestatement+=','
                wherestatement=wherestatement[:-1]+')'

                setstatement=''
                for k in range(len(K)):
                    setstatement+=K[k]+'='+kdata[k]+','
                setstatement=setstatement[:-1]
                
                print('UPDATE {} SET {} WHERE {}'.format(alldata[0], setstatement, wherestatement))
                #cursor.execute('UPDATE {} SET {} WHERE {}'.format(alldata[0], setstatement, wherestatement))
                #mysql.connection.commit()
                
            elif temp[-1]=='0111' or temp[-1]=='0101': #insert
                for j in data:
                    k = j.replace('_', ',')
                    try:
                        k=int(k)
                        changeddata.append(str(k))
                    except:
                        changeddata.append('\''+k+'\'')
                #print(changeddata)
                for j in range(len(changeddata)):
                    if changeddata[j]=='\'None\'':
                        changeddata[j]='NULL'
                pkdata=[changeddata[i] for i in range(len(changeddata)) if var[i] in PK]
                kdata=[changeddata[i] for i in range(len(changeddata)) if var[i] not in PK]

                insertstatement='('
                for d in changeddata:
                    insertstatement+=d
                    insertstatement+=','
                insertstatement=insertstatement[:-1]+')'

                print('INSERT INTO {} VALUES {}'.format(alldata[0], insertstatement))
            elif temp[-1]=='1011' or temp[-1]=='1001': #delete
                for j in data:
                    k = j.replace('_', ',')
                    try:
                        k=int(k)
                        changeddata.append(str(k))
                    except:
                        changeddata.append('\''+k+'\'')
                #print(changeddata)
                for j in range(len(changeddata)):
                    if changeddata[j]=='\'None\'':
                        changeddata[j]='NULL'
                pkdata=[changeddata[i] for i in range(len(changeddata)) if var[i] in PK]
                kdata=[changeddata[i] for i in range(len(changeddata)) if var[i] not in PK]
                
                deletestatement='('
                for p in PK:
                    deletestatement+=p
                    deletestatement+=','
                deletestatement=deletestatement[:-1]+')=('
                for p in pkdata:
                    deletestatement+=p
                    deletestatement+=','
                deletestatement=deletestatement[:-1]+')'

                print('DELETE FROM {} WHERE {}'.format(alldata[0], deletestatement))
                #cursor.execute('DELETE FROM {} WHERE {}'.format(alldata[0], deletestatement))
                #mysql.connection.commit()
            elif temp[-1]=='1101' or temp[-1]=='1111': #nothing
                pass
           
            #print(s)
            #cursor.execute('INSERT INTO {} VALUES {}'.format(alldata[0], s))
            #mysql.connection.commit()

        cursor.execute('SELECT * FROM TABLESTATS')
        tablestats=cursor.fetchall()[0]
        tablestats=[tablestats[x] for x in tablestats.keys() if x!='ID']
        
    return render_template('results.html', name=name, results=results, numResults=len(results), columnName=cols, varName=var, numCols=len(cols), tab=tab, result1=result1, result2=result2, result3=result3, result4=result4, colsplotted=colsplotted, imgs=imgs, numimgs=len(imgs), battlelist=battlelist, numBattle=len(battlelist), countrylist=countrylist, numCountry=len(countrylist), tablestats=tablestats, tablestatscols=tablestatscols, numStats=len(tablestats), countryvariablenames=countryvariablenames, countryvariable=countryvariable, numCountryVariable=len(countryvariable))

@app.route('/login/<name>/results', methods=['GET', 'POST'])
def load_results(results, name):
    return render_template('results.html', name=name, results=results, numResults=len(results))

@app.route('/css/main.css/')
def cssroute():
    return render_template('css/main.css')

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run()
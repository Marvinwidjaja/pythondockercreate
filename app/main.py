from flask import *
import sqlite3, hashlib, os
from werkzeug.utils import secure_filename
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import os
from urllib.parse import urljoin, urlparse
import re
from flask import request
from itertools import chain
def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)
def check(email):                                        
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
    if(re.search(regex,email)):                          
        return 1                                         
                                                         
    else:                                                
        return 0                                         
app=Flask(__name__, instance_relative_config=True, static_url_path="", static_folder="static")
app.secret_key='anything'
ALLOWED_EXTENSIONS=set(['jpeg','jpg','png','gif'])
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")
def get_info():
    html_page=urlopen('https://bbcicecream.eu/collections/newarrivals')              
    soup = BeautifulSoup(html_page,"html.parser")                                    
    bbc_product = []                                                                 
    bbc_price=[]                                                                     
    bbc_image=[]                                                                     
    bbc_image_final=[] 
    bbc_link=[]
    bbc_desc=[]
    detail_images = []
    numofpic = []
    num=[]
    accessories=[]
    crewnecks=[]
    headwear=[]
    hoodies=[]
    jackets=[]
    lstshirts=[]
    pants=[]
    shirts=[]
    shorts=[]
    tshirts=[]
    list_of_categories=[]
    dict={}
    for img in soup.findAll('img'):                                                  
        img_url = img.attrs.get("src")                                               
        bbc_image.append(img_url)                                                    
    del bbc_image[0]
    bbc_image = bbc_image[::2]
    del bbc_image[0]
    bbc_image = bbc_image[::2]
    aces = ["https:" + i for i in bbc_image]                                                                                                                                     
    for div in soup.findAll('a', {'class': 'prd-Card_TitleLink'}):                            
        bbc_product.append(div.contents)                                                      
    lst2 = [item[0] for item in bbc_product]                                                  
    stripped_line = [s.strip() for s in lst2]
    for div in soup.findAll('span', {'class': 'money'}):    
        bbc_price.append(div.contents[0].strip())   
    for div in soup.findAll('href', {'class': 'prd-Card_TitleLink'}):
        bbc_link.append(div.contents)
    maxx = [link['href'] for link in soup.findAll("a", {"class": "prd-Card_TitleLink"})]
    spades = ["https://bbcicecream.eu" + i for i in maxx]
    for i in spades:
        response=requests.get(i)
        soup=BeautifulSoup(response.content,"html.parser")
        for div in soup.findAll('p', {'class': 'prd-Content_ShortDesc'}):
            bbc_desc.append(div.contents[0].strip())
    for i in spades:
        response = requests.get(i)
        soup = BeautifulSoup(response.content, "html.parser")

        numofpic=[]
        for tag in soup.find_all("meta"):
            if tag.get("property", None) == "og:image:secure_url":
                detail_images.append(tag.get("content", None))
                numofpic=len(detail_images)
                dict[i]=numofpic
    for value in dict.values():
        num.append(value)
    ids=[]
    a=num[0]
    num=[j-i for i, j in zip(num[:-1], num[1:])]
    num.append(a)
    length=len(num)
    for i in range(0,length):
        ids.append(i)
    len_detail=len(detail_images)
    cu_list = [sum(num[0:x:1]) for x in range(0, length+1)]
    accessories_link="https://bbcicecream.eu/collections/newarrivals/filter-type-accessories"
    response = requests.get(accessories_link)
    soup=BeautifulSoup(response.content,"html.parser")
    for div in soup.findAll('a', {'class': 'prd-Card_TitleLink'}):
        accessories.append(div.contents)
    list0 = [item[0] for item in accessories]
    accessories_final = [s.strip() for s in list0]
    crewnecks_link="https://bbcicecream.eu/collections/newarrivals/filter-type-crewnecks"
    response = requests.get(crewnecks_link)
    soup=BeautifulSoup(response.content,"html.parser")
    for div in soup.findAll('a', {'class': 'prd-Card_TitleLink'}):
        crewnecks.append(div.contents)
    list1 = [item[0] for item in crewnecks]
    crewnecks_final = [s.strip() for s in list1]
    headwear_link="https://bbcicecream.eu/collections/newarrivals/filter-type-headwear"
    response = requests.get(headwear_link)
    soup=BeautifulSoup(response.content,"html.parser")
    for div in soup.findAll('a', {'class': 'prd-Card_TitleLink'}):
        headwear.append(div.contents)
    list2 = [item[0] for item in headwear]
    headwear_final = [s.strip() for s in list2]
    hoodies_link="https://bbcicecream.eu/collections/newarrivals/filter-type-hoodies"
    response = requests.get(hoodies_link)
    soup=BeautifulSoup(response.content,"html.parser")
    for div in soup.findAll('a', {'class': 'prd-Card_TitleLink'}):
        hoodies.append(div.contents)
    list3 = [item[0] for item in hoodies]
    hoodies_final = [s.strip() for s in list3]
    jackets_link="https://bbcicecream.eu/collections/newarrivals/filter-type-jackets"
    response = requests.get(jackets_link)
    soup=BeautifulSoup(response.content,"html.parser")
    for div in soup.findAll('a', {'class': 'prd-Card_TitleLink'}):
        jackets.append(div.contents)
    list4 = [item[0] for item in jackets]
    jackets_final = [s.strip() for s in list4]
    lstshirts_link="https://bbcicecream.eu/collections/newarrivals/filter-type-l-s-t-shirt"
    response = requests.get(lstshirts_link)
    soup=BeautifulSoup(response.content,"html.parser")
    for div in soup.findAll('a', {'class': 'prd-Card_TitleLink'}):
        lstshirts.append(div.contents)
    list5 = [item[0] for item in lstshirts]
    lstshirts_final = [s.strip() for s in list5]
    pants_link="https://bbcicecream.eu/collections/newarrivals/filter-type-pants"
    response = requests.get(pants_link)
    soup=BeautifulSoup(response.content,"html.parser")
    for div in soup.findAll('a', {'class': 'prd-Card_TitleLink'}):
        pants.append(div.contents)
    list6 = [item[0] for item in pants]
    pants_final = [s.strip() for s in list6]
    shirts_link="https://bbcicecream.eu/collections/newarrivals/filter-type-shirts"
    response = requests.get(shirts_link)
    soup=BeautifulSoup(response.content,"html.parser")
    for div in soup.findAll('a', {'class': 'prd-Card_TitleLink'}):
        shirts.append(div.contents)
    list7 = [item[0] for item in shirts]
    shirts_final = [s.strip() for s in list7]
    shorts_link="https://bbcicecream.eu/collections/newarrivals/filter-type-shorts"
    response = requests.get(shorts_link)
    soup=BeautifulSoup(response.content,"html.parser")
    for div in soup.findAll('a', {'class': 'prd-Card_TitleLink'}):
        shorts.append(div.contents)
    list8 = [item[0] for item in shorts]
    shorts_final = [s.strip() for s in list8]
    tshirts_link='https://bbcicecream.eu/collections/newarrivals/filter-type-t-shirts'
    response = requests.get(tshirts_link)
    soup=BeautifulSoup(response.content,"html.parser")
    for div in soup.findAll('a', {'class': 'prd-Card_TitleLink'}):
        tshirts.append(div.contents)
    list9 = [item[0] for item in tshirts]
    tshirts_final = [s.strip() for s in list9]
    html_page = urlopen('https://bbcicecream.eu/collections/newarrivals')
    soup = BeautifulSoup(html_page, "html.parser")
    bbc_product = []
    for div in soup.findAll('a', {'class': 'prd-Card_TitleLink'}):
        bbc_product.append(div.contents)
    lst2 = [item[0] for item in bbc_product]
    stripped_line = [s.strip() for s in lst2]
    for i in stripped_line:
        if i in accessories_final:
            list_of_categories.append("accessories")
        if i in crewnecks_final:
            list_of_categories.append("crewnecks")
        if i in headwear_final:
            list_of_categories.append("headwear")
        if i in hoodies_final:
            list_of_categories.append("hoodies")
        if i in jackets_final:
            list_of_categories.append("jackets")
        if i in lstshirts_final:
            list_of_categories.append("lshirts")
        if i in pants_final:
            list_of_categories.append("pants")
        if i in shirts_final:
            list_of_categories.append("shirts")
        if i in shorts_final:
            list_of_categories.append("sorts")
        if i in tshirts_final:
            list_of_categories.append("tshirts")

    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        for i in range(49):
            cur.execute("INSERT INTO user (product_id,product_name, product_price,product_url,product_desc,total,cum_total)"
                    " VALUES (?, ?, ?, ?, ?, ?,?)",
                    (ids[i],stripped_line[i], bbc_price[i],aces[i],bbc_desc[i],num[i],cu_list[i]))
        conn.commit()
        # cur.execute("INSERT INTO user (total_data)"
        # "VALUES(?)",(int(length)))
        # conn.commit()
        for j in range(len_detail):
            cur.execute("INSERT INTO details (detail_images)"
            " VALUES (?)",
            (detail_images[j],))
        conn.commit()
    conn.close()

# def get_details():
#     html_page=urlopen('https://bbcicecream.eu/collections/newarrivals')
#     soup = BeautifulSoup(html_page,"html.parser")
#     bbc_link=[]
#     bbc_desc=[]
#     for div in soup.findAll('p', {'class': 'prd-Content_ShortDesc'}):
#         bbc_link.append(div.contents[0])
#     maxx = [link['href'] for link in soup.findAll("a", {"class": "prd-Card_TitleLink"})]
#     spades = ["https://bbcicecream.eu" + i for i in maxx]
#     detail_images = []
#     dict={}
#     numofpic = []
#     num=[]
#     dict2={}
#     for i in spades:
#         response = requests.get(i)
#         soup = BeautifulSoup(response.content, "html.parser")

#         numofpic=[]
#         for tag in soup.find_all("meta"):
#             if tag.get("property", None) == "og:image:secure_url":
#                 detail_images.append(tag.get("content", None))
#                 numofpic=len(detail_images)
#                 dict[i]=numofpic
#     for value in dict.values():
#         num.append(value)
#     a=num[0]
#     num=[j-i for i, j in zip(num[:-1], num[1:])]
#     num.append(a)
#     length=len(num)
#     cu_list = [sum(num[0:x:1]) for x in range(0, length+1)]

#     return detail_images,num,cu_list
# def get_link():
#     details,num,cumsum_final=get_details()
#     return details,num,cumsum_final
@app.route("/")
def root(): 
    loggedIn, firstName= getLoginDetails()
    final_price=[]
    final_name=[]
    final_url=[]
    # aces,stripped_line,bbc_price=get_info()
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("SElECT  product_name FROM user")
        stripped_line=cur.fetchall()
        cur.execute("SElECT  product_price FROM user")
        bbc_price=cur.fetchall()
        cur.execute("SElECT  product_url FROM user")
        aces=cur.fetchall()
        conn.commit()
    conn.close()
    final_price=list(chain.from_iterable(bbc_price))
    final_url=list(chain.from_iterable(aces))
    final_name=list(chain.from_iterable(stripped_line))
    # for i in bbc_price:
    #     final_price.append(i)
    return render_template('home.html',aces=final_url,name=final_name,price=final_price, loggedIn=loggedIn, firstName=firstName)
    # return render_template('home.html')
def getLoginDetails():
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        if 'email' not in session:
            loggedIn = False
            name = ''
        else:
            loggedIn = True
            cur.execute("SELECT userId, name FROM registerrr WHERE email = ?", (session['email'], ))
            firstName = cur.fetchone()
    conn.close()
    return (loggedIn, firstName)
def is_valid(email, password):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT email, password FROM registerrr')
    data = cur.fetchall()
    for row in data:
        if row[0] == email and row[1] == hashlib.md5(password.encode()).hexdigest():
            return True
    return False
@app.route("/registration")
def registration():
    return render_template("register.html")
@app.route("/success")
def success():
    return render_template("success.html")
@app.route("/shop")
def shop():
    final_price=[]
    final_name=[]
    final_url=[]
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("SElECT  product_name FROM user")
        stripped_line=cur.fetchall()
        cur.execute("SElECT  product_price FROM user")
        bbc_price=cur.fetchall()
        cur.execute("SElECT  product_url FROM user")
        aces=cur.fetchall()
        conn.commit()
    conn.close()
    final_price=list(chain.from_iterable(bbc_price))
    final_url=list(chain.from_iterable(aces))
    final_name=list(chain.from_iterable(stripped_line))
    return render_template('shop.html',aces=final_url,name=final_name,price=final_price)
@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'POST': 
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        with sqlite3.connect(db_path) as con:
            cur = con.cursor()

                
        x = cur.execute("SELECT email FROM registerrr WHERE email=:email", {"email":email}).fetchone()
        a=check(email)
        if x is not None or a == 0:
            flash("Invalid Email or Email has already been registered","warning")
            return render_template('register.html')
            
        else:
            cur.execute('INSERT INTO registerrr (password, email, name) VALUES (?, ?, ?)', (hashlib.md5(password.encode()).hexdigest(), email, name))
            con.commit()
            con.close()
        return render_template("success.html")

@app.route("/loginForm")
def loginForm():
    if 'email' in session:
        return redirect(url_for('root'))
    else:
        return render_template('login.html', error='')

@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if is_valid(email, password):
            session['email'] = email
            return redirect(url_for('root'))
        else:
            error = 'Invalid UserId / Password'
            return render_template('login.html', error=error)
@app.route('/details')
def details():
    id=request.args.get('id')
    details=[]
    details_final=[]
    num=[]
    cumsum_final=[]
    num_final=[]
    cumsum_final=[]
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("SElECT  detail_images FROM details")
        details=cur.fetchall()
        conn.commit()
    conn.close()
    final_details=list(chain.from_iterable(details))
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("SElECT total FROM user")
        num=cur.fetchall()
        cur.execute("SElECT cum_total FROM user")
        cumsum=cur.fetchall()
        cur.execute("SELECT product_name FROM user")
        name=cur.fetchall()
        cur.execute("SELECT product_price FROM user")
        price=cur.fetchall()
        cur.execute("SELECT product_desc FROM user")
        desc=cur.fetchall()
        conn.commit()
    conn.close()
    num_final=list(chain.from_iterable(num))
    cumsum_final=list(chain.from_iterable(cumsum))
    price_final=list(chain.from_iterable(price))
    name_final=list(chain.from_iterable(name))
    desc_final=list(chain.from_iterable(desc))
    q=int(id)
    if (q==0) and ((num_final[1]-0)==2):
        a=0
        b=1
        return render_template("detailscopy.html",a=a,b=b,name=name_final,price=price_final,desc=desc_final,q=q)
    if (q==0) and ((num_final[1]-0)==3):
        a=0
        b=1
        c=2
        return render_template("details.html",a=a,b=b,details=final_details,c=c,name=name_final,price=price_final,desc=desc_final,q=q)
    if (q>0) and (cumsum_final[q]-cumsum_final[q-1]==3):
        a=cumsum_final[q]
        b=cumsum_final[q]+1
        c=cumsum_final[q]+2
        return render_template("details.html",a=a,b=b,details=final_details,c=c,name=name_final,price=price_final,desc=desc_final,q=q)
    if (q>0) and (cumsum_final[q]-cumsum_final[q-1]==2):
        a=cumsum_final[q]+1
        b=cumsum_final[q]+2
        return render_template("detailscopy.html",a=a,b=b,details=final_details,name=name_final,price=price_final,desc=desc_final,q=q)

    return render_template("details.html",details=final_details,name=name_final,price=price_final,desc=desc_final)

@app.route('/accessories')
def accessories():

    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        values = 'accessories'
        cur.execute("SELECT product_name FROM user WHERE category=?",(values,))
        name=cur.fetchall()
        cur.execute("SELECT product_price FROM user WHERE category=?",(values,))
        price=cur.fetchall()
        cur.execute("SELECT product_url FROM user WHERE category=?",(values,))
        desc=cur.fetchall()
        cur.execute("SELECT product_id FROM user WHERE category=?",(values,))
        ids=cur.fetchall()
        conn.commit()
    conn.close()
        
    ids_final=list(chain.from_iterable(ids))
    price_final=list(chain.from_iterable(price))
    name_final=list(chain.from_iterable(name))
    desc_final=list(chain.from_iterable(desc))
    a=len(price_final)
    return render_template('accessories.html',name=name_final,price=price_final,desc=desc_final,a=a,ids=ids_final)
@app.route('/crewnecks')
def crewnecks():
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        values = 'crewnecks'
        cur.execute("SELECT product_name FROM user WHERE category=?",(values,))
        name=cur.fetchall()
        cur.execute("SELECT product_price FROM user WHERE category=?",(values,))
        price=cur.fetchall()
        cur.execute("SELECT product_url FROM user WHERE category=?",(values,))
        desc=cur.fetchall()
        cur.execute("SELECT product_id FROM user WHERE category=?",(values,))
        ids=cur.fetchall()
        conn.commit()
    conn.close()
        
    ids_final=list(chain.from_iterable(ids))
    price_final=list(chain.from_iterable(price))
    name_final=list(chain.from_iterable(name))
    desc_final=list(chain.from_iterable(desc))
    a=len(price_final)
    return render_template('crewnecks.html',name=name_final,price=price_final,desc=desc_final,a=a,ids=ids_final)
@app.route('/lstshirt')
def lstshirt():

    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        values = 'lshirts'
        cur.execute("SELECT product_name FROM user WHERE category=?",(values,))
        name=cur.fetchall()
        cur.execute("SELECT product_price FROM user WHERE category=?",(values,))
        price=cur.fetchall()
        cur.execute("SELECT product_url FROM user WHERE category=?",(values,))
        desc=cur.fetchall()
        cur.execute("SELECT product_id FROM user WHERE category=?",(values,))
        ids=cur.fetchall()
        conn.commit()
    conn.close()
        
    ids_final=list(chain.from_iterable(ids))
    price_final=list(chain.from_iterable(price))
    name_final=list(chain.from_iterable(name))
    desc_final=list(chain.from_iterable(desc))
    a=len(price_final)
    return render_template('lstshirts.html',name=name_final,price=price_final,desc=desc_final,a=a,ids=ids_final)
@app.route('/tshirts')
def tshirts():

    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        values = 'tshirts'
        cur.execute("SELECT product_name FROM user WHERE category=?",(values,))
        name=cur.fetchall()
        cur.execute("SELECT product_price FROM user WHERE category=?",(values,))
        price=cur.fetchall()
        cur.execute("SELECT product_url FROM user WHERE category=?",(values,))
        desc=cur.fetchall()
        cur.execute("SELECT product_id FROM user WHERE category=?",(values,))
        ids=cur.fetchall()
        conn.commit()
    conn.close()
        
    ids_final=list(chain.from_iterable(ids))
    price_final=list(chain.from_iterable(price))
    name_final=list(chain.from_iterable(name))
    desc_final=list(chain.from_iterable(desc))
    a=len(price_final)
    return render_template('tshirts.html',name=name_final,price=price_final,desc=desc_final,a=a,ids=ids_final)
@app.route('/shirts')
def shirts():

    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        values = 'shirts'
        cur.execute("SELECT product_name FROM user WHERE category=?",(values,))
        name=cur.fetchall()
        cur.execute("SELECT product_price FROM user WHERE category=?",(values,))
        price=cur.fetchall()
        cur.execute("SELECT product_url FROM user WHERE category=?",(values,))
        desc=cur.fetchall()
        cur.execute("SELECT product_id FROM user WHERE category=?",(values,))
        ids=cur.fetchall()
        conn.commit()
    conn.close()
        
    ids_final=list(chain.from_iterable(ids))
    price_final=list(chain.from_iterable(price))
    name_final=list(chain.from_iterable(name))
    desc_final=list(chain.from_iterable(desc))
    a=len(price_final)
    return render_template('shirts.html',name=name_final,price=price_final,desc=desc_final,a=a,ids=ids_final)
@app.route('/shorts')
def shorts():

    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        values = 'shorts'
        cur.execute("SELECT product_name FROM user WHERE category=?",(values,))
        name=cur.fetchall()
        cur.execute("SELECT product_price FROM user WHERE category=?",(values,))
        price=cur.fetchall()
        cur.execute("SELECT product_url FROM user WHERE category=?",(values,))
        desc=cur.fetchall()
        cur.execute("SELECT product_id FROM user WHERE category=?",(values,))
        ids=cur.fetchall()
        conn.commit()
    conn.close()
        
    ids_final=list(chain.from_iterable(ids))
    price_final=list(chain.from_iterable(price))
    name_final=list(chain.from_iterable(name))
    desc_final=list(chain.from_iterable(desc))
    a=len(price_final)
    return render_template('shorts.html',name=name_final,price=price_final,desc=desc_final,a=a,ids=ids_final)
@app.route('/pants')
def pants():

    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        values = 'pants'
        cur.execute("SELECT product_name FROM user WHERE category=?",(values,))
        name=cur.fetchall()
        cur.execute("SELECT product_price FROM user WHERE category=?",(values,))
        price=cur.fetchall()
        cur.execute("SELECT product_url FROM user WHERE category=?",(values,))
        desc=cur.fetchall()
        cur.execute("SELECT product_id FROM user WHERE category=?",(values,))
        ids=cur.fetchall()
        conn.commit()
    conn.close()
        
    ids_final=list(chain.from_iterable(ids))
    price_final=list(chain.from_iterable(price))
    name_final=list(chain.from_iterable(name))
    desc_final=list(chain.from_iterable(desc))
    a=len(price_final)
    return render_template('pants.html',name=name_final,price=price_final,desc=desc_final,a=a,ids=ids_final)
@app.route('/jackets')
def jackets():

    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        values = 'jackets'
        cur.execute("SELECT product_name FROM user WHERE category=?",(values,))
        name=cur.fetchall()
        cur.execute("SELECT product_price FROM user WHERE category=?",(values,))
        price=cur.fetchall()
        cur.execute("SELECT product_url FROM user WHERE category=?",(values,))
        desc=cur.fetchall()
        cur.execute("SELECT product_id FROM user WHERE category=?",(values,))
        ids=cur.fetchall()
        conn.commit()
    conn.close()
        
    ids_final=list(chain.from_iterable(ids))
    price_final=list(chain.from_iterable(price))
    name_final=list(chain.from_iterable(name))
    desc_final=list(chain.from_iterable(desc))
    a=len(price_final)
    return render_template('jackets.html',name=name_final,price=price_final,desc=desc_final,a=a,ids=ids_final)
@app.route('/headwear')
def headwear():

    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        values = 'headwear'
        cur.execute("SELECT product_name FROM user WHERE category=?",(values,))
        name=cur.fetchall()
        cur.execute("SELECT product_price FROM user WHERE category=?",(values,))
        price=cur.fetchall()
        cur.execute("SELECT product_url FROM user WHERE category=?",(values,))
        desc=cur.fetchall()
        cur.execute("SELECT product_id FROM user WHERE category=?",(values,))
        ids=cur.fetchall()
        conn.commit()
    conn.close()
        
    ids_final=list(chain.from_iterable(ids))
    price_final=list(chain.from_iterable(price))
    name_final=list(chain.from_iterable(name))
    desc_final=list(chain.from_iterable(desc))
    a=len(price_final)
    return render_template('headwears.html',name=name_final,price=price_final,desc=desc_final,a=a,ids=ids_final)
@app.route('/hoodies')
def hoodies():

    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        values = 'hoodies'
        cur.execute("SELECT product_name FROM user WHERE category=?",(values,))
        name=cur.fetchall()
        cur.execute("SELECT product_price FROM user WHERE category=?",(values,))
        price=cur.fetchall()
        cur.execute("SELECT product_url FROM user WHERE category=?",(values,))
        desc=cur.fetchall()
        cur.execute("SELECT product_id FROM user WHERE category=?",(values,))
        ids=cur.fetchall()
        conn.commit()
    conn.close()
        
    ids_final=list(chain.from_iterable(ids))
    price_final=list(chain.from_iterable(price))
    name_final=list(chain.from_iterable(name))
    desc_final=list(chain.from_iterable(desc))
    a=len(price_final)
    return render_template('hoodies.html',name=name_final,price=price_final,desc=desc_final,a=a,ids=ids_final)

def getLoginDetails():
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        if 'email' not in session:
            loggedIn = False
            firstName = ''
            noOfItems = 0
        else:
            loggedIn = True
            cur.execute("SELECT name FROM registerrr WHERE email = ?", (session['email'], ))
            firstName = cur.fetchone()
    conn.close()
    return (loggedIn, firstName)
@app.route("/addToWishh")
def addToWishh():

    productId = request.args.get('id')
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO wishlist (product_id) VALUES (?)", (productId,))
        conn.commit()
    conn.close()
    return redirect(url_for('shop'))
@app.route("/addToWish")
def addToWish():

    productId = request.args.get('id')
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO wishlist (product_id) VALUES (?)", (productId,))
        conn.commit()
    conn.close()
    return redirect(url_for('root'))
@app.route("/addToWishhh",methods=["GET"])
def addToWishhh():
    productId = request.args.get('id')
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO wishlist (product_id) VALUES (?)", (productId,))
        conn.commit()
    conn.close()
    return redirect(url_for('shop'))
@app.route("/deleteWish")
def deleteWish():
    n = request.args.get('id')
    n=int(n)
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM wishlist")
        productID=cur.fetchall()
        conn.commit()
    if productID!=None:
        productID=list(chain.from_iterable(productID))
        final=productID[n]
        with sqlite3.connect(db_path) as conn:
            cur=conn.cursor()
            cur.execute("DELETE FROM wishlist where product_id = (?)",(final,))
        conn.close()
    else:
        return redirect(url_for('wishlist'))
    return redirect(url_for('wishlist'))
@app.route("/deleteCart")
def deleteCart():
    n = request.args.get('id')
    n=int(n)
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("SELECT product_id FROM cart")
        productID=cur.fetchall()
        conn.commit()
    if productID!=None:
        productID=list(chain.from_iterable(productID))
        final=productID[n]
        with sqlite3.connect(db_path) as conn:
            cur=conn.cursor()
            cur.execute("DELETE FROM cart where product_id = (?)",(final,))
        conn.close()
    else:
        return redirect(url_for('cart'))
    return redirect(url_for('cart'))
@app.route("/wishlist")
def wishlist():
    with sqlite3.connect(db_path) as conn:
        cur=conn.cursor()
        cur.execute("SELECT user.product_name FROM user, wishlist WHERE user.product_id = wishlist.product_id")
        name=cur.fetchall()
        cur.execute("SELECT user.product_price FROM user, wishlist WHERE user.product_id = wishlist.product_id")
        price=cur.fetchall()
        cur.execute("SELECT user.product_url FROM user, wishlist WHERE user.product_id = wishlist.product_id")
        image=cur.fetchall()
        cur.execute("SELECT count(*) FROM wishlist")
        a=cur.fetchone()
        cur.execute("SELECT * FROM wishlist")
        product_id=cur.fetchall()

    if a is None:
        a=0
    else:
        a=a[0]
    name_final=list(chain.from_iterable(name))
    product_id=list(chain.from_iterable(product_id))
    price_final=list(chain.from_iterable(price))
    image_final=list(chain.from_iterable(image))
    return render_template("wishlist.html",name= name_final,price=price_final,image=image_final,a=a,product_id=product_id)
@app.route("/cart")
def cart():
    loggedIn, firstName= getLoginDetails()
    email = session['email']
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("SELECT userId FROM registerrr WHERE email = ?", (email, ))
        userId = cur.fetchone()[0]
        cur=conn.cursor()
        cur.execute("SELECT user.product_name FROM user, cart WHERE user.product_id = cart.product_id AND cart.userId = ?", (userId, ))
        name=cur.fetchall()
        cur.execute("SELECT user.product_price FROM user, cart WHERE user.product_id = cart.product_id AND cart.userId = ?", (userId, ))
        price=cur.fetchall()
        cur.execute("SELECT user.product_url FROM user, cart WHERE user.product_id = cart.product_id AND cart.userId = ?", (userId, ))
        image=cur.fetchall()
        cur.execute("SELECT count(*) FROM cart WHERE cart.userId = ?", (userId, ))
        a=cur.fetchone()
        cur.execute("SELECT size from cart WHERE cart.userId = ?", (userId, ))
        size=cur.fetchall()
        cur.execute("SELECT quantity from cart WHERE cart.userId = ?", (userId, ))
        number=cur.fetchall()
        cur.execute("SELECT product_id FROM cart WHERE cart.userId = ?", (userId, ))
        product_id=cur.fetchall()
    
    name_final=list(chain.from_iterable(name))
    a=a[0]
    price_final=list(chain.from_iterable(price))
    image_final=list(chain.from_iterable(image))
    size=list(chain.from_iterable(size))
    number_final=list(chain.from_iterable(number))
    product_id=list(chain.from_iterable(product_id))
    capital=[x.upper() for x in size]
    return render_template("cart.html",name= name_final,price=price_final,image=image_final,a=a,size=capital,quantity=number_final,product_id=product_id)

@app.route("/addtocart", methods = ["GET", "POST"] )
def addtocart():
    if 'email' not in session:
        return redirect(url_for('loginForm'))
    else:
        productid = request.args.get('id')
        if request.method == 'POST':
            quantity=request.form.get("quantity",None)
            size=request.form.get("size",None)
            with sqlite3.connect(db_path) as conn:
                cur=conn.cursor()
                cur.execute("SELECT userId FROM registerrr WHERE email = ?", (session['email'], ))
                userId = cur.fetchone()[0]
                cur.execute("INSERT INTO cart (userId,product_id,size,quantity) VALUES (?,?,?,?)", (userId,productid,size,quantity))
                conn.commit()
            conn.close()
            return redirect(url_for('shop'))
        else:
            return redirect(url_for('shop'))    
@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('root'))

if __name__ == '__main__':
    get_info()
    app.run(host="0.0.0.0",port=8080,debug=True)
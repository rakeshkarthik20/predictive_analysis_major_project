# from crypt import methods
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/whatpdis")
def hello1():
    return render_template("whatpdis.html")

@app.route("/Diseases")
def hello2():
    return render_template("Diseases.html")

@app.route("/feedback")
def hello3():
    return render_template("feedback.html")

@app.route("/Diabetes")
def hello4():
    return render_template("diabetes.html")

@app.route("/sub",methods=['POST'])
def submit():
    if request.method == "POST":
        # name = request.form["username"]
        a=request.form["pregnancy"]
        b=request.form["glucose"]
        c=request.form["bloodpressure"]
        d=request.form["SkinThickness"]
        e=request.form["insulin"]
        f=request.form["BMI"]
        g=request.form["DiabetesPedigreeFunction"]
        h=request.form["Age"]
        import pandas as pd
        import numpy as np
        df=pd.read_csv("diabetes.csv")

        x=df.iloc[:,0:8].values
        y=df.iloc[:,8].values

        from sklearn.model_selection import train_test_split
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
        from sklearn.preprocessing import StandardScaler
        sc=StandardScaler()
        x_train=sc.fit_transform(x_train)
        x_test=sc.transform(x_test)
        from sklearn.linear_model import LogisticRegression
        Log= LogisticRegression(random_state=0)
        Log.fit(x_train,y_train)
        y_pred=Log.predict(x_test)
        z=Log.predict(sc.transform([[a,b,c,d,e,f,g,h]]))
        if z==1:
            name="YES"
        else:
            name="NO"
        
    return render_template("sub.html",n=name,a1=a,b1=b,c1=c,d1=d,e1=e,f1=f,g1=g,h1=h) 

if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def home():
    return render_template ('home.html')




jacket = [
    {'model': 'Пальто', 'size':56, 'colors':'Черный'},
    {'model': 'Пуховик', 'size':57, 'colors':'красный'},
    {'model': 'Пуховик', 'size':57, 'colors':'красный'}
]

@app.get('/jacket/')
def set_jacket():
    return render_template('jacket.html', jacket=jacket)


shoes= [
    {'model':'Туфли', 'size':40, 'colors':'Красный'},
    {'model':'Кроссовки', 'size':43, 'colors':'Белый'},
    {'model':'Кеды', 'size':45, 'colors':'Черный'},
]

@app.get('/shoes/')
def set_shoes():
    return render_template('shoes.html', shoes=shoes)






if __name__=='__main__':
    app.run(debug=True)
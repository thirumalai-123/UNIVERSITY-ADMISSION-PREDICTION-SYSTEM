@app.route('/')
def home():
    return render_template('Demo2.html')
@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    for rendering results on HTML GUI
    '''
    #min max Scaling
    minl=[290.0,92.0,1.0,1.0,1.0,6.8,0.0]
    maxl=[340.0,120.0,5.0,5.0,5.0,9.92,1.0]
    k=[float(x) for x in request.form.values()]
    p=[]
    for i in range(7):
        l=(k[i]-min1[i])/(maxl[i]-min[i])
        p.append(l)
    prediction = model.predict([p])
    print(prediction)
    output=prediction[0]
    if(output==False):
        return render_template('nochance.html',prediction_text='You Dont have a chance of gettin
        else:
            return render_template('chance.html',prediction_text='You have a chance of getting admis
            if__name__=="__main__" :
              app.run(debug=False)                     

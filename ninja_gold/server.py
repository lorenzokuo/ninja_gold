from flask import Flask, session, redirect, render_template, request
import random, datetime
app=Flask(__name__)
app.secret_key="ThisIsSecret"

@app.route('/')
def goldGame():
    if 'gold' not in session:
        session['gold'] = 0
    if 'dialog' not in session:
        session['dialog'] = []
    return render_template('index.html', x = session['gold'])

@app.route('/process_money', methods=['POST'])
def processMoney():
    print(request.form)
    now = str(datetime.datetime.now())
    if request.form['building'] == 'farm':
        session['num'] = random.randint(10,20)
        session['gold'] += session['num']
        session['dialog'].insert(0, "<p style='color: green'>Earned "+str(session['num'])+" golds from the Farm! ( "+now+" )</p>")

    if request.form['building'] == 'cave':
        session['num'] = random.randint(5,10)
        session['gold'] += session['num']
        session['dialog'].insert(0, "<p style='color: green'>Earned "+str(session['num'])+" golds from the Cave! ( "+now+" )</p>")

    if request.form['building'] == 'house':
        session['num'] = random.randint(2,5)
        session['gold'] += session['num']
        session['dialog'].insert(0, "<p style='color: green'>Earned "+str(session['num'])+" golds from the House! ( "+now+" )</p>")

    if request.form['building'] == 'casino':
        session['num'] = random.randint(-50,50)
        if session['num'] > 0:
            session['gold'] += session['num']
            session['dialog'].insert(0, "<p style='color: green'>Earned "+str(session['num'])+" golds from the Casino! ( "+now+" )</p>")
        if session['num'] <= 0:
            session['gold'] += session['num']
            session['dialog'].insert(0, "<p style='color: red'>Entered a casino and lost "+str(session['num']*-1)+" golds... Ouch.. ( "+now+" )</p>")

    return redirect('/')

@app.route('/reset', methods=['POST'])
def resetSession():
    session.clear()
    return redirect('/')
# end routes
app.run(debug=True)
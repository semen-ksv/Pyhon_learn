from bottle import route, run

@route('/first_page')
def first_page():

    return '<H1 align="center">Питон через браузер!<H1>'

run(host='localhost', port=8080, debug=True)

# http://localhost:8080/first_page показывает код с return

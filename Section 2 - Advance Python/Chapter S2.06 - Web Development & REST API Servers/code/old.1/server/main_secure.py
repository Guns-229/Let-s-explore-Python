#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:57:43 2018.

@author: mayank
"""
from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)
app.config['SESSION_COOKIE_SECURE'] = True


@app.route("/")
def template_test():
    """."""
    return render_template('main.html')


@app.route('/success/')
def success():
    """."""
    return '!!! Welcome Success !!!'


@app.route("/send_clear")
def template_send_clear():
    """."""
    return render_template('jinja_for.html')


@app.route("/form_1", methods=['POST', 'GET'])
def template_form_1():
    """."""
    if request.method == 'GET':
        return render_template('form_submit.html')
    elif request.method == 'POST':
        return redirect(url_for('success'))


@app.route("/form_2", methods=['POST', 'GET'])
def template_form_2():
    """."""
    if request.method == 'GET':
        return render_template('form_bootstrap.html')
    elif request.method == 'POST':
        return redirect(url_for('success'))


@app.route("/form_bootstrap_dropdown", methods=['POST', 'GET'])
def form_bootstrap_dropdown():
    """."""
    if request.method == 'GET':
        return render_template('form_bootstrap_dropdown.html')
    elif request.method == 'POST':
        return redirect(url_for('success'))


@app.route("/form_bootstrap_radiobutton", methods=['POST', 'GET'])
def form_bootstrap_radiobutton():
    """."""
    if request.method == 'GET':
        return render_template('form_bootstrap_radiobutton.html')
    elif request.method == 'POST':
        return redirect(url_for('success'))


@app.route("/form_cb_badge", methods=['POST', 'GET'])
def form_cb():
    """."""
    if request.method == 'GET':
        return render_template('form_bootstrap_checkbox_badge.html')
    elif request.method == 'POST':
        return redirect(url_for('success'))


@app.route("/form_bootstrap_progress", methods=['POST', 'GET'])
def form_bootstrap_progress():
    """."""
    if request.method == 'GET':
        return render_template('form_bootstrap_progress.html')
    elif request.method == 'POST':
        return redirect(url_for('success'))


@app.route("/form_html5_progress", methods=['POST', 'GET'])
def form_html5_progress():
    """."""
    if request.method == 'GET':
        return render_template('form_html5_progress.html')
    elif request.method == 'POST':
        return redirect(url_for('success'))


@app.route("/bootstrap_menu", methods=['POST', 'GET'])
def bootstrap_menu():
    """."""
    if request.method == 'GET':
        return render_template('bootstrap_menu.html')
    elif request.method == 'POST':
        return redirect(url_for('success'))


@app.route("/canvas", methods=['POST', 'GET'])
def canvas():
    """."""
    if request.method == 'GET':
        return render_template('canvas.html')
    elif request.method == 'POST':
        return redirect(url_for('success'))


@app.route("/drag_and_drop", methods=['POST', 'GET'])
def drag_and_drop():
    """."""
    if request.method == 'GET':
        return render_template('drag_and_drop.html')
    elif request.method == 'POST':
        return redirect(url_for('success'))


@app.route("/cookies", methods=['POST', 'GET'])
def cookies():
    """."""
    if request.method == 'GET':
        return render_template('cookies.html')
    elif request.method == 'POST':
        return redirect(url_for('success'))


if __name__ == '__main__':
    # pip install pyopenssl
    # Run the following command to get cert.pem and key.pem
    # `openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365`
    app.run(debug=True, port=4040,
            ssl_context=('cert.pem', 'key.pem'))

#!/usr/bin/env python3

from flask import Flask, request, render_template,render_template_string, make_response, redirect, url_for
import logging

template = f"""
    <!DOCTYPE html>
    <!--[if lt IE 7]> <html class="lt-ie9 lt-ie8 lt-ie7" lang="en"> <![endif]-->
    <!--[if IE 7]> <html class="lt-ie9 lt-ie8" lang="en"> <![endif]-->
    <!--[if IE 8]> <html class="lt-ie9" lang="en"> <![endif]-->
    <!--[if gt IE 8]><!--> <html lang="en"> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>Christmas Present Complaint Form</title>
        <link rel="stylesheet" href="/static/style.css">

        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->
    </head>
    <body>
    <script src="static/snowstorm.js"></script>
    <h1 font-size: 250%; font-weight: normal; text-align: center;>Christmas Present Complaint Form</h1>
        <form action="/" class="contact" onclick="return validateForm()" method="POST">
        <fieldset class="contact-inner">
            <p class="contact-input">
            <input type="text" name="title" placeholder="Message Title" autofocus>
            </p>
            <p class="contact-input">
            <label for="select" class="select">
                <select name="name" id="select">
                <option value="" selected>Choose name…</option>
                <option value="Reindeer Overloard">Reindeer Overloard</option>
                <option value="Chief Elf Slave Driver">Chief Elf Slave Driver</option>
                <option value="Naughty List Legislator">Naughty List Legislator</option>
                </select>
            </label>
            </p>
            <p class="contact-input">
            <textarea name="message" placeholder="Your Message…"></textarea>
            </p>
            <p class="contact-submit">
            <input type="submit" value="Send Message">
            </p>
            <p id='response'>Send your complaint</p>
            <p>
        </fieldset>
        </form>
    """

app = Flask(__name__)
logging.basicConfig(encoding='utf-8', level=logging.WARNING)

@app.route("/",methods=["GET", "POST"])
def contactForm():
    if request.method == "POST":
        title = str(request.form.get("title"))
        name = request.form.get("name")
        message = request.form.get("message")
        logging.info(f"Name is: {name}\nTitle is: {title}\nMessage is: {message}")
        reflect = f"<p id='response'>Your complaint has been sent to {name}.</p>"
        return render_template_string(template.replace("Send your complaint", reflect))
    else:
      return render_template_string(template)

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
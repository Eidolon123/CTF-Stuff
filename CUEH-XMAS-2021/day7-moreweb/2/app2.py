from flask import Flask, request, render_template,render_template_string, make_response, redirect, url_for
import logging
import re

def create_page(reflect=""):
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
    <form action="/" class="contact" onclick="return validateForm()" method="GET">
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
        {reflect}
        <p class="contact-submit">
          <input type="submit" value="Send Message">
        </p>
      </fieldset>
    </form>
  """
  return template

app = Flask(__name__)
logging.basicConfig(encoding='utf-8', level=logging.CRITICAL)
log=logging.getLogger()
def blackList(title, name, message):
  badChars = ["_", "config" , "os", "RUNCMD", "base", "mro", "class"]
  matchName, matchTitle, matchMessage = "", "", ""
  regex = re.compile('|'.join(map(re.escape, badChars)))
  if type(title) == (str or bytes): matchTitle = regex.findall(title)
  if type(name) == (str or bytes):  matchName = regex.findall(name)
  if type(message) == (str or bytes): matchMessage = regex.findall(message)
  if (len(matchTitle) or len(matchName) or len(matchMessage)) >= 1:
    return "<p>Illegal characters detected, how dare you try hack Santa! -_- </p>"
  else:
    return f"<p>Your message to {name} has been sent.</p>"


@app.route("/",methods=["GET", "POST"])
def contactForm():
  if request.method == "GET":
    title = str(request.args.get("title"))
    name = request.args.get("name")
    message = request.args.get("message")
    logging.info(f"Name is: {name}\nTitle is: {title}\nMessage is: {message}")
    if (title != None) or (name != None) or (message != None):
      reflect = blackList(title, name, message)
      return render_template_string(create_page(reflect=reflect))
    return render_template_string(create_page())

if __name__ == "__main__":
  app.run("0.0.0.0", port=5000, debug=True)

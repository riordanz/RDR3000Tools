from flask import *
from flask import request as req
from flask_cors import *
from RDRTools import *
import os.path, json, base64, os

app = Flask(__name__)
CORS(app)
bypass = Bypasser()
BD = BatchDownloader()

def toHtml(page, ext = "html"):
    if os.path.isfile("templates/%s.%s" % (page, ext)):
        return Markup(open("templates/%s.%s" % (page, ext)).read())
    else:
        return None
@app.route('/api/<action>/<url>')
@app.route('/api/<action>/<url>/<judul>')
def api(action, url, judul = ""):
    global bypass, BD
    if action == "terbit21":
        if judul != "":
            if url == "search":
                s = bypass.terbit21(url, judul)
                return s if s is not None else jsonify([])
            elif url == "link":
                s = bypass.terbit21("get_link", judul)
                return s if s is not None else jsonify([])
            return jsonify([])
        else:
            s = bypass.terbit21(url)
            return jsonify(s) if s is not None else jsonify([])
    elif action == "kuyhaa":
        data = bypass.kuyhaa(url)
        if data:
            return jsonify(data)
        return jsonify([])
    elif action == "gigapurbalingga":
        data = bypass.gigapurbalingga(url)
        if data:
            return jsonify(data)
        return jsonify([])
    elif action == "oploverz":
        data = bypass.oploverz(url)
        if data:
            return jsonify(data)
        return jsonify([])
    elif action == "nimegami":
        data = bypass.nimegami(url)
        if data:
            return jsonify(data)
        return jsonify([])
    elif action == "pahe":
        data = bypass.pahe(url)
        if data:
            return jsonify(data)
        return jsonify([])
    elif action == "batch":
        if url == "mediafire":
            try:
                data = base64.b64decode(req.args.get('url')).decode("utf-8")
                if len(data.split("\n")) <= 0:
                    return jsonify(['0'])
            except:
                return jsonify(['error'])
            s = BD.mediafire(data.split("\n"))
            return jsonify({"msg" : "success"}) if s is not None else jsonify([])
        return jsonify([])

@app.route("/")
def main():
    return render_template("template.html", data=toHtml("home"))

@app.route("/film/<web>")
def film(web):
    if web == "terbit21":
        return render_template("template.html", data=toHtml("film/terbit21"))
    elif web == "pahe":
        return render_template("template.html", data=toHtml("film/pahe"))
    else:
        return render_template("404.html")

@app.route("/software/<web>")
def software(web):
    if web == "gigapurbalingga":
        return render_template("template.html", data=toHtml("software/giga"))
    elif web == "kuyhaa":
        return render_template("template.html", data=toHtml("software/kuyhaa"))
    else:
        return render_template("404.html")

@app.route("/anime/<web>")
def anime(web):
    if web == "oploverz":
        return render_template("template.html", data=toHtml("anime/oploverz"))
    elif web == "nimegami":
        return render_template("template.html", data=toHtml("anime/nimegami"))
    else:
        return render_template("404.html")
@app.route("/batch/<web>")
@app.route("/batch/<web>/<action>")
def batch(web, action = ""):
    if web == "mediafire":
        if not action:
            return render_template("template.html", data=toHtml("batch/mediafire"))
        elif action == "download":
            return session["_id"]
            # return send_file("mediafire.zip", as_attachment = True)

app.run(host = '0.0.0.0', debug = True)
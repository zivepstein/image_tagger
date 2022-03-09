from flask import Flask,render_template, url_for, redirect
import pandas as pd
import os
from os import listdir
import argparse
from os.path import isfile, join

parser = argparse.ArgumentParser()

app = Flask(__name__)

parser.add_argument('--folder', type=str, default = '')
parser.add_argument('--datasheet', type=str, default = '')
args = parser.parse_args()

print(args.folder)

if args.folder == '' and args.datasheet == "":
	print("no data specified...")
elif args.folder == '':
	images = pd.read_csv(args.datasheet)
	urls = images['urls'].values
	ids = images['index'].values
	num_pages = int(float(len(ids))/100)
else:
	mypath= "static/data/" + args.folder
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	onlyfiles_abs = [mypath.replace("static/","") + "/" + f.replace(" "," ") for f in listdir(mypath) if isfile(join(mypath, f))]
	df = pd.DataFrame({"name":onlyfiles, "url": onlyfiles_abs, "index" : range(1,1+len(onlyfiles))})
	df.to_csv("static/data/{}.csv".format(args.folder))
	urls = df['url']
	ids = df['index']
	num_pages = int(float(len(ids))/100)

@app.route('/')
def hello_world_base():
	return(redirect(url_for('hello_world', page=0)))

@app.route('/<page>')
def hello_world(page):
	page = int(page)
	si = page*100
	endi = (page+1)*100
	print(urls.values)
	print(urls.values[si:endi])
	return render_template('index.html', assets = zip(ids[si:endi],urls[si:endi]), page = page, num_pages = num_pages)

if __name__ == '__main__':
    app.run()
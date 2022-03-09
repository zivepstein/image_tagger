from flask import Flask,render_template, url_for
import pandas as pd
import os
from os import listdir
import argparse
from os.path import isfile, join

parser = argparse.ArgumentParser()

app = Flask(__name__)

from_data = False
parser.add_argument('--folder', type=str, default = '')
args = parser.parse_args()

print(args.folder)

if from_data:
	images = pd.read_csv("images.csv")
	people = images[images['ooi']=='person']
	urls = people['s3_transformed'].values
	ids = people['Unnamed: 0'].values
	num_pages = int(float(len(ids))/100)
else:
	folder = 'contentwarning_generations5'
	mypath= "static/data/" + folder
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	onlyfiles_abs = [mypath.replace("static/","") + "/" + f.replace(" "," ") for f in listdir(mypath) if isfile(join(mypath, f))]
	df = pd.DataFrame({"name":onlyfiles, "url": onlyfiles_abs, "index" : range(1,1+len(onlyfiles))})
	df.to_csv("static/data/{}.csv".format(folder))
	urls = df['url']
	ids = df['index']
	num_pages = int(float(len(ids))/100)



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
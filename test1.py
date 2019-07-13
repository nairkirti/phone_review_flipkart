from flask import Flask, render_template, request
from webscrapper import scrape_page
#from flask_table import Table, Col

#class ItemTable(Table):
 #   review_text = Col('Review')
  #  author = Col('Name')

#class Item(object):
 #   def __init__(self, authorname, reviewtext):
  #      self.authorname = authorname
   #     self.reviewtext = reviewtext
        
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("showreviews.html")
#response = ""
@app.route("/submit/", methods=['POST'])
def readurl():
    url_text = request.form['url_text']
    response = scrape_page(url_text)
    #table=ItemTable(response)
    #print(table.__html__())
    #return "done"
    #for i in response:
    #    
    return render_template("showreviews.html",insert_status = response)  


if __name__=="__main__":
    app.run(debug=True)
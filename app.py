import streamlit as st
# import module
import requests
from bs4 import BeautifulSoup
import csv
import re
import pandas as pd


# def add_numbers(num1, num2):
#     return num1 + num2

def scrapper( tag, Page):


    # link for extract html data
    # Making a GET request


    def getdata(url):
      r = requests.get(url)
      return r.text

    #Var Created
    Title = []
    Author = []
    Cat = []
    All = []
    author_link = []
    dic = {"Article": Title, "Author": Author, "Category": Cat, "Link": author_link}


    # url
    for i in range(Page+1):
        st.success(f"Processing page : {i}", icon="✅")
        url = "https://www.analyticsvidhya.com/blog/category/"+tag+"/page/"+str(i)


        # pass the url
        # into getdata function
        htmldata = getdata(url)
        soup = BeautifulSoup(htmldata, 'html.parser')

        All = []
        # traverse author name
        for i in soup.find_all("div", "list-card-content"):
            All.append(i.get_text().split("\n"))

        # attribute starting with "https://"
        for link in soup.find_all('a',
                                attrs={'href': re.compile("^https://www.analyticsvidhya.com/blog/author/")}):
            # display the actual urls
            author_link.append(link.get('href'))


        for i in All:
            Title.append(i[1])
            Author.append(i[3])
            Cat.append(i[-2])

    df = pd.DataFrame(dic) 
        
    # saving the dataframe 
    df.to_csv('Result.csv')
    return("Completed")


def main():
    st.title("Scrapper App")
    st.write("Enter Tag and Number of pages to get the Result.")

    tag = st.text_input("Category: ")
    Page = st.number_input("Number of Pages :", step=1)

    if st.button("Export to CSV"):
        result = scrapper( tag, Page)
        st.success("True")

if __name__ == "__main__":
    main()

    

 

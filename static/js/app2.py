# import necessary libraries
from sqlalchemy import func

from flask import Flask, render_template, jsonify

import bellybutton_diversity as bd

from flask import (
    Flask,
    render_template,
    jsonify,
    redirect)


# from bellybutton_diversity import json_otu

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################


# Query the database and send the jsonified results

@app.route("/")
def home():
    """Return the dashboard homepage."""
    return render_template("index.html")

@app.route("/names")
def samples():
    
    return jsonify(bd.samples_header)


@app.route("/otu")
def otu_desc():
    
    return jsonify(bd.otu_desc)

@app.route("/metadata/<sample>")
def sample_metadata(sample):

    def get_num_from_string(string):  
        num = ''  
    # Loop through characters in the string  
        for i in string:  
            # If one of the characters is a number, add it to the empty string  
            if i in '1234567890':  
                num+=i  
        # Convert the string of numbers to an integer  
        integer = int(num)  
        return integer  

    string= sample
    
    sample_id = get_num_from_string(string)


    
    return jsonify(bd.metadata_dict[sample_id])


@app.route("/wfreq/<sample>")
def sample_wfreq(sample):

    def get_num_from_string(string):  
        num = ''  
    # Loop through characters in the string  
        for i in string:  
            # If one of the characters is a number, add it to the empty string  
            if i in '1234567890':  
                num+=i  
        # Convert the string of numbers to an integer  
        integer = int(num)  
        return integer  

    string= sample
    
    sample_id = get_num_from_string(string)


    
    return jsonify(bd.metadata_dict[sample_id]['WFREQ'])

@app.route("/samples/<sample>")
def samples_sample(sample):

    temp_df=bd.samples_df[[sample]]

    temp_df = temp_df.sort_values(sample, ascending=False)

    temp_df=temp_df.fillna(0)

    # temp_df

    sample_values = temp_df[sample].tolist()


    otu_id_list = temp_df.index.tolist()

    otu_id_list=list(map(int, otu_id_list))

    samples_dict = {"otu_id":otu_id_list, "sample_values":sample_values}

    # print(samples_dict)

    samples_list=[]
        
    samples_list.append(dict(samples_dict))


    
    return jsonify([samples_list])



# # create route that renders index.html template
# @app.route("/")
# def home():
#     return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
import datetime
from pathlib import Path
import json, sys
import easyocr
import os

def imageToJson(path, lang="en"):
    reader = easyocr.Reader([lang])
    lines  = reader.readtext(path, detail=0, paragraph=True)
    result =  " ".join(lines)

    return result

def extractTextFromImage(request):

    now = datetime.datetime.now()

    formatted_date_time = now.strftime("%A, %B %d, %Y %I:%M %p")
    data = request.form
    uploaded_file = request.files['file']
    user_id =data['user_id']

    title =f'{uploaded_file.filename}-{now}' 
    file_path=f"uploads/{uploaded_file.filename}"
    uploaded_file.save(file_path)
    result= imageToJson(file_path)
    os.remove(file_path)
    temp_url="https://rccd.edu/news/publishing-images/2022_2023/STEM_NASA_FLYER.png"
    return {"title":title,"user_id":user_id,"description": result,"image_url": temp_url}



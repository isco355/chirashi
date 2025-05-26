import datetime


def extractTextFromImage(request):

    now = datetime.datetime.now()

    formatted_date_time = now.strftime("%A, %B %d, %Y %I:%M %p")
    data = request.form
    uploaded_file = request.files['file']
    user_id =data['user_id']

    title =f'{uploaded_file.filename}-{now}' 
    temp_url="https://rccd.edu/news/publishing-images/2022_2023/STEM_NASA_FLYER.png"
    return {"title":title,"user_id":user_id,"description": "placeholder description","image_url": temp_url}



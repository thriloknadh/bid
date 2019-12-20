def sendSMS(contact,mess):
    import requests
    url="https://www.fast2sms.com/dev/bulk"
    payload="sender_id=FSTSMS&message="+mess+"&language=english&route=p&numbers="+contact
    headers={
        'authorization':'FHU1m7xQXWV5Yr0IbjNtSh8ilOcRLM6JnBeZzTdPouqGvCp92fL8s01RJ4gzVQk2ndOf6HGCrZowNKP5',
         'Content-Type':"application/x-www-form-urlencoded",
        'Cache-Control':"no-cache",
        }
    response=requests.request("POST",url,data=payload,headers=headers)
    s1=response.text
    return s1
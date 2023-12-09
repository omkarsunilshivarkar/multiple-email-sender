import smtplib as s 
ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('your gmail id','your gmail app password')
subject="test python"
body="i love python"
message="subject:{}\n\n{}".format(subject,body)
listadd=['omkarsunilshivarkar@gmail.com','shivarkarsunilomkar@gmail.com']
ob.sendmail('omkarsunilshivarkar@gmail.com',listadd,message)
print('mail sent')
ob.quit()
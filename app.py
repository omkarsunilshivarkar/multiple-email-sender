import smtplib as s 
ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('sender gmail id','sender gmail app password')
subject="test python"
body="i love python"
message="subject:{}\n\n{}".format(subject,body)
listadd=['receiver gmail address 1','receiver gmail address 2']
ob.sendmail('sender gmail address',listadd,message)
print('mail sent')
ob.quit()
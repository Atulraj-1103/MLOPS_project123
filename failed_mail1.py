{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import smtplib \n",
    "# creates SMTP session \n",
    "s = smtplib.SMTP('smtp.gmail.com', 587) \n",
    "# start TLS for security \n",
    "s.starttls()   \n",
    "# Authentication \n",
    "s.login(\"sender-mail\", \"password\") \n",
    "# message to be sent \n",
    "message = \"Hey Developer, you need to check your code once. Might be this have some error. \n",
    "\"\n",
    "# sending the mail \n",
    "s.sendmail(\"sender-mail\", \"developer_mail\", message) \n",
    "# terminating the session \n",
    "s.quit()\n",
    "\n",
    "   "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

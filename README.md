# Line-Bot-and-API-demonstration 
This is a message app chat bot and API demonstration.

## About this repositary 
This README is going to be ritten in English although Line is an Message app only popular in Taiwan.  
You might need know **mandairn** but you can trasnlate the webpage into your perfer language by google translate in google Chrome via right click.  
There is a Chrome extension called [Google Translate](https://chrome.google.com/webstore/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb/RK%3D2/RS%3DBBFW_pnWkPY0xPMYsAZI5xOgQEE-). This extension can translate words show on the webpage.  

This is just to show how to use a API in google colab.
I **DO NOT** recommand this app at all because of the reasons below:
* Your older photos or files in the chat will be "Expired" after some days.
* It's a Buggy  App.
* The App is slow.
* The app takes a lot of storage from your phone even if you clean all the chches and chat history.
* The app is full of ads.
* The UI/UX is so bad. 
* It's just like a bloatware.


## Things used in this project. 
* [ ] Internet

* [ ] A computer

* [ ] Ngrok authorizationth key[Ngrok site](https://ngrok.com/)

* [ ] Taiwanese Central Weather Bureau API authorizationth key ([Website](https://opendata.cwb.gov.tw/index))
* [ ] Google colab  ([about colab](https://research.google.com/colaboratory/faq.html#:~:text=Using%20Colab&text=Colab%20notebooks%20are%20stored%20in,Google%20Drive%20file%20sharing%20instructions.))

* [ ] Line account

* [ ] A phone

## Q&A 
Q: Why do you use colab?  
A: It's easy to use and in this case it's a better choice.  

Q: Is colab free and safe?  
A: Yes, I think. It's a google product.([Colab Q&A](https://research.google.com/colaboratory/faq.html#:~:text=Using%20Colab&text=Colab%20notebooks%20are%20stored%20in,Google%20Drive%20file%20sharing%20instructions))  

Q: Any other app for coding?  
A: I always strongly recommand <a href="https://code.visualstudio.com/">VSCode</a> for coding.  

Q: Why do you choose Taiwanese Central Weather Bureau API?  
A: Because it's a free API and it's a great weather source in Taiwan.  

Q: Is this hard?  
A: I don't think so, if you like code then it's great.  

Q: Is this free to use?  
A: It's free, You can also copy my code.  

Q: Why do you do this?  
A: Because I love coding and as a CS student, I think this might help for my further career. Moreover, I want to help people to have a place to learn.  

# Install and setup in google colab

Download Ngrok and unzip the file
```
!wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz -O ngrok-v3-stable-linux-amd64.tgz
!tar xzvf ngrok-v3-stable-linux-amd64.tgz
```
Install Ngrok  
PIP is a package manager for Python packages, or modules if you like.  
Usually er only need to use **pip install** instad of **!pip install** while using VSCode.[pip documentation](https://pip.pypa.io/en/stable/#)or[install pip](https://pypi.org/project/pip/)
```
!pip install pyngrok
```
[Line bot api](https://developers.line.biz/en/docs/messaging-api/overview/)
```
!pip install line-bot-sdk
```

```
!pip install flask_ngrok
```

Now, let's set the authorizationth token.  
Please put your authorizationth cone in the **"Your authorizationth token"**

```python
from pyngrok import ngrok, conf
ngrok.set_auth_token("Your authorizationth token")
```

```python
from pyngrok import ngrok
def connNgrok():
	port=5000

	public_url=ngrok.connect(port, bind_tls=True).public_url
	print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}/\"".format(public_url, port))
```


# Functions

⚠️ This might not work at the time you are reading.
The reason is because API provider might change the key word in their **JSON** file.

```python

```

```python

```

```python

```

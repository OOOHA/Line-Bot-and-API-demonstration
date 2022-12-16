<h1> Line-Bot-and-API-demonstration </h1>
This is a message app chat bot and API demonstration.

<h2> About this repositary </h2>
<p>This README is going to be ritten in English although Line is an Message app only popular in Taiwan.<br />
   You might need know <strong> mandairn</strong> but you can trasnlate the webpage into your perfer language by google translate in google Chrome via right click.<br />
   This is just to show how to use a API in google colab.
I <strong> DO NOT </strong> recommand this app at all because of the reasons below:</p>
<ol>
  <li> Your older photos or files in the chat will be "Expired" after some days.</li>
  <li> It's a Buggy  App.</li>
  <li> The App is slow. </li>
  <li> The app takes a lot of storage from your phone even if you clean all the chches and chat history.</li>
  <li> The app is full of ads. </li>
  <li> The UI/UX is so bad. </li>
  <li> It's just like a bloatware. </li>
</ol>

<h2>Things used in this project. </h2>
<ol>
  <li> Internet </li>
  <li> A computer </li>
  <li> Ngrok authorizationth key</li>
  <li> Taiwanese Central Weather Bureau API authorizationth key (<a href="https://opendata.cwb.gov.tw/index">Website</a>)</li>
  <li> Google colab  (<a href = "https://research.google.com/colaboratory/faq.html#:~:text=Using%20Colab&text=Colab%20notebooks%20are%20stored%20in,Google%20Drive%20file%20sharing%20instructions.">about colab</a>)</li>
  <li> Line account </li>
  <li> A phone. </li>
</ol>

<h2> Q&A </h2>
<ol>
  <li> Why do you use colab? </li>
   <p>A: It's easy to use and in this case it's a better choice. </P>
  <li> Is colab free and safe? </li>
   <p>A: Yes, I think. It's a google product.(<a href = "https://research.google.com/colaboratory/faq.html#:~:text=Using%20Colab&text=Colab%20notebooks%20are%20stored%20in,Google%20Drive%20file%20sharing%20instructions.">colab Q&A</a>)
  <li> Any other app for coding? </li>
   <p>A: I always strongly recommand <a href="https://code.visualstudio.com/">VSCode</a> for coding.</P>
  <li> Why do you choose Taiwanese Central Weather Bureau API?</li>
   <p>A: Because it's a free API and it's a great weather source in Taiwan.</P>
  <li> Is this hard? </li>
   <p>A: I don't think so, if you like code then it's great.</P>
  <li> Is this free to use? </li>
   <p>A: It's free, You can also copy my code.</P>
  <li> Why do you do this? </li>
   <p>A: Because I love coding and as a CS student, I think this might help for my further career. Moreover, I want to help people to have a place to learn.</P>
</ol>

<h1> Install enviroment in google colab</h1>

```python
!wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz -O ngrok-v3-stable-linux-amd64.tgz
!tar xzvf ngrok-v3-stable-linux-amd64.tgz
```

```python
!pip install pyngrok
```
<p>Now, let's set the authorizationth token.<br />
   Please put your authorizationth cone in the <strong>"Your authorizationth token"</strong>
</p>

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

```python
!pip install line-bot-sdk
```

```python
!pip install flask_ngrok
```

```python

```

```python

```

```python

```

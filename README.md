<h1 align=center>TCP Chat Room</h1>

<p>Simple TCP Chat Project made with <a href='https://docs.python.org/3/library/socket.html'>sockets</a> using python language.</p>

**NOTE : In order to run and connect the client from an external server(another pc), follow the following steps >**

**Run the `server.py` file first before running/connecting the `client.py`.**


<h1><code>server.py file</code></h1>

```python
#in server.py
HOST = 'localhost'
PORT = 9999
```

`localhost` refers to the machine in which the script is running in.
<p></p>

`PORT = 9999` is a random port for connecting to the server. This can be changed as per the user, but it has to be changed in both `server.py` as well as `client.py`. 

<h1><code>client.py file</code></h1>

```python
#in client.py
HOST = 'localhost'
PORT = 9999
```

As you may have noticed, both the <a href = 'Socket-Files/client.py'>client</a> and sever uses a `HOST` and `PORT` to connect with each other.

 Therefore, they have to be on the same `HOST` and `PORT` in order to connect.

<h1 align=center><code>client.py</code> and <code>server.py</code> on different machines.</h1>

You may have been wondering that it is possible to run the `server.py` and `client.py` but, running the same files on the same machine is not fun. 

Then how can we use server in another machine and connect the client from another machine?


**Note : The different machines you're using to connect with each other has to be on the same network(e.g., Connected to the same router)**

Im using my router for this process.


> Step 1 : Connecting to the same network

To connect different machines with each other on same network, you have to `run` the `server.py` with your local ip address.

:bulb: You can get your local ip address with `ipconfig` command on Windows and `ifconfig` command on Linux/Mac.




```python
#local IP should look something like this
> 192.168.0.108
```

> Step 2 : Hosting the `server.py` on the local ip

Now, we've got our local IP and the next thing we have to do is to `HOST` the `server.py` on that IP.

```python
#in server.py
HOST = '192.168.0.108'
PORT = 9999
#You can choose any port exceeding to the value 65,535
```

Now, our `server.py` is running on our local IP(our IP with the Router) and we've completed most of the process.

> Step 3 : Connecting `client.py` with `server.py`

Now, our server is running on the Local IP and our `client.py` is connected to the same network as our `server.py`.

All that is left is to connect our client to the server on the Local IP.

It can be done by changing the `HOST` and `PORT` in `client.py`

```python
#in client.py
HOST = '192.168.0.108'
PORT = 9999
```

Ok, so now the client and the server are connected to the same network and running on the same network.

Only thing left is the demonstration!

*NOTE : unfortunately i don't have 2 devices to show you but the scripts will run just fine if you try on different devices.*

> Step 4 : Demonstration


<img src='readme-media\Tcp-chat-test.gif' align=center></img>



So, the chat works as expected, i know there are scope of improvements which i'm working on!

There will be new features in the near future, for now if you have any suggestions, you can send them via <a href='fallencat.user@gmail.com'>Email</a>!

For further updates on this project, **Star the Repo**, it really means a lot!

Peace.

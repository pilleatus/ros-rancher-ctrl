### ros-rancher-ctrl
With this package it is possible to call some functions from the RANCHER REST API, with a ROS Action.

#### dependencies
```
sudo pip install gdapi-python
```

#### Quick start
Make sure that they have set the following environment variables
```
export RANCHER_ACCESS_KEY=<access_key>
export RANCHER_SECRET_KEY=<secret_key>
export RANCHER_URL=<url_with_port>
```
If you do not have these keys already. You can create a new API key on the RANCHER web interface.

#### some valid ROS Messages
| scope   	| command  	         | nodes   	          |
|-----------|--------------------|--------------------|
| service   | activate           | vocon-asr          |
|   	    	| deactivate    	   | vocon-asr          |
|   	    	| remove  	         | ork	    	        |

| stack     | deactivateservices | people-detection	  |
|           | activateservices   | slam    	          |
|           | remove             | slam    	          |

| container | start              | x11-rviz-1      	  |
|           | stop               | x11-node-manager-1 |
|           | restart            | camera-xtion-1     |
|           | remove             | camera-xtion-1     |

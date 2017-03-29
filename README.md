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
| scope   	| command  	         | nodes   	        |
|-----------|--------------------|------------------|
| service   | activate           | vocon-asr        |
|   	    	| deactivate    	   | vocon-asr        |
|   	    	| restart    	       | [arm, moveit]    |
|   	    	| remove  	         | ork	    	      |
|-----------|--------------------|------------------|
| stack     | deactivateservices | people_detection	|
|           | activateservices   | slam    	        |
|           | remove             | slam    	        |
|-----------|--------------------|------------------|
| container | start              | rviz           	|
|           | stop               | node-manager     |

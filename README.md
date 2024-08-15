## Real-Time Collaborative Drawing and Chat Application

*Visit:* http://app-envs.eba-mkzqqbgw.us-west-2.elasticbeanstalk.com/

**Overview**
This application provides a platform for users to engage in real-time collaborative drawing and chat sessions. Users can create rooms, invite others, and interact through drawing and text-based communication.

**Technologies**
* **Backend:** Django
* **Real-time Communication:** Django Channels
* **Data Storage:** Redis
* **Deployment:** AWS (Elastic Beanstalk or EC2)

**Features**
* User authentication and registration
* Room creation and management
* Real-time collaborative drawing canvas
* Real-time chat functionality within rooms

**Known Issues**
Currently, the application experiences performance bottlenecks due to limitations in the Redis tier, impacting canvas and chat responsiveness.

**Deployment**
The application is deployed to AWS using [Elastic Beanstalk or EC2]. Detailed deployment instructions can be found in the respective configuration files.

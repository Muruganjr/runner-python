# runner-python

4. Steps to Deploy on Kubernetes

    Set Up Kubernetes on EC2 with kubeadm: Ensure you have a Kubernetes cluster up and running on EC2 using kubeadm. Follow this guide for setting up a single master and worker node on your EC2 instance.

    Create a Namespace: Create the namespace webapps to separate your applications.

    bash

kubectl create namespace webapps

Deploy the Application: Use the deployment file to deploy the Python app.

bash

    kubectl apply -f deployment-service.yaml

    This command will create a deployment and a service to expose the application on port 8000.

    Update Docker Image: When you push a new version of the Docker image to Docker Hub, GitHub Actions will automatically update the Kubernetes deployment with the new image using the kubectl set image command.

5. Run and Monitor the Application

Once the application is deployed:

kubectl get deployments -n webapps

Check the service and get the external IP:

kubectl get svc -n webapps

Test the application by visiting the external IP on port 8000:

arduino

    http://<EXTERNAL_IP>:8000

Conclusion

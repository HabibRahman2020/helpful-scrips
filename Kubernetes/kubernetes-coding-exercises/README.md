# Kubernetes Coding Exercises

This repository contains a set of coding exercises related to Kubernetes along with their solutions. Each exercise focuses on a specific aspect of Kubernetes deployment and configuration.

## Exercises

1. [Exercise 1: Deploying NGINX Pod and Service](exercise-1/README.md)
2. [Exercise 2: Creating a Deployment](exercise-2/README.md)
3. [Exercise 3: Working with ConfigMaps](exercise-3/README.md)
4. [Exercise 4: Configuring PersistentVolume and PersistentVolumeClaim](exercise-4/README.md)
5. [Exercise 5: Horizontal Pod Autoscaling](exercise-5/README.md)
6. [Exercise 6: Running a Job](exercise-6/README.md)
7. [Exercise 7: Scheduling a CronJob](exercise-7/README.md)
8. [Exercise 8: Managing ServiceAccounts and RoleBindings](exercise-8/README.md)
9. [Exercise 9: Implementing Network Policies](exercise-9/README.md)
10. [Exercise 10: Configuring Ingress Routing](exercise-10/README.md)

## Solutions

The solutions for each exercise can be found in their respective directories. Here's a quick overview of each exercise and its corresponding solution:

1. Exercise 1: Deploying NGINX Pod and Service
   - Solution: [nginx-pod.yaml](exercise-1/nginx-pod.yaml), [nginx-service.yaml](exercise-1/nginx-service.yaml)

2. Exercise 2: Creating a Deployment
   - Solution: [my-app-deployment.yaml](exercise-2/my-app-deployment.yaml)

3. Exercise 3: Working with ConfigMaps
   - Solution: [my-config-configmap.yaml](exercise-3/my-config-configmap.yaml)

4. Exercise 4: Configuring PersistentVolume and PersistentVolumeClaim
   - Solution: [my-pv-pvc.yaml](exercise-4/my-pv-pvc.yaml)

5. Exercise 5: Horizontal Pod Autoscaling
   - Solution: [my-app-hpa.yaml](exercise-5/my-app-hpa.yaml)

6. Exercise 6: Running a Job
   - Solution: [time-job.yaml](exercise-6/time-job.yaml)

7. Exercise 7: Scheduling a CronJob
   - Solution: [backup-cronjob.yaml](exercise-7/backup-cronjob.yaml)

8. Exercise 8: Managing ServiceAccounts and RoleBindings
   - Solution: [my-service-account.yaml](exercise-8/my-service-account.yaml), [my-service-account-rolebinding.yaml](exercise-8/my-service-account-rolebinding.yaml)

9. Exercise 9: Implementing Network Policies
   - Solution: [network-policy.yaml](exercise-9/network-policy.yaml)

10. Exercise 10: Configuring Ingress Routing
    - Solution: [my-ingress.yaml](exercise-10/my-ingress.yaml)

Feel free to explore each exercise and its solution. These exercises cover various Kubernetes concepts and will help you practice and improve your Kubernetes skills.

## Tips and Tricks

Here are some additional tips and tricks to enhance your Kubernetes knowledge and usage:

1. Use `kubectl` Cheat Sheet: Familiarize yourself with the `kubectl` command-line tool and its various commands. You can find a cheat sheet [here](https://kubernetes.io/docs/reference/kubectl/cheatsheet/).

2. Leverage Labels and Selectors: Utilize labels and selectors to organize and manage your Kubernetes resources effectively. They enable you to group and select specific resources based on custom criteria.

3. Explore Resource Definitions: Study and understand different Kubernetes resource definitions, such as Pods, Deployments, Services, ConfigMaps, and PersistentVolumes. Experiment with their configurations and explore the available options.

4. Understand Networking Concepts: Learn about Kubernetes networking concepts, including Services, Ingress, Network Policies, and DNS resolution. Understand how these components interact and enable communication within the cluster.

5. Practice with Helm: Explore Helm, a popular package manager for Kubernetes. Helm allows you to define, install, and manage applications as Helm charts, simplifying the deployment and management of complex applications.

Remember, continuous learning and hands-on practice are key to mastering Kubernetes. Happy coding and Kubernetes exploration!


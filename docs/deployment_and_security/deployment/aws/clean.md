# Clean

The following procedure explains how to delete the platform. The full procedure takes around 45m to 1h to be completed.
To clean up **YData Fabric**, you will need to delete the CloudFormation stack and remove the subscription. 

Please take in consideration that this will delete **everything associated with the installation**.

## Deleting the stacks
- Go to the regions where the product is installed
- Go to the *CloudFormation* service
- Select the *ydata stack*
- Click in the **Delete** button

![delete stack](../../../assets/deployment_security/aws/delete_stack.png){: style="width:65%"}

- Select the Extension stack and click in the **Delete** button.

!!! Note
    
    This will disable the extension. If you are using this extension for any other project, please do not delete this stack.

![EKS cluster delete](../../../assets/deployment_security/aws/eks_cluster_delete.png){: style="width:65%"}

## Deleting the subscription
- Go to the ^^[**AWS Marketplace Subscriptions](https://console.aws.amazon.com/marketplace/home?region=eu-west-1)^^** → Manage subscriptions
- Click the *YData product*

![ydata product](../../../assets/deployment_security/aws/ydata_subscription.png){: style="width:65%"}

- **Actions → Cancel** subscription
- Click the checkbox and click *Yes*, cancel subscription

![cancel](../../../assets/deployment_security/aws/cancel_subscription.png){: style="width:65%"}

Following the above steps completes the process of deleting YData Fabric from your AWS Cloud instance.

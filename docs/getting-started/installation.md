
YData SDK is generally available through both Pypi and Conda allowing an easy process of installation. This experience allows combining YData SDK with other packages such as Pandas, Numpy or Scikit-Learn. 

YData SDK is available for the general public through a token-based authentication system. If you don’t have one yet, you can get your free license key during the installation process. You can check what features are available in the free version here.

##Installing the package
YData SDK supports python versions bigger than python 3.8, and can be installed in Windows, Linux or MacOS operating systems. 

Prior to the package installation, it is recommended the creation of a virtual or conda environment:
=== "pyenv"
    ``` commandline
    import tensorflow as tf
    ```

=== "conda env" 
    ``` commandline
    conda create --name ydata
    ```

And install `ydata-sdk`

=== "pypi"
    ``` commandline
    pip install ydata-sdk
    ```
=== "conda-forge"
    ``` commandline
    pip install ydata-sdk
    ```

##Authentication
Once you've installed `ydata-sdk` package you will need a token to run the functionalities.
YData SDK uses a token based authentication system. To get access to your token, you need to create a YData account.

YData SDK offers a free-trial and an enterprise version. To access your free-trial token, you need to create a [YData account](https://ydata.ai/ydata-fabric-free-trial).

The token will be available [here](https://fabric.ydata.ai), after login:

![SDK Token](../assets/fabric_sdk_token.png){: style="height:450px;width:750px;align:center"}

With your account toke copied, you can set a new environment variable `YDATA_TOKEN` in the beginning of your development session.

``` python
    import os
    
    os.setenv['YDTA_TOKEN'] = '{add-your-token}'
```

Once you have set your token, you are good to go to start exploring the incredible world of data-centric AI and smart synthetic data generation! 

[Add here a quick gif]

Check out our [quickstart](https://ydata-sdk.ydata.ai/0.0/getting-started/quickstart/) guide!

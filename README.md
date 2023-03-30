# Choose Context

This script is to facilitate changing contexts between many kubernetes clusters configs.

Some dependecies to use this:
- [Kubernetes][kube-py] and [Pyinstaller][pyinstaller] libs
- Python version >= 3.10.6

Run this to install requirements:
```
pip install -r requirements.txt
```

After install these libs, run:
```
pyinstaller -F choose.py #the script name can be anyone 
```

This will create one file in `dist/` with name of your script, copy that file to your `/bin` directory and enjoy changing contexts in a easier way

# Usage

Run `choose` and pick one of the numbers according to the context you want to use

```
$ choose

0-arn:aws:eks:us-east-1:
1-arn:aws:eks:us-east-1:
2-arn:aws:eks:us-east-1:
3-arn:aws:eks:us-east-1:
4-arn:aws:eks:us-east-1:
Choose one context to load according to the number.:

Choose one context to load according to the number.: 1
Switched to context "arn:aws:eks:us-east-1:".
Context loaded: arn:aws:eks:us-east-1:
```

[//]: # (important links)
[pyinstaller]: <https://pypi.org/project/pyinstaller/>
[kube-py]: <https://github.com/kubernetes-client/python/>
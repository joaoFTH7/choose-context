# Choose Context

This script is to facilitate changing contexts between many kubernetes clusters configs.

Some dependecies to use this:
- [kubectl][kubectl] the Kubernetes command-line tool
- [Kubernetes][kube-py] and [Pyinstaller][pyinstaller] libs
- Python version >= 3.10.6

Run this to install requirements:
```
pip install -r requirements.txt
```

After install these libs, run:
```
pyinstaller -F main.py -n choose
```
Pyinstaller parameters used:
```bash
-F Create a one-file bundled executable.
-n Name to assign to the bundled app and spec file "(default: first script's basename)"
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
Choose one context to load according to the number.: 1
Switched to context "arn:aws:eks:us-east-1:".
Context loaded: arn:aws:eks:us-east-1:
```

[//]: # (important links)
[kubectl]: <https://kubernetes.io/docs/tasks/tools/>
[pyinstaller]: <https://pypi.org/project/pyinstaller/>
[kube-py]: <https://github.com/kubernetes-client/python/>
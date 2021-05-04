# Telescope


![GitHub repo size](https://img.shields.io/github/license/michal-siedlecki/telescopeWebApp)
![GitHub repo size](https://img.shields.io/github/repo-size/michal-siedlecki/telescopeWebApp)


Telescope is a no framework web app cookiecutter that allows begginers to do quickly create pure python web application.
It can be used also to learn concepts of http and backend web development.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed `python` >= 3.7.2
* You have a `<Windows/Linux/Mac>` machine.
* You will have to install a HTTP web server like `Green Unicorn` in case Linux/Mac or `Waitress` in case of Windows

## Installing Telescope

To install Telescope, follow these steps:

Linux and macOS:
```
git clone https://github.com/michal-siedlecki/telescopeWebApp
pip install gunicorn
```

Windows:
```
git clone https://github.com/michal-siedlecki/telescopeWebApp
pip install waitress
```
## Using Telescope

To use Telescope, follow these steps:
if You are on `Linux/Mac` machine:
```
gunicorn -w 3 app:app
```
if You are on `Windows` machine:
```
waitress-serve --listen=127.0.0.1:8000 app:app
```

This repo comes in with very simple demo function that calculates shortest path in graph. Sample json request can be found in repo. 

## Contributing to Telescope

To contribute to Telescope, follow these steps:

1. Fork this repository.
2. 2. Create a branch: `git checkout -b <branch_name>`.
3. 3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. 4. Push to the original branch: `git push origin <project_name>/<location>`
5. 5. Create the pull request.
Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to the following people who have contributed to this project:

* [@michal-siedlecki](https://github.com/michal-siedlecki) 😎 [author]


## Contact

If you want to contact me you can reach me at <siedlecki.michal@gmail.com>.

## License

This project uses the following license: MIT (<https://github.com/michal-siedlecki/telescopeWebApp/blob/main/LICENSE>).
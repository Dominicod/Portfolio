# Dominic O'Donnell's Portfolio

Created and designed from development to production by Dominic O'Donnell. 
Designed to showcase all my skills and projects within a single consolidated domain. 
For this project, I learned to arrange the files for code readability and optimization. 
I also focused on mobile responsiveness, which I succeeded in.

## Test the portfolio on your local machine

If you wish to edit or test my portfolio on your local machine, go ahead and run...

```shell
git clone git@github.com:Dominicod/Portfolio.git
cd Portfolio
pip install -r requirements.txt
brew install sass/sass/sass *else* npm install -g sass
```

From there you will be within the webApp directory allowing you to find all the files
you will need in order to edit to your hearts desire. However in order to fully
setup this webApp you will need to configure `WSGI` and `Apache`.

### Initial Configuration

For Flask to properly work you will need to set the SECRET_KEY as well as the 
MAIL_USERNAME/MAIL_PASSWORD and EMAIL_API_KEY. This can be done by;

```shell
cd Portfolio/webApp
touch .env
nano .env
```
When editing .env you will want to paste this code, with your own generated values.

```
MAIL_USERNAME=""
MAIL_PASSWORD=""
SECRET_KEY =
EMAIL_API_KEY = 
```

## Developing

To customize the portfolio however you want you will want to get familar with the file-system.
Specifically with the SCSS and how that functions. Follow the code below.

*I recommend opening a seperate terminal*

```shell
cd Portfolio/webApp/static/styles
sass --watch styles.scss styles.css
```

You will first navigate to the styles file directory. From there you will activate
sass, which will complie the styles.scss file (which houses all the scss files through imports)
into regular styles.css. You will **NEVER** need to touch the regular styles.css.
From here everything is organized accordingly.

## Project technology

This project is running the following languages and tools:

* Python/Flask
* SCSS
* Figma (For Design)
* Javascript
* Apache

## What I learned

I learned alot from this project and I am glad I did it. For this portfolio I primarily focused on learning front end skills, and I wanted to dazzle anyone looking at my portfolio. For this I learned Javascript animations. I also wanted to learn how to structure my code, this is why I went with SCSS and seperated my files into imports. Lastly one big thing I learned was mobile responsiveness, I wanted this portfolio to work on all devices and i'm sure I got it to worK!

## Links

- Project homepage: https://github.com/Dominicod/Portfolio
- Repository: https://github.com/Dominicod/Portfolio



## Licensing

The code in this project is licensed under MIT license.
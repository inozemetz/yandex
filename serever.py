from flask import Flask, request, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def a():
    return 'Миссия Колонизация Марса'

@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
<html lang="ru">
<head>
    <!-- Required meta tags -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <!-- Google fonts -->
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,700&display=swap" rel="stylesheet">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="static/css/style.css">

    <title>Bootstrap. Basic carousel</title>
</head>
<body>
<h1> Пейзажи марса </h1>
    <!-- Carousel in a container -->
<div class="container">
        <div id="carousel-basic" class="carousel slide" data-ride="carousel">
            <!-- Indicators -->
            <ol class="carousel-indicators">
                <li data-target="carousel-basic" data-slide-to="0" class="active"></li>
                <li data-target="carousel-basic" data-slide-to="1"></li>
                <li data-target="carousel-basic" data-slide-to="2"></li>
            </ol>

            <!-- Wrapper -->
            <div class="carousel-inner" role="listbox">
                <div class="carousel-item active">
                    <img src="static/img/a1.jpg" alt="" class="img-fluid">
                    <div class="carousel-caption">
                    </div>
                </div>
                <div class="carousel-item">
                    <img src="static/img/a2.jpeg" alt="" class="img-fluid">
                </div>
                <div class="carousel-item">
                    <img src="static/img/a3.jpg" alt="" class="img-fluid">
                </div>
            </div>

            <!-- Controls -->
            <a class="carousel-control-prev" href="#carousel-basic" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Назад</span>
            </a>
            <a class="carousel-control-next" href="#carousel-basic" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Вперед</span>
            </a>
        </div>

        <!-- Content -->

    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


  <h3 align="center">News Portal project</h3>

  <p align="center">
    This is my homework, which is using django framework (python)
    <br />
    <a href="https://github.com/YtseyJam/Django_HW_NewsPortal/tree/master/DraftNews"><strong>Explore the code »</strong></a>
    <br />
    <br />

  </p>
</div>

<!-- TABLE OF CONTENTS 
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
-->


<!-- ABOUT THE PROJECT -->
## About The Project

Latest updates:

*03/09/2023:

Добавлено логгирование в [settings.py](https://github.com/YtseyJam/Django_HW_NewsPortal/blob/master/DraftNews/DraftNews/settings.py)



*23/07/2023:


Добавлена поддержка БД Redis и библиотеки Celery для асинхронного взаимодействия.


Теперь рассылки подписчикам категорий происходит с помощью функций в tasks.py. Signals.py по-прежнему вызывает таску при создании статьи.

<!--Затронуты/созданы файлы: 

<a href="https://github.com/YtseyJam/Django_HW_NewsPortal/blob/main/DraftNews/DraftNews/__init__.py"><strong>__init__.py</strong></a>

<a href="https://github.com/YtseyJam/Django_HW_NewsPortal/blob/main/DraftNews/newsportal/signals.py"><strong>signals.py</strong></a>

<a href="https://github.com/YtseyJam/Django_HW_NewsPortal/blob/main/DraftNews/DraftNews/celery.py"><strong>celery.py</strong></a>

<a href="https://github.com/YtseyJam/Django_HW_NewsPortal/blob/main/DraftNews/newsportal/tasks.py"><strong>tasks.py</strong></a>-->

Стиль страниц постов, конкретного поста, подписки на категории и поиска унифицирован.

Redis использован в виде бесплатного облака, в константы settings.py подставить свои данные.

Для запуска на Win данного функционала нужно три терминала и три команды:

1. Сервер приложения: `python manage.py runserver`
2. Celery worker: `celery -A DraftNews worker -l INFO --pool=solo`
3. Celery beat для задач по расписанию: `celery -A DraftNews beat -l INFO`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Django][Django.url]][Django-url]
* [![Redis][Redis.url]][Redis-url]
* and many others
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED 
## Getting Started

Здесь будут инструкции по запуску...

### Prerequisites

Что понадобится установить
* ...
  ```..
  ...
  ```

### Installation

_Инуструкции в процессе_

1. ...
2. ...
   ```sh
   ...
   ```
3. ...
   ```sh
   ...
   ```
4. ...
   ```js
   ...
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- USAGE EXAMPLES 
## Usage



<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- ROADMAP 
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- CONTRIBUTING 
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- LICENSE 
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- CONTACT -->
## Contact

Your Name - [@ytseyjam](https://t.me/ytseyjam) <!--- email@example.com-->

Project Link: [https://github.com/YtseyJam/Django_HW_NewsPortal](https://github.com/YtseyJam/Django_HW_NewsPortal)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments


* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Django.url]: https://img.shields.io/badge/Django-f
[Django-url]: https://www.djangoproject.com/
[Redis.url]: https://img.shields.io/badge/Redis-red
[Redis-url]: https://redis.io/

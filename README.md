<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Novanglus96/LenoreCraft">
    <img src="frontend/public/logov2.png" alt="Logo" height="40">
  </a>

<h3 align="center">LenoreCraft</h3>

  <p align="center">
    A simple woodworking/craft project tracking app.
    <br />
    <a href="https://github.com/Novanglus96/LenoreCraft"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Novanglus96/LenoreCraft/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/Novanglus96/LenoreCraft/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
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



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]

This project evolved as a way to keep track of my woodworking projects and all the parts/cuts needed to complete them.

It probably can be expanded to use for general crafting projects but it's main purpose was geared towards woodworking.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


 
### Built With

* [![Django][Django]][Django-url]
* [![Vue][Vue.js]][Vue-url]
* [![Docker][Docker]][Docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

Welcome to LenoreCraft! This guide will help you set up and run the application using Docker and Docker Compose.

### Prerequisites

Make sure you have the following installed on your system:

* [Docker](https://www.docker.com/get-started)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Step 1: Create a `.env` File

Create a `.env` file in the root directory of the project. This file will store environment variables required to run the application. Below is an example of the variables you need to define:

```env
# Database configuration
DB_HOST=db
DB_PORT=5432
DB_NAME=my_database
DB_USER=my_user
DB_PASSWORD=my_password

# Application settings
APP_ENV=production
APP_DEBUG=false
APP_SECRET=your_secret_key_here

# Other configurations
REDIS_HOST=redis
REDIS_PORT=6379
```

Adjust these values according to your environment and application requirements.

### Step 2: Create a `docker-compose.yml` File

Create a `docker-compose.yml` file in the root directory of the project. Below is an example configuration:

```yaml
version: '3.8'

services:
  app:
    image: your-docker-image
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db
      - redis

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}
    volumes:
      - db_data:/var/lib/postgresql/data
    restart: always

  redis:
    image: redis:7
    ports:
      - "6379:6379"
    restart: always

volumes:
  db_data:
```

### Step 3: Run the Application

1. Build and start the services:

   ```bash
   docker-compose up --build
   ```

2. Access the application in your browser at `http://localhost:8000`.

3. Monitor logs to ensure all services start correctly:

   ```bash
   docker-compose logs -f
   ```

### Notes

* Make sure to replace `your-docker-image` with the actual Docker image name.
* Adjust exposed ports (e.g., `8000`, `6379`) as needed for your environment.
* If you encounter any issues, ensure your `.env` file has the correct values and your Docker and Docker Compose installations are up to date.

Enjoy using LenoreCraft!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/Novanglus96/LenoreCraft/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
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



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Support

<a href="https://www.buymeacoffee.com/novanglus" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

<p>Or</p> 

<a href="https://www.patreon.com/novanglus">
	<img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

<!-- CONTACT -->
## Contact

John Adams - Lenore.Apps@gmail.com

Project Link: [https://github.com/Novanglus96/LenoreCraft](https://github.com/Novanglus96/LenoreCraft)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgements

A heartfelt thanks to our Patrons for their generous support! Your contributions help us maintain and improve this project.

### ⭐ Thank You to Our Supporters:

![Supporter Badge](https://img.shields.io/badge/Supporter-Patron%20Name%201-blue)  
![Supporter Badge](https://img.shields.io/badge/Supporter-Patron%20Name%202-green)  
![Supporter Badge](https://img.shields.io/badge/Supporter-Patron%20Name%203-red)

Want to see your name here? Support us on [Patreon](https://www.patreon.com/novanglus) to join our amazing community and shape the future of LenoreCraft!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Novanglus96/LenoreCraft?style=for-the-badge
[contributors-url]: https://github.com/Novanglus96/LenoreCraft/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Novanglus96/LenoreCraft?style=for-the-badge
[forks-url]: https://github.com/Novanglus96/LenoreCraft/forks
[stars-shield]: https://img.shields.io/github/stars/Novanglus96/LenoreCraft?style=for-the-badge
[stars-url]: https://github.com/Novanglus96/LenoreCraft/stargazers
[issues-shield]: https://img.shields.io/github/issues/Novanglus96/LenoreCraft?style=for-the-badge
[issues-url]: https://github.com/Novanglus96/LenoreCraft/issues
[license-shield]: https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge
[license-url]: https://github.com/Novanglus96/LenoreCraft/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/johnmadamsjr
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
[Django]: https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[Docker]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
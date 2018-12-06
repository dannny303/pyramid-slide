<template>
  <div class="main-wrapper">
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top" id="sideNav">
      <a class="navbar-brand js-scroll-trigger" href="#about">
        <span class="d-block d-lg-none">Danny Marez</span>
        <span class="d-none d-lg-block">
          <img class="img-fluid img-profile rounded-circle mx-auto mb-2" src="./assets/20160813_115404.jpeg" alt="">
        </span>
      </a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link js-scroll-trigger" href="#about">About</a>
          </li>
          <li class="nav-item">
            <a class="nav-link js-scroll-trigger" href="#experience">Experience</a>
          </li>
          <li class="nav-item">
            <a class="nav-link js-scroll-trigger" href="#skills">Skills</a>
          </li>
          <li class="nav-item">
            <a class="nav-link js-scroll-trigger" href="#interests">Interests</a>
          </li>
          <li class="nav-item">
            <a class="nav-link js-scroll-trigger" href="#awards">Certifications</a>
          </li>
          <li class="nav-item">
            <a class="nav-link js-scroll-trigger" href="#education">Education</a>
          </li>
        </ul>
      </div>
    </nav>

    <div class="container-fluid p-0">

      <section class="resume-section p-3 p-lg-5 d-flex d-column" id="about">
        <div class="my-auto">
          <h1 class="mb-0">{{ name }}
            <span class="text-primary">{{ surname }}</span>
          </h1>
          <div class="subheading mb-5">{{ address }}
            <a href="mailto:750danny@gmail.com">{{ email }}</a>
          </div>
          <p class="mb-5">{{ aboutMe }}</p>
          <ul class="list-inline list-social-icons mb-0">
            <li class="list-inline-item">
              <a href="https://www.instagram.com/dannny_750">
                <span class="fa-stack fa-lg">
                  <i class="fa fa-circle fa-stack-2x"></i>
                  <i class="fa fa-instagram fa-stack-1x fa-inverse"></i>
                </span>
              </a>
            </li>
            <li class="list-inline-item">
              <a href="https://join.slack.com/t/marez/shared_invite/enQtNDkzMzMwNDc0NjU5LTU2NjA4YTg0MDEzOTk2ZmYyNDFiMzFmMjg4ZDljZjA0MTFhYjhlOGNmMzdlNDM2Yjg0MDFjNjIyYTM1MjNmOGY">
                <span class="fa-stack fa-lg">
                  <i class="fa fa-circle fa-stack-2x"></i>
                  <i class="fa fa-slack fa-stack-1x fa-inverse"></i>
                </span>
              </a>
            </li>
            <li class="list-inline-item">
              <a href="https://github.com/dannny303">
                <span class="fa-stack fa-lg">
                  <i class="fa fa-circle fa-stack-2x"></i>
                  <i class="fa fa-github fa-stack-1x fa-inverse"></i>
                </span>
              </a>
            </li>
            <li class="list-inline-item">
              <a href="https://open.spotify.com/user/12729519?si=m1pSoip0Sk2TGIY3ORRxEg">
                <span class="fa-stack fa-lg">
                  <i class="fa fa-circle fa-stack-2x"></i>
                  <i class="fa fa-spotify fa-stack-1x fa-inverse"></i>
                </span>
              </a>
            </li>
          </ul>
        </div>
      </section>

      <section class="resume-section p-3 p-lg-5 d-flex flex-column" id="experience">
        <div class="my-auto">
          <h2 class="mb-5">Experience</h2>

          <div class="resume-item d-flex flex-column flex-md-row mb-5" v-for="job in experience" :key="job.description">
            <div class="resume-content mr-auto">
              <h3 class="mb-0">{{ job.position }}</h3>
              <div class="subheading mb-3">{{ job.company }}</div>
              <p>{{ job.description }}</p>
            </div>
            <div class="resume-date text-md-right">
              <span class="text-primary">{{ job.startDate }} - {{ job.endDate }}</span>
            </div>
          </div>
        </div>
      </section>

      <section class="resume-section p-3 p-lg-5 d-flex flex-column" id="skills">
        <div class="my-auto">
          <h2 class="mb-5">Skills</h2>
          <div class="subheading mb-3">Programming Languages &amp; Tools</div>
          <ul class="list-inline list-icons">

            <li class="list-inline-item">
              <i class="devicons devicons-apple"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicons devicons-windows"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicons devicons-linux"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicons devicons-html5"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicons devicons-css3"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicons devicons-sass"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicons devicons-javascript"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicon-vuejs-plain"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicons devicons-jquery"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicons devicons-python"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicons devicons-django"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicon-foundation-plain"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicons devicons-bootstrap"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicons devicons-postgresql"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicon-mysql-plain"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicons devicons-heroku"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicons devicons-git"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicons devicons-npm"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicons devicons-vim-plain"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicon-trello-plain"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicons devicons-slack"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicon-ssh-plain"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicons devicons-visualstudio-plain"></i>
            </li>
            <li class="list-inline-item">
              <i class="devicon-webpack-plain"></i>
            </li>
          </ul>
          <div class="subheading mb-3">Projects</div>
            <a href="https://arcane-sea-76068.herokuapp.com">Wishin I Was Fishin</a>
            <p>A site to look up Colorado surface water information and log trip reports utilizing Flask, several API's and an SQL database.</p>
        </div>
      </section>

      <section class="resume-section p-3 p-lg-5 d-flex flex-column" id="interests">
        <div class="my-auto">
          <h2 class="mb-5">Interests</h2>
          <p>I've got an insatiable desire to discover how things work. The Internet of Things, or IoT, is a fascinating beast with unlimited potental. I love reading about the latest and greatest advances in technology and science. Music enthusiast and a DIY backyard engineer.</p>
          <p>A true Colorado native at heart, I thoroughly enjoy everything outdoors! A Huge fly fisherman that loves to row my boat down the river hunting for fishy friends. Turning over river rocks to find bugs to photograph then replicate on the flytying vise.  A snowboarder with an endless thirst for deep and steep untracked powder. Long distance hiker extraordinaire.</p>
        </div>
      </section>

      <section class="resume-section p-3 p-lg-5 d-flex flex-column" id="awards">
        <div class="my-auto">
          <h2 class="mb-5">Certifications</h2>
          <ul class="fa-ul mb-0">
            <li>
              <i class="fa-li fa fa-certificate text-warning"></i>
              <li>Software Development Certification</li>
              <li>Devetry Code/Forward and Emily Griffith Technical College</li>
            <li>
              <i class="fa-li fa fa-tint text-warning"></i>
              <li>River Outfitter/Fly-Fishing Guide </li>
              <li> Colorado Division of Parks and Outdoor Recreation</li>
            <li>
              <i class="fa-li fa fa-heartbeat text-warning"></i>
              <li>CPR, AED and Basic First Aid</li>
              <li>American Safety and Heart Institute</li>
            <li>
              <i class="fa-li fa fa-trophy text-warning"></i>
              <li>Colorado Trail</li>
              <li>Through hike of the Colorado Trail, Denver to Durango, 500 miles in 26 days.</li>
            <li>
              <i class="fa-li fa fa-ambulance text-warning"></i>
              <li>Emergency Medical Technician-B</li>
              <li>St. Anthony Pre-Hospital Services and Institute of Emergency Medical Training</li>
          </ul>
        </div>
      </section>

      <section class="resume-section p-3 p-lg-5 d-flex flex-column" id="education">
        <div class="my-auto">
          <h2 class="mb-5">Education</h2>

          <div class="resume-item d-flex flex-column flex-md-row">
            <div class="resume-content mr-auto">
              <h3 class="mb-0">P.S.1 Charter School</h3>
              <div class="subheading mb-3">High School Diploma </div>
            </div>
            <div class="resume-date text-md-right">
              <span class="text-primary">May 2004</span>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      title: 'My portfolio',
      name: 'DANNY',
      surname: 'MAREZ',
      address: '720 16th Street · Denver, CO 80202 · (720) 427-4582 ·',
      email: '750danny@gmail.com',
      aboutMe: 'A junior software developer with full stack knowledge and extensive experience in property management. Avid Outdoorsman and DIY Master.',
      experience: [
        {
          position: 'Software Development Intern',
          company: 'Zero Kelvin',
          description: 'Contribute to the development of various web based applications. Experience with database design and architecture, along with frontend reporting and visualization. Regularly participate in code reviews and collaborate with other engineers to optimize code bases. Git workflow experience. Experience with feature flow, and deploying releases.',
          startDate: 'September 2017',
          endDate: 'Present'
        },
        {
          position: 'Property Manager',
          company: 'Neusteters Condominium Association Inc.',
          description: 'On-Site Manager of 100,000 sq. foot Condominium building with 100+ residents. Conduct routine maintenance and cleaning duties to keep the building running properly, including monitor and adjustment of Heating, Ventilation and Air Conditioning system. Provide direct services to residents and act as buffer between residents and HOA board members. Enforcement of buildings bylaws according to Condominium documents. Research, organize, and supervise, a wide variety of contractors and vendors. Minor electrical, plumbing and carpentry work.',
          startDate: 'Jaunary 2007',
          endDate: 'Present'
        },
        {
          position: 'Fuels Specialist/Wildland Firefighter',
          company: 'U.S.D.A Forest Service',
          description: 'Worked for the United States Department of Agriculture as a Wildland Firefighter, protecting the National Forest from human and natural caused forest fires. Prevented future forest fires through fuel reduction work, prescribed burns, and public education. Distinguished the risk of catastrophic fire by conducting many types of agricultural tests and fuel samplings.',
          startDate: 'April 2006',
          endDate: 'October 2006'
        }
      ]
    }
  },
  mounted () {
    const $ = this.jquery
    this.$nextTick(() => {
      // our custom jQuery code goes here
      $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
        if (location.pathname.replace(/^\//, '') === this.pathname.replace(/^\//, '') && location.hostname === this.hostname) {
          var target = $(this.hash)
          target = target.length ? target : $('[name=' + this.hash.slice(1) + ']')
          if (target.length) {
            $('html, body').animate({
              scrollTop: (target.offset().top)
            }, 1000, 'easeInOutExpo')
            return false
          }
        }
      })
      // Closes responsive menu when a scroll trigger link is clicked
      $('.js-scroll-trigger').click(function () {
        $('.navbar-collapse').collapse('hide')
      })
      // Activate scrollspy to add active class to navbar items on scroll
      $('body').scrollspy({
        target: '#sideNav'
      })
    })
  }
}
</script>

<style>
body {
  font-family: 'Open Sans', serif;
  padding-top: 54px;
  color: #868e96;
}
@media (min-width: 992px) {
  body {
    padding-top: 0;
    padding-left: 17rem;
  }
}
h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: 'Saira Extra Condensed', serif;
  font-weight: 700;
  text-transform: uppercase;
  color: #343a40;
}
h1 {
  font-size: 6rem;
  line-height: 5.5rem;
}
h2 {
  font-size: 3.5rem;
}
.subheading {
  text-transform: uppercase;
  font-weight: 500;
  font-family: 'Saira Extra Condensed', serif;
  font-size: 1.35rem;
}
.list-social-icons a {
  color: #495057;
}
.list-social-icons a:hover {
  color: #6567a5;
}
.list-social-icons a .fa-lg {
  font-size: 1.75rem;
}
.list-icons {
  font-size: 3rem;
}
.list-icons .list-inline-item i:hover {
  color: #6567a5;
}
#sideNav .navbar-nav .nav-item .nav-link {
  font-weight: 600;
  text-transform: uppercase;
}
@media (min-width: 992px) {
  #sideNav {
    text-align: center;
    position: fixed;
    top: 0;
    left: 0;
    display: flex;
    flex-direction: column;
    width: 17rem;
    height: 100vh;
  }
  #sideNav .navbar-brand {
    display: flex;
    margin: auto auto 0;
    padding: 0.5rem;
  }
  #sideNav .navbar-brand .img-profile {
    max-width: 10rem;
    max-height: 10rem;
    border: 0.5rem solid rgba(255, 255, 255, 0.2);
  }
  #sideNav .navbar-collapse {
    display: flex;
    align-items: flex-start;
    flex-grow: 0;
    width: 100%;
    margin-bottom: auto;
  }
  #sideNav .navbar-collapse .navbar-nav {
    flex-direction: column;
    width: 100%;
  }
  #sideNav .navbar-collapse .navbar-nav .nav-item {
    display: block;
  }
  #sideNav .navbar-collapse .navbar-nav .nav-item .nav-link {
    display: block;
  }
}
section.resume-section {
  border-bottom: 1px solid #dee2e6;
  padding-top: 5rem !important;
  padding-bottom: 5rem !important;
}
section.resume-section .resume-item .resume-date {
  min-width: none;
}
@media (min-width: 768px) {
  section.resume-section {
    min-height: 100vh;
  }
  section.resume-section .resume-item .resume-date {
    min-width: 18rem;
  }
}
@media (min-width: 992px) {
  section.resume-section {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
  }
}
.bg-primary {
  background-color: #6567a5 !important;
}
.text-primary {
  color: #6567a5!important;
}
a {
  color: #6567a5;
}
a:hover, a:focus, a:active {
  color: #6567a5;
}
</style>

import streamlit as st
import streamlit.components.v1 as components
from header import Header
st.set_page_config(page_title="Alishbah.PY", layout="wide")
Header()

swiper_html = """
<!DOCTYPE html>
<html lang="en">
<head>

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Alishbah.PY</title>
  <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/swiper@8/swiper-bundle.min.css'>
  <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css'>
  <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css" />

  <style>
    body {
      background-color: hsl(228, 6%, 8%);
      margin: 0;
      padding: 0;
      font-family: "Poppins", sans-serif;
      overflow-y: auto;
    }
    span {
      color: rgb(233, 193, 134);
    }

    main {
      position: relative;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      margin-top: -60px;
      padding: 20px;
      max-width: 1400px !important;
      margin-bottom: 0 !important;
    }

    main h2 {
      font-size: 2.8rem;
      color: white;
      text-shadow: 0px 1px 10px rgb(180, 151, 48);
    }

    @media screen and (max-width: 400px) {
      main{
        margin-top: -40px;
      }
      main h2{
          font-size: 20px;
      }
      p {
        font-size: 12px !important;
        margin-top: -5px !important;
      }
      .swiper-slide{
        width: 200px !important;
        height: 400px !important;
      }
    }
    main p {
      color: white;
      max-width: 600px;
      font-size: 16px;
      line-height: 1.6;
      margin-top: -20px
    }

    .btn {
      background: transparent;
      border: 2px solid white;
      color: white;
      padding: 12px 20px;
      font-size: 16px;
      cursor: pointer;
      display: inline-block;
      border-radius: 4px;
      box-shadow: 0px 1px 15px white;
      margin-top: 20px;
    }

    .btn i {
      margin-left: 15px;
    }

    .btn:hover {
      background-color: rgb(233, 193, 134);
      color: black;
      transition: 0.5s ease-in !important;
    }

    .swiper-container {
      width: 750px;
      padding-top: 50px;
    }
    .swiper-slide{
      display: flex;
      justify-content: center;
      align-items: center;
      width: 300px;
      height: 500px;
      border: 4px solid rgb(233, 193, 134);
      border-radius: 20px;
      box-shadow: 0px 1px 20px rgb(233, 193, 134)
    }
    .swiper-slide h3{
      font-size: 25px;
      font-weight: 700;
      font-family: cursive;
      color: white;
      text-shadow: 0px 1px 20px rgb(233, 193, 134)
    }
    .slide-one{
     background: linear-gradient(to bottom, #2c536400, #203a4303, #0f2027cc), url("https://png.pngtree.com/thumb_back/fh260/background/20240603/pngtree-cloud-server-and-computing-data-storage-and-processing-internet-and-technology-image_15739065.jpg") no-repeat 50% 50%/cover;
    }
    .slide-two{
      background: linear-gradient(to bottom, #2c536400, #203a4303, #0f2027cc), url("https://play-lh.googleusercontent.com/mxqkNmFZp6PT9MBZ1Am4mpBMN81z8E06Tu-V7Utv4m6gYDASAcDqyKxzeI6P2jGNUvU") no-repeat 50% 50%/cover;
    }
    .slide-three{
      background: url("https://img.freepik.com/premium-vector/blue-simple-lock-seamless-pattern_138551-89.jpg?semt=ais_hybrid") no-repeat 50% 50%/cover;
    }
  </style>

</head>
<body>
  <main>
    <h2 data-aos="fade-right" data-aos-duration="2000" data-aos-delay="400">ALISHBAH.<span>PY</span></h2>
    <p data-aos="zoom-in" data-aos-duration="2000" data-aos-delay="400">As I embark on my Python journey, this space will serve as a collection of my projects, showcasing my progress and learning.</p>
    <button class="btn" data-aos="fade-right" data-aos-duration="2000" data-aos-delay="400">About Me <i class="fa-solid fa-arrow-right"></i></button>
    <div class="swiper-container" data-aos="zoom-out" data-aos-duration="2000" data-aos-delay="400">

        <div class="swiper-wrapper" >

            <div class="swiper-slide slide-one">
                <h3>Data Sweeper</h3>
            </div>

            <div class="swiper-slide slide-two">
                <h3>Unit Converter</h3>
            </div>

            <div class="swiper-slide slide-three">
                <h3>Password Strength</h3>
            </div>

        </div>
    </div>
  </main>

  <script src="https://unpkg.com/aos@next/dist/aos.js"></script>
  <script src='https://cdnjs.cloudflare.com/ajax/libs/Swiper/8.4.5/swiper-bundle.min.js'></script>
  <script>
    AOS.init();

    document.querySelector(".btn").addEventListener("click", function () {
      window.open("https://alishbah-portfolio.vercel.app/", "_blank");
    });


    var mySwiper = new Swiper('.swiper-container', {
        loop: true,
        speed: 1000,
        autoplay: {
            delay: 1800,
        },
        effect: 'coverflow',
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: 'auto',
        coverflowEffect: {
            rotate: 0,
            stretch: 34,
            depth: 160,
            modifier: 1,
            slideShadows: false,
        },
    })
  </script>
</body>
</html>
"""

components.html(swiper_html, height=800)

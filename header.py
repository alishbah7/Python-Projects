import streamlit as st


# st.set_page_config(layout="wide", page_title="Alishbah.PY")

def Header():
  st.markdown("""
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
      <style>
          header {visibility: hidden;}
          footer {visibility: hidden;}
        .stApp{
          background-color: hsl(228, 6%, 8%);
        }
        ::-webkit-scrollbar{
          width: 12px !important;
        }
        ::-webkit-scrollbar-track{
            background: hsl(228, 6%, 8%) !important;
        }
        ::-webkit-scrollbar-thumb{
            background: rgb(233, 193, 134) !important;
            border-radius: 10px !important;
        }
      .header{
          padding: 0;
          margin: 0;
          box-sizing: border-box;
          font-family: 'Poppins', sans-serif;
          list-style: none;
          text-decoration: none;
          scroll-behavior: smooth;
      }
      a{
          text-decoration: none;
      }

      span{
          color: rgb(233, 193, 134);
      }
      nav{
          margin-top: -80px;
          position: absolute;
          z-index: 1000;
          width: 100%;
      }
      nav .wrapper{
        position: relative;
        max-width: 1300px;
        padding: 0px -30px !important;
        height: 70px;
        line-height: 70px;
        margin: auto;
        display: flex;
        align-items: center;
        justify-content: space-between;
      }
      .wrapper .logo a{
        color: white;
        font-size: 30px;
        font-weight: 600;
        text-decoration: none;
        text-shadow: 0px 1px 10px rgb(180, 151, 48);  
      }
      .wrapper .nav-links{
        display: inline-flex;
      }
      .nav-links li{
        list-style: none;
      }
      .nav-links li a{
        color: white;
        text-decoration: none;
        font-size: 18px;
        font-weight: 500;
        padding: 9px 10px !important;
        margin-left: -20px !important;
        border-radius: 5px;
      }
      .nav-links .mobile-item{
        display: none;
      }
      .nav-links .drop-menu{
        margin-top: -10px;
        margin-left: -10px !important;
        width: 200px;
        position: absolute;
        background: rgb(233, 193, 134);
        line-height: 20px;
        top: 85px;
        opacity: 0;
        visibility: hidden;
      }
      .nav-links li:hover .drop-menu{
        transition: all 0.3s ease;
        top: 70px;
        opacity: 1;
        visibility: visible;
        box-shadow: 0px 1px 10px black;
        text-align: center;
      }
      .drop-menu li a{
        font-size: 15px;
        margin-left: -30px !important;
        display: block;
        padding: 0 0 0 15px;
        text-align: center;
        font-weight: 400;
        border-radius: 0px;
        color: black;
        transition: all 0.3s ease;
      }
      .drop-menu li a:hover{
          background: rgb(255, 247, 247);
          transition: all 0.3s ease;      
      }
      .wrapper .btn{
        color: #fff;
        font-size: 20px;
        cursor: pointer;
        display: none;
      }
      .wrapper .btn.close-btn{
        position: absolute;
        right: 30px;
        top: 10px;
      }
      .portfolio a{
          margin-left: 10px;
          display: inline-flex;
          justify-content: center;
          align-items: center;
          height: 40px;
          background: rgb(233, 193, 134);
          border-radius: 5px;
          font-size: 15px;
          padding: 12px 25px;
          color: black;
          text-decoration: none;
          letter-spacing: 1px;
      }
      #logoTitleSmall a{
        display: none;
      }
      @media screen and (max-width: 970px) {
        .wrapper .btn{
          display: block;
        }
        .wrapper .nav-links{
          position: fixed;
          height: 100vh;
          width: 100%;
          max-width: 350px;
          top: 0;
          left: -100%;
          background-color: hsl(228, 6%, 8%);
          display: block;
          padding: 50px 10px !important;
          line-height: 30px;
          overflow-y: auto;
          box-shadow: 0px 15px 15px rgba(0,0,0,0.18);
          transition: all 0.3s ease;
        }
        #logoTitleSmall a{
          display: block;
          font-size: 30px;
          font-weight: 600;
        }
        .drop-menu li a:hover{
          background: rgb(233, 193, 134);
          color: black;
          transition: all 0.3s ease;      
      }
        .nav-links .drop-menu{
          margin-top: 0px;
      }
        #menu-btn{
          margin-top: 20px !important;
        }
        #menu-btn:checked ~ .nav-links{
          left: 0%;
        }
        #menu-btn:checked ~ .btn.menu-btn{
          display: none;
        }
        #close-btn:checked ~ .btn.menu-btn{
          display: block;
        }
        .nav-links li{
          margin: 10px 10px !important;
        }
        .nav-links li a{
          padding: 0 20px;
          display: block;
          font-size: 20px;
        }
        .nav-links .drop-menu{
          position: static;
          opacity: 1;
          top: 65px;
          visibility: visible;
          max-height: 0px;
          overflow: hidden;
          box-shadow: none;
          transition: all 0.3s ease;
          margin-left: 20px;
        }
        #showDrop:checked ~ .drop-menu{
          max-height: 100%;
        }
        .nav-links .desktop-item{
          display: none;
        }
        .nav-links .mobile-item{
          margin-left: -10px !important;
          display: block;
          color: white;
          font-size: 20px;
          font-weight: 500;
          cursor: pointer;
          border-radius: 5px;
          transition: all 0.3s ease;
        }
        .drop-menu li{
          margin: 0;
        }
        .drop-menu li a{
          border-radius: 5px;
          font-size: 18px;
        }
        .portfolio a{
          margin-top: 10px !important;
        }
      }
      @media screen and (max-width: 700px){
          ::-webkit-scrollbar{
              display: none;
          }
          .wrapper .logo a{
              font-size: 20px;
          }
      }
      nav input{
        display: none;
      }
      </style>
      <div class='header'>
      <nav>
          <div class="wrapper">
            <div class="logo"><a href="#">PYTHON<span>.PY</span></a></div>
            <input type="radio" name="slider" id="menu-btn">
            <input type="radio" name="slider" id="close-btn">
            <ul class="nav-links" style="margin-top: 20px;">
              <label for="close-btn" class="btn close-btn"><i class="fas fa-times" style="color: white;"></i></label>
              <li id="logoTitleSmall"><a href="#">PYTHON<span>.PY</span></a></li>
              <li><a href="https://alishbahpy.streamlit.app/">Home</a></li>
              <li>
                <a href="#" class="desktop-item" >Projects</a>
                <input type="checkbox" id="showDrop">
                <label for="showDrop" class="mobile-item">Projects</label>
                <ul class="drop-menu">
                  <li><a href="https://csvex-byalishbah.streamlit.app/">CSVEX</a></li>
                  <li><a href="https://unitconverter-byalishbah.streamlit.app/">Unit Converter</a></li>
                  <li><a href="https://password-strength-meter-byalishbah.streamlit.app/">Password Strength Meter</a></li>
                  <li><a href="https://comingsoon.streamlit.app/">Library Manager</a></li>
                </ul>
              </li>
              <div class="portfolio"><a href="https://alishbah-portfolio.vercel.app/">Portfolio</a></div>
          </ul>
            <label for="menu-btn" class="btn menu-btn"><i class="fas fa-bars" style="color: white;"></i></label>
          </div>
        </nav>
    </div>

  """, unsafe_allow_html=True)



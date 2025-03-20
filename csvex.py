import streamlit as st
st.set_page_config(page_title="CSVEX💫", layout="wide")
import pandas as pd 
import os 
from io import BytesIO
from header import Header
Header()

# --==== CSS ====-- #
st.markdown("""
        <style> 
        .mainTitle{
            color: white;
            text-shadow: 0px 1px 20px rgb(233, 193, 134);
            font-size: 40px;
            font-weight: 900;    
            margin-bottom: 10px
        }
        .subTitle{
            color: white;
            padding-bottom: 10px;
            letter-spacing: 2px   
        }
        div.stFileUploader label {
            color: white !important; 
            font-weight: bold;
            font-size: 18px;
            margin-top: 14px
        }
        div.stFileUploader button {
            background: rgb(233, 193, 134);
            border-radius: 5px;
            color: black;
            font-weight: bold;
            border-radius: 8px;
            padding: 6px 12px;
            transition: .5s ease
        }
        div.stFileUploader button:hover {
            background-color: transparent;
            color: rgb(190, 144, 74) !important;
            border: 1px solid rgb(190, 144, 74);
            box-shadow: 0px 1px 20px rgb(190, 144, 74);
            transition: .5s ease
        }
        div.stFileUploader div{
            color: white !important;
            font-size: 12px;    
        }
        div.stFileUploader span {
            color: rgb(190, 144, 74) !important;
            font-weight: bold;
        }
        .fileName, .fileSize{
            color: white !important;
        }
        .fileName span, .fileSize span{
            color: rgb(244, 214, 169) !important;
            font-family: cursive;
            text-shadow: 0px 1px 10px white;
            font-style: italic  
        }
        .dataPreview, .cleanData, .columns, .visual, .converOpt{
            color: white;
            text-shadow: 0px 1px 10px rgb(244, 214, 169);
            margin-bottom: -20px
        }
        .chooseCol, .converTo{
            color: white;
            margin-bottom: -30px !important;
        }
        .warning{
            color: black;
            background: rgb(255, 215, 193);
            border-radius: 20px;
            padding: 6px 10px;
            height: 40px;
        }
        div[role="radiogroup"] label {
            width: 80px;
            padding: 5px;
            color: white;
            margin: 10px !important;
            background: white;
            box-shadow: 0px 1px 10px rgb(244, 214, 169);
        }
        @media screen and (max-width: 600px) {
            .fileName{
                font-size: 20px;
                margin-bottom: -30px
            }
            .dataPreview{
                margin-top: -30px
            }
            .warning{
                font-size: 12px;
                padding: 2px 10px;
            }
        }
        @media screen and (max-width: 700px){
          ::-webkit-scrollbar{
              display: none;
          }
        }
        h1, h2, h3, h4 {
            color: black !important;
            text-align: left;
        }
        .stButton>button, .stDownloadButton>button {
            width: 180px;
            background: rgb(233, 193, 134);
            color: black !important;
            font-size: 10px !important;
            border-radius: 8px;
            border: 2px solid white !important; 
            box-shadow: 0px 1px 10px rgb(249, 228, 195);;
            transition: 0.5s ease-in-out;
        }
        .stButton>button:hover, .stDownloadButton>button:hover {
            transform: scale(1.05); 
            transition: 0.3s ease-in-out;
            background: transparent;
            color: white !important;
        }
        .stCheckbox label, .stRadio label {
            font-size: 16px;
            font-weight: bold;
        }
        .section {
            margin-top: 30px !important;
            margin-bottom: 30px !important;
        }
        hr {
            border: 1px solid rgb(244, 214, 169) !important;
            margin: 30px 0 !important;
        }

    </style>
""", unsafe_allow_html=True)

# --==== TITLE & SUB-TITLE ====-- #
st.markdown('<div class="mainTitle">CSVEX</div>', unsafe_allow_html=True)
st.markdown('<div class="subTitle">Welcome To <b>CSVEX</b></div>', unsafe_allow_html=True)

# --==== FILE UPLOADER ====- #
uploaded_files = st.file_uploader("📂 Upload Your Files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

processed_files = 0

# --==== FILE TYPE CHECKING AND DETAILS ====-- #
if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"❌ Unsupported File Type: {file_ext}")
            continue
        st.markdown("<hr>", unsafe_allow_html=True) 
        st.write(f"### <div class='fileName'> 📄 File Name: <span> **{file.name}** </span> </div>" , unsafe_allow_html=True)
        st.write(f" <div class='fileSize'> 📏  File Size: <span> {round(file.size/1024, 2)} KB </span> </div>", unsafe_allow_html=True)
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.write("#### <div class='dataPreview'> 🏁 Data Preview </div>", unsafe_allow_html=True)
        st.dataframe(df.head())
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)


        # --==== DATA CLEANING SECTION ====-- #
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.write(f"### <div class='cleanData'> 🛠 Data Cleaning Options </div>", unsafe_allow_html=True)
        if st.button("🗑 Remove Duplicates"):
                df.drop_duplicates(inplace=True)
                st.write("✅ Duplicates Removed!")
        if st.button("🛠 Fill Missing Values"):
                numeric_cols = df.select_dtypes(include=["number"]).columns
                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                st.write("✅ Missing Values Have Been Filled")
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True) 


        # --==== COLUMN SELECTION SECTION ====-- #
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.write(f"### <div class='columns'> 🔄 Select Columns to Convert </div>", unsafe_allow_html=True)
        st.write(f"<div class='chooseCol'> 🎯 Choose Columns For {file.name} </div>", unsafe_allow_html=True)
        columns = st.multiselect("", df.columns, default=df.columns)
        df = df[columns]
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)  


        # --==== DATA VISUALIZATION SECTION ====-- #
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.write(f"### <div class='visual'> 📊 Data Visualization </div>", unsafe_allow_html=True)
        numeric_cols = df.select_dtypes(include=["number"])
        if numeric_cols.shape[1] == 0:
            st.write("<div class='warning'>⚠️ Not enough numeric columns to show visualization. </div>", unsafe_allow_html=True)
        else:
            if st.checkbox(f"📈 Show Visualization For {file.name}"):
                st.bar_chart(numeric_cols.iloc[:, :2])
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True) 


        # --==== CONVERSION OPTIONS SECTION ====-- #
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.write("### <div class='converOpt'>🔃 Conversion Options </div>", unsafe_allow_html=True)
        st.write(f"<div class='converTo'> 🔀 Convert {file.name} To: </div>", unsafe_allow_html=True)
        conversion_type = st.radio("",["CSV", "Excel"], key=file.name)
        if st.button("📥 Download"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            else:
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)
            st.download_button(
                label=f"⬇️ Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )
            processed_files += 1 
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)  

# --==== SUCCESS ====-- #
if processed_files > 0:
    st.success(f"🎉 {processed_files} File(s) Successfully Processed!")




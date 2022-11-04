@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

*, html, body{
  padding: 0px;
  margin: 0px;
  box-sizing: border-box;
  cursor:url("images/fc.cur"), default;
}

.post{
  border-radius: 30px;
  padding: 0px;
  margin: 10px;
  text-align: center;
  width: 23%;
  display: inline-block;
}

.post h2{
  padding: 15px;
  background-color: gold;
  color: white;

}

@media(max-width: 900px){
 .post{
   width: 100%;
   display: block;
   margin: 8px;
  }
}

header{
  position: fixed;
  background-color: red;
  text-align: center;
  padding: 30px;
  color: white;
  z-index: 0;
}

.navbar{
  background-color: black;
  padding: 20px;
  text-align: center;
}

.navbar a{
  padding:10px;
  color: white;
  text-decoration: none;
}

.navbar a:hover{
  color: rgb(109, 15, 15);
}

.post-form{
  border: 2px solid green;
  border-radius: 5px;
  width: 40%;
  margin: 10px auto;
  background-size: cover;
}

.post-form p{
  padding: 15px; 
}

.post-form input, textarea{
  display: block;
}

.post-form textarea{
  width: 100%
}

.post-form button{
  margin: 10px;
  padding: 5px;
  background-color: red;
  color: white;
  font-size: 24px;
}

header{
  font-family: Press Start 2P;
  height: 65px;
  width: 100%;
  display: flex;
  text-align: center;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  background: linear-gradient(red,
    yellow);
  margin-top: 0px;
}

body, html{
  font-family: Press Start 2P;
  background-color: rgb(0, 0, 0);
  padding: 0;
  margin: 0;
  color: black;
  margin-bottom: 200px;
}

h1{
    font-size: 50px;
    justify-content: center;
    text-align: center;
    padding-top: 0px;
}

.sitting{
    text-align: center;
    justify-content: center;
    height: 80%;
} 

.parallax1{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/download2.jpg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.parallax2{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/kre.jpg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.parallax3{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/Levaithan.jpg");
    justify-content: center;
    min-height: 100%;
    text-align: center;
}

.parallax4{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/trex.jpg");
    justify-content: center;
    min-height: 100%;
    text-align: center;
}

.parallax5{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/bigf.jpg");
    justify-content: center;
    min-height: 100%;
    text-align: center;
}

.information{
   background-color: rgba(139, 88, 88, 0.13);
   font-size: 16px;
   padding: 20px;
   text-align: center;
   justify-content: center;
}

.caption1{
    padding: 10px;
    background-size: cover;
    font-size: 24px;
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 45%;
    color: white;
    background-color: rgba(3, 0, 0, 0.3);
}

.caption2{
    padding: 10px;
    background-size: cover;
    font-size: 24px;
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 150%;
    color: white;
    background-color: rgba(3, 0, 0, 0.3);
}

.caption3{
    padding: 10px;
    background-size: cover;
    font-size: 24px;
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 250%;
    color: white;
    background-color: rgba(3, 0, 0, 0.3);
}

#sun{
  position: absolute;
  top: 80%;
  left: 50%;
  width: 220px;
  height: 50px;
  margin-top: -100px;
  margin-left: -100px;
  border: 1px;
  box-shadow: 0px 0px 128px blue;
}

#sun2{
  position: absolute;
  top: 221%;
  left: 49%;
  width: 222px;
  height: 50px;
  margin-top: -100px;
  margin-left: -100px;
  border: 1px;
  box-shadow: 0px 0px 128px red;
}


nav ul{
    display: flex;
    margin-left: 0px;
}

nav a{
    padding: 10px;
    margin-right: 0px;
}

nav a{
    color: white;
    font-size: 18px;
}

nav a:hover{
   color: rgb (114, 0, 0);
   border-bottom: 2ps solid red;
}

.copyright {
  background-color:gold;
  text-align: center;
  justify-content: center;
  display: flex;
  width: 100%;
}

.h6 {
  text-align: center;
  position: relative;
}

body, html{
  font-family: Press Start 2P;
  background-color: rgb(0, 0, 0);
  padding: 0;
  margin: 0;
  color: white;
}

.subscript{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/Levaithan.jpg");
    width: 100%;
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.subscript2{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/lm.jpg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.informational{
   background-color: rgba(139, 88, 88, 0.13);
   font-size: 18px;
   padding: 20px;
   text-align: center;
   justify-content: center;
}

.c1{
    padding: 10px;
    background-size: cover;
    font-size: 50px;
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 50%;
    color: white;
    background-color: rgba(3, 0, 0, 0.3);
}

.c2{
    padding: 10px;
    background-size: cover;
    font-size: 50px;
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 230%;
    color: white;
    background-color: rgba(3, 0, 0, 0.3);
}

.c3{
    padding: 10px;
    font-size: 50px;
    background-size: cover;
    background-color: rgba(3, 0, 0, 0.3);
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 130%;
}

.c4{
    padding: 90px;
    font-size: 50px;
    background-size: cover;
    top: 240%;
    left: 32%;
}

body{
    --mainblue: red;
    --mainyellow: greenyellow;
    --mainred: red;
    --mainorange: orange;
}

h1{
  color: gold;
}

.header{
    height: 500px;
    flex-direction: row;
    justify-content: space-between;
    width: 100%;
    background-color: rgb(117, 117, 141);
         
position: relative; 
    
}


.FlexBoox{
  height: 20px;
  width: 100%;
  background-image: url("OIP (52).jpg");
  border: 2px solid red;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding-left: 15px;
}

.text{
     position: absolute;
     top: 0px;
     right: 0px;
}

.box{
     height: 100px;
     width: 100px;
     background-color: var(--mainyellow);

}

p{
     font-size: 20px;
     border: 10px solid var(--mainblue);
     color: var(--mainblue);
}

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    list-style: none;
    text-decoration: rgb(red, green, blue);
    scroll-behavior: smooth;
    font-family: 'Playfair Display', serif;
}

.section{
      min-height: 100vh;  
}

#header{
  background-image: url("R (4).jpg");
  background-size: cover;
}

#header1{
  background-image: url("257381.jpg");
  background-size: cover;
  text-align: center;
  color: gold;
}

#header2{
  background-image: url("161013.jpg");
  background-size: cover;
}  

#header3{
  background-image: url("redf.jpg");
  background-size: cover;
  color: gold;
}

#header4{
  background-image: url("R (4).jpg");
  background-size: cover;
  color: gold;
}

#header5{
  background-image: url("R (5).jpg");
  background-size: cover;
  color: gold;
}

#header6{
  background-image: url("OIP (34).jpg");
  background-size: cover;
  color: gold;
}

#header7{
  background-image: url("upio.jpg");
  background-size: cover;
  color: gold;
}

#header h1{
  width: 300px;
  font-size: 80px;
  margin: 0px;
  color: var(--mainblue);
  position: absolute;
  text-align: center;
  top: 0%;
  transform: translateY(0%);
}

#header a{
  color: var(--mainblue);
  border: 3px var(--mainblue);
  background-color: solid rgba(red, green, blue, alpha);
  border-radius: 3px;
  padding: 20px;
  font-size: 30px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  transition: background-color, .2s linear, border-color, .2s linear;
}

.blue{
    color: var(--mainblue);
}

#navbar a:hover{
  color: red;
  background-color: greenyellow;
  border-color: red;
  font-size: 20px;
}

#about{
   text-align: left;
   position: left;
   font-size: 10px;
   font-family: 'playfair display';
   color: red;

}

#about1{
   text-align: center;
   position: center;
   font-size: 10px;
   font-family: 'playfair display';
   color: red;

}

@media(max-width: 900px){
 
    .section{
       padding: 30px;
       position: center;
    }
    
        #header{
        text-align: left;
  
}

    #header h1{
    font-size: 40px;
    width: auto;
    transform: none;
    position: static;
    }

    nav {
        flex-direction: column;
        padding: 10px 0;
    }
    
    nav ul{
    display: flex;
    margin-left: 100px;  
  }

}
  
.blue{
  color: var(--mainyellow);
}

a,p{
   font-family: "Open Sans", sans-serif;
}

navbar{
    background-color: blue;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 10px 100px;
    position: sticky;
    top: 0;
    border-bottom: 5px solid var(--mainblue);
    z-index: -2;
}  

nav h2{
    color: gold;
    margin-left: 0px;
    
}

nav ul{
    display: flex;
}

nav ul{
    display: flex;
    margin-left: 100px;
}

nav li{
     padding: 5px;
     margin-right: 20px;
}

nav li a{
     color: red;
     font-size: 24px;
}

nav{
    width: 250px;
    height: 100vh;
    padding: 60px 20px;
    background: linear-gradient(red,
    orange, yellow, green);
    position: fixed;
    right: -240px;
    top: 0;
    transition: right 0.5s;

}

.section h1{
    font-size: 64px;
    text-align: center;
    margin-bottom: 30px;

}

.aboutTop{
     text-align: center;
     padding: 40px;
     font-size: 24px; width: 80%;
     margin: auto;
    
}

.aboutTop img{
     width: 400px;
     border-radius: 50%;
     background-color: var(--mainblue);
     margin-bottom: 20px;

}

.aboutBottom{
     display: flex;
     justify-content: space-around;
     padding: 40px;

}

.hobby{
     text-align: center;
     width: 30%;
     height: 300px;
     padding: 40px;
     background-color: var(--maingray);
     border-radius: 16px;
     color: white;
     border-bottom: 7px solid var(--mainblue)
  
}
.hobby i{
     font-size:120px;
     color:var(--mainblue);
     margin-bottom: 20px;
}

#projects{
    background-color:rgb(255, 255, 255);
}

.myprojects{
   width: 90%;
   margin: auto;
   text-align: center;
}

.project{
   display: flex;
   justify-content: space-between;
   align-items: center;
   margin: 20px;

}  

projectText{
  flex: 1;
  margin: auto 40px;

}

projectText h2{
    color: var(--mainblue);
    font-size: 36px;
    margin-bottom: 10px;
    border-bottom: 2px solid var(--maingray);
}

.projectText p{
    font-size: 20px;
}

.screen{
  width: 400px;
  position: relative;
}

.screen img{  
    width: 100%;    
}

.screening{
    background-color: red;
    background-size: cover;
    background-position: fixed;

    position: absolute;
    width: 305px;
    height: 195px;
    top: 8px;
    left: 48px;
    border-radius: 3px;

    display: flex;
    justify-content: center;
    align-items: center;

}

.sceening i{
   font-size: 8px;
   color: var(--mainyellow);
   opacity:0;

   transition: opacity, .2s linear;

   transform: translateX(-10px);
}

.screen:hover i{
    opacity: 1;
    transform: translateX(0px);
}

.projects{
     width: 1000px;
     margin: auto;
     display: flex;
     justify-content: center;
     flex-wrap: wrap;

}

.project{
     width: 333px;
     height: 300px;
     background-size: cover;
     background-position: center;
}

.project a{
     color: white;
     background-color: var(--mainblue);
     display: show;
     width: 100%;
     font-size: 30px;
     padding:5px;
     text-align: center;
     opacity: 0;
     transition: opacity, .2s linear;
}

#mountian-of-money{
     background-image: url("mountian-of-money.jpg");

}



#flex {
  background-image: url("images/flex.png");

}



.skillsContainer{
  display: flex;
  justify-content: space-inbetween;
  align-items: center;
  max-height: 600px;  
  position: relative;
}

.skill{
  width: 20%;
  display: flex;
  justify-content: center;

}

.skills img{
  width: 10%;
  height: 10%;

}

.skillsBackground{
  position: absolute;
  width: 100%;
  height: 100%;
  background-color: var(--mainblue);
  z-index: -1;
}

#buy-hover~ skillsBackground{
  background-color: rgb(red, green, blue);

}
#sell:hover~skillsBackground{
  background-color: red;
}
#trade:hover~skillsBackground{
  background-color: red;
}

#css:hover~skillsBackground{
  background-color: red;
}

#css:hover~skillsBackground{
  background-color: red;
}

#html:hover~#htmltext{
  display: block;

}
#python:hover ~ pythontext{
  display: block;
} 

#unityhover ~ unitytext{
  display: block;
}

.skillScale{
   display: flex;
   flex-direction: column;
   width: 80%;
   margin:auto;
}

.levels{
  display: flex;
  justify-content:space-between;
}

.level{
  font-size: 30px;
}

.bar{
  height: 60px;
  display: flex;
  justify-content: flex-end;
  padding-right: 40px;
  color: white;
  font-size: 40px;

}

.graph{
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  width: 100%;
  height: 400px;
  margin-top: 50px;
  position: relative;
}

.bar .beg{
  width: 33%;
}

.bar .int{
  width: 66%;
}

.bar .exp{
  width: 100%;
}

.bar.first{
    background-color: rgb(255, 145, 0);
}

.bar.second{
    background-color: rgb(4, 128, 7);
}

.bar.first{
    background-color: rgb(247, 232, 28);
}

.bar.second{
    background-color: rgb(31, 31, 31);
}
.skillsContainer p{
  position: absolute;
  bottom: 20px;

  width: 100%;
  text-align: center;
  font-size: 34px;
  color: orange;
  display: none;
}

.aboutLeft{
    width: 100%;
    display: inline-block;
    justify-content: left;
    padding: 30px;
    vertical-align: center;
    color: red;
    font-size: 30px;
    text-align: center;
}

.aboutLeft img{
     width: 400px;
     vertical-align: center;

     background-color: var(--mainblue);
     margin-bottom: 20px;
     
}

.aboutRight{
     width: 100%;
     display: inline-block;
     justify-content: left;
     padding: 30px;
     vertical-align: center;
     color: red;
     font-size: 30px;
     text-align: center;


}

.aboutTop{
     padding: 0;
     display: inline-block;
     width: 100%;
     font-size: 60px;
     vertical-align: center;

     }

.hobby{
    width: 100%;
    height: 30%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 5px solid var(--mainblue); 

}

.hobby i{
     font-size: 120px;
     color: var(--maingray);
     margin-right: 30px;
}



.about top img{
    width: 100%;
}

.aboutBottom{
     flex-direction: column;
     padding: 30;

}

.hobby{
     width:100%;
     height: auto;
}

.project{
    flex-direction: column;
     overflow: hidden;
}

.marker second{
  left: 33%;
}

.marker third{
  left: 66%;
}

.marker fourth{
  left: 100%;
} 

footer{
  height: 100px;
  background-color: var(--mainblue);
  
  color: white;    
  text-align: center;
}

footer ul {
  display: flex;
  justify-content: center;
  margin: auto;
}

footer li{
  padding: 20px;

}

footer a{
  color: white;
  
}

.aboutNorth img{
  width: 40%;
  height: 60%;
  vertical-align: center;
  position: center;
  justify-content: center;
  margin-left: 25px;
  margin-bottom: 25px;

}

.aboutNorth1 img{
  width: 49%;
  height: 60%;
  vertical-align: center;
  position: center;
  justify-content: center;
  margin-left: 0px;
  margin-bottom: 0px;

}

.aboutSouth img{
  width: 40%;
  height: 60%;
  vertical-align: left;
  position: center;
  justify-content: center;
  margin-bottom: 10px;      

}

.textualFire{
  text-align: left;
  justify-content: center;
  margin-top: 0px;
}
  
.flaming{
  text-align: center;
} 

.textualFire1{
  text-align: left;
  justify-content: center;
  margin-top: 0px;
}
  
.flaming1{
  text-align: center;
} 

.textualFire2{
  text-align: left;
  justify-content: center;
  margin-top: 0px;
}
  
.flaming2{
  text-align: center;
} 

.policies{
  text-align: center;
  justify-content: center;
  color: red;
}

.parallax1a{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/ere.jpg");
    min-height: 100%;
    justify-content: center;
    text-align: center;
}

.parallax2a{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/j.jpg");
    min-height: 100%;
    justify-content: center;
    text-align: center;
}

.parallax3a{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/4.jpg");
    justify-content: center;
    min-height: 100%;
    text-align: center;
}

.parallax4a{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/retp.jpg");
    justify-content: center;
    min-height: 100%;
    text-align: center;
}

.information{
   background-color: rgba(139, 88, 88, 0.13);
   font-size: 50px;
   padding: 20px;
   text-align: center;
}

.caption1a{
    padding: 10px;
    font-size: 24px;
    background-color: rgba(3, 0, 0, 0.3);
    position: absolute;
    width: 100%;
    text-align: center;
    justify-content: center;
    top: 46%;
}

.caption2a{
    padding: 10px;
    background-size: cover;
    font-size: 24px;
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 150%;
    color: white;
    background-color: rgba(3, 0, 0, 0.3);
}

.caption3a{
    padding: 10px;
    background-size: cover;
    font-size: 24px;
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 250%;
    color: white;
    background-color: rgba(3, 0, 0, 0.3);
}

.caption4a{
    padding: 10px;
    background-size: cover;
    font-size: 24px;
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 350%;
    color: white;
    background-color: rgba(3, 0, 0, 0.3);
}

.caption5a{
    padding: 10px;
    background-size: cover;
    font-size: 24px;
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 450%;
    color: white;
    background-color: rgba(3, 0, 0, 0.3);
}

.opening{
    padding: 10px;
    background-size: cover;
    font-size: 50px;
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 25%;
    color: white;
    background-color: rgba(3, 0, 0, 0.3);
}

.opening2{
    padding: 10px;
    background-size: cover;
    font-size: 50px;
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 130%;
    color: white;
    background-color: rgba(3, 0, 0, 0.3);
}

.opening3{
    padding: 10px;
    background-size: cover;
    font-size: 50px;
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 230%;
    color: white;
    background-color: rgba(3, 0, 0, 0.3);
}

.opening4{
  padding: 10px;
  background-size: cover;
  font-size: 50px;
  width: 100%;
  text-align: center;
  justify-content: center;
  position: absolute;
  top: 330%;
  color: white;
  background-color: rgba(3, 0, 0, 0.3);
}

.opening5{
  padding: 10px;
  background-size: cover;
  font-size: 50px;
  width: 100%;
  text-align: center;
  justify-content: center;
  position: absolute;
  top: 430%;
  color: white;
  background-color: rgba(3, 0, 0, 0.3);
}
#sun{
  justify-content: center;
  top: 80%;
  left: 50%;
  width: 220px;
  height: 50px;
  margin-top: -100px;
  margin-left: -100px;
  border: 1px;
  box-shadow: 0px 0px 128px green;
}


#sun2{
  justify-content: center;
  top: 221%;
  left: 49%;
  width: 222px;
  height: 50px;
  margin-top: -100px;
  margin-left: -100px;
  border: 1px;
  box-shadow: 0px 0px 128px red;
}

nav ul{
    display: flex;
    margin-left: 0px;
}

nav a{
    padding: 10px;
    margin-right: 0px;
}

nav a{
    color: white;
    font-size: 18px;
}

nav a:hover{
   color: rgb (114, 0, 0);
   border-bottom: 2ps solid red;
}

.copyright {
  background-color:blue;
  text-align: center;
  justify-content: center;
  display: flex;
  width: 100%;
}

.h6 {
  text-align: center;
  position: relative;
  justify-content: center;
}

.Flexbox{
    padding: 10px;
    background-size: cover;
    font-size: 50px;
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 346%;
    color: white;
    background-color: rgba(3, 0, 0, 0.3);

}

.parallaxw{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/OIP55.jpg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.parallax2w{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/R2.png");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.parallax3w{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/885551.png");
    justify-content: center;
    min-height: 100%;
    text-align: center;
}

.parallax4w{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/R9.jpg");
    justify-content: center;
    min-height: 100%;
    text-align: center;
}


.parallaxc1{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/R8.jpg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.parallaxc2{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/lm.jpg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.parallaxc3{
    background-attachment: fixed;
    background-size: cover;
    background-image:  url("images/download5.jpeg");
    justify-content: center;
    min-height: 100%;
    text-align: center;
}


.parallaxtu{
    background-attachment: fixed;
    background-size: cover;
    background-image:  url("images/wt.jpg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.parallax2tu{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/download6.jpeg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.parallax3tu{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/rth.jpg");
    justify-content: center;
    min-height: 100%;
    text-align: center;
}

.parallax4tu{
    background-attachment: fixed;
    background-size: cover;
    background-image:  url("images/kb.jpg");
    justify-content: center;
    min-height: 100%;
    text-align: center;
}


.openinge{
  padding: 10px;
    background-size: cover;
    font-size: 50px;
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 30%;
    color: white;
    background-color: rgba(3, 0, 0, 0.3);
}

.opening2e{
  padding: 10px;
    background-size: cover;
    font-size: 50px;
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 130%;
    color: white;
    background-color: rgba(3, 0, 0, 0.3);
}

.opening3e{
  padding: 10px;
    background-size: cover;
    font-size: 50px;
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 230%;
    color: white;
    background-color: rgba(3, 0, 0, 0.3);
}

.opening4e{
   padding: 10px;
    background-size: cover;
    font-size: 50px;
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 330%;
    color: white;
    background-color: rgba(3, 0, 0, 0.3);
}


.subscriptw{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images3.jpeg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.subscriptw2{
    background-attachment: fixed;
    background-size: 100%;
    background-image: url("images/t725.jpg");
    height: 100%;
    text-align: center;
    justify-content: center;
}

.subscriptw3{
    background-attachment: fixed;
    background-size: cover;
    background-image:  url("images/R12.jpg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.subscriptw4{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/OIP57.jpg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.caption1r{
    padding: 10px;
    background-size: cover; 
    font-size: 24px;
    background-color: rgba(3, 0, 0, 0.3);
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 50%;
}


.caption2r{
    padding: 10px;
    background-size: cover; 
    font-size: 24px;
    background-color: rgba(3, 0, 0, 0.3);
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 150%;
}


.caption3r{
    padding: 10px;
    background-size: cover; 
    font-size: 24px;
    background-color: rgba(3, 0, 0, 0.3);
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 250%;
}


.caption4r{
    padding: 10px;
    background-size: cover; 
    font-size: 24px;
    background-color: rgba(3, 0, 0, 0.3);
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 350%;
}

.c1a{
    padding: 10px;
    background-size: cover; 
    font-size: 50px;
    background-color: rgba(3, 0, 0, 0.3);
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 30%;
}

.c2a{
    padding: 10px;
    text-align: center;
    justify-content: center;
    background-color: rgba(3, 0, 0, 0.3);
    font-size: 50px;
    width: 100%;
    background-size: cover;
    position: absolute;
    top: 130%;
}

.c3a{
    padding: 10px;
    font-size: 50px;
    background-size: cover;
    background-color: rgba(3, 0, 0, 0.3);
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 230%;
}

.c4a{
     padding: 10px;
    font-size: 50px;
    background-size: cover;
    background-color: rgba(3, 0, 0, 0.3);
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 330%;
}

.metaclass{
    font-size: 18px;
    width: 100%;
    text-align: center;
    justify-content: left;
    position: absolute;
    top: 475%;
    border-radius: 95%;
}

.metaclass1{
    font-size: 18px;
    width: 50%;
    height: 50%;
    border-radius: 95%;
}

.metaclass2{
    font-size: 18px;
    width: 100%;
    text-align: center;
    justify-content: left;
    position: absolute;
    top: 375%;
    border-radius: 95%;
}

.metaclass1a{
    font-size: 18px;
    width: 100%;
    text-align: center;
    justify-content: left;
    position: absolute;
    top: 65%;
    border-radius: 95%;
}

.metaclass2a{
    font-size: 18px;
    width: 100%;
    text-align: center;
    justify-content: left;
    position: absolute;
    top: 165%;
    border-radius: 95%;
}

.metaclass3a{
    font-size: 18px;
    width: 100%;
    text-align: center;
    justify-content: left;
    position: absolute;
    top: 265%;
    border-radius: 95%;
}

.c1e{
    padding: 10px;
    background-size: cover;
    font-size: 50px;
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 30%;
    background-color: rgba(3, 0, 0, 0.3);
}

.c2e{
    padding: 10px;
    text-align: center;
    justify-content: center;
    font-size: 50px;
    width: 100%;
    background-size: cover;
    background-color: rgba(3, 0, 0, 0.3);
    position: absolute;
    top: 130%;
}

.c3e{
    padding: 10px;
    font-size: 50px;
    background-size: cover;
    background-color: rgba(3, 0, 0, 0.3);
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 230%;
}

.c4e{
    padding: 10px;
    font-size: 50px;
    background-size: cover;
    background-color: rgba(3, 0, 0, 0.3);
    width: 100%;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 330%;

}

.c5e{
    padding: 90px;
    font-size: 10px;
    justify-content: left;
    background-size: cover;
    top: 340%;
    left: 2%;
}

.parallax0e{
    background-attachment: fixed;
    background-size: cover;
    background-image:  url("images/Re.jpg");
    min-height: 100%;
    justify-content: center;
    text-align: center;
}

.parallax1e{
    background-attachment: fixed;
    background-size: cover;
    background-image:  url("images/R1.jpg");
    min-height: 100%;
    justify-content: centerere;
    text-align: center;
}

.parallax2e{
    background-attachment: fixed;
    background-size: cover;
    background-image:  url("images/R2e.png");
    min-height: 100%;
    justify-content: center;
    text-align: center;
}

.parallax3e{
    background-attachment: fixed;
    background-size: cover;
    background-image:  url("images/OIPe2.jpg");
    justify-content: center;
    min-height: 100%;
    text-align: center;
}

#overlay {  
  height: 500vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  background-image: url("images/76.gif");
  background-size: 100%;
  position: absolute;
  z-index: 10;
}

.bar {
  width: 400px;
  height: 30px;
}

.filter {
  transition: width 1s linear;
  width: 1%;
  height: 100%;
  background-color: red;
  animation: grow 0.3s linear infinite;
}

@keyframes grow {
  0% {
    width: 0%;
  }

  100% {
    width: 100%;
  }
}

button {
  display: inline-block;
  padding: 15px 25px;
  font-size: 24px;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  outline: none;
  color: #fff;
  background-color: #4CAF50;
  border: none;
  border-radius: 15px;
  box-shadow: 0 9px #999;
}


.hamburger {
    position: fixed;
    top: 20px;
    right: 50px;
    z-index: 30;
    cursor: pointer;
}

.bun {
    height: 4px;
    width: 30px;
    border-radius: 6px;
    background-color: white;
    border: 1px solid red;
    margin-bottom: 3px;
}

.bun2 {
    height: 8px;
    margin-right: 20px;
    width: 30px;
    border-radius: 6px;
    background-color: white;
    border: 1px solid red;
    margin-bottom: 3px;
}


.bun3 {
    height: 30px;
    margin-right: 20px;
    width: 8px;
    border-radius: 6px;
    background-color: white;
    border: 1px solid red;
    margin-bottom: 3px;
}

.bell {
  position: fixed;
  height: 30px;
  width: 50px;
  top: 14px;
  right: 40px;
  border-radius: 20px;
  background-color: gold;
  border: 2px solid greenyellow;
  z-index: -1;


}

h1{
   font-size: 50px;
}

img {
    width: 150px;
}

nav.show {
    right: 0px;
}

.navItem {
    margin-top: 20px;
    background:lightblue;
     width: 70px;
    border-radius: 15px;
    text-align: center;
    font-size: 18px;
    font-family: 'Times New Roman', Times, serif;
    background: url("images/gelbuttonleft.gif") top left no-repeat, url("images/gelbuttonright.gif") top right no-repeat, url("images/gelbuttoncenter.gif") top center repeat-x;
}
   


.navItem2 {
    margin-top: 20px;
    background-color: blue;
    width: 100px;
    border-radius: 15px;
    text-align: center;
    font-size: 18px;
    font-family: 'Times New Roman', Times, serif;
}

.navItem3 {
    margin-top: 20px;
    background-color: blue;
    width: 180px;
    border-radius: 15px;
    text-align: center;
    font-size: 18px;
    font-family: 'Times New Roman', Times, serif;
}

.navItem4 {
    margin-top: 20px;
    background-color: blue;
    width: 120px;
    border-radius: 15px;
    text-align: center;
    font-size: 18px;
    font-family: 'Times New Roman', Times, serif;
}

.navItem5 {
    margin-top: 20px;
    background-color: blue;
    width: 110px;
    border-radius: 15px;
    text-align: center;
    font-size: 18px;
    font-family: 'Times New Roman', Times, serif;
}

.navItem6 {
    margin-top: 20px;
    background-color: blue;
    width: 120px;
    border-radius: 15px;
    text-align: center;
    font-size: 18px;
    font-family: 'Times New Roman', Times, serif;
}

.navItem7 {
    margin-top: 20px;
    background-color: blue;
    width: 60px;
    border-radius: 15px;
    text-align: center;
    font-size: 18px;
    font-family: 'Times New Roman', Times, serif;
}

.navItem8 {
    margin-top: 20px;
    background-color: blue;
    width: 140px;
    border-radius: 15px;
    text-align: center;
    font-size: 18px;
    font-family: 'Times New Roman', Times, serif;
}

.navItem9 {
    margin-top: 20px;
    background-color: blue;
    width: 150px;
    border-radius: 15px;
    text-align: center;
    font-size: 18px;
    font-family: 'Times New Roman', Times, serif;
}

.navItem10 {
    margin-top: 20px;
    background-color: blue;
    width: 150px;
    border-radius: 15px;
    text-align: center;
    font-size: 18px;
    font-family: 'Times New Roman', Times, serif;
}

.song{
    margin: 20px auto;
    width: 50%;
    display: flex;
    align-items: center;
    position: relative;
    top: 100px;
    transition: top 0.4s, opacity 0.4s;
    opacity: 0; 
}

.songtext {
  text-align: left;
  margin-left: 50px;
  font-size: 20px;
}


.song.slide {
  top: 0;
  opacity: 1;
}

body.dark{
    background-color: rgb(37, 37, 37);
    color: white;
}


button.dark {
    background-color: white;
    border: 2px solid grey;

}

navtext{
  text-align: center;
  font-size: 60px;
  justify-content: center;
}

.parallax1t{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/uni.jpeg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.parallax2t{
    background-attachment: fixed;
    background-size: cover;
    background-image:  url("images/fm.jpg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.parallax3t{
    background-attachment: fixed;
    background-size: cover;
    background-image:  url("images/eq.jpg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.access{
  background-color: gold;   
  background-image: url("images/Levaithan.jpg");
  text-align: center;
  justify-content: center;
  
}

.access1{
  padding-top: 10px;
  color: blue;
}

body {font-family: Arial, Helvetica, sans-serif;}


/* Full-width input fields */
input[type=text], input[type=password] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

/* Set a style for all buttons */
button {
  background-color: #04AA6D;
  color: white;
  font-size: 20px;
  padding: 14px 20px;
  margin: 8px 0;
  border: 2px red;
  border-radius: 20px;
  cursor: pointer;
  width: 100%;
}

button:hover {
  transition-duration: 0.1s;
  display: inline-block;
  padding: 15px 25px;
  font-size: 24px;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  outline: none;
  color: #fff;
  background-color: red;
  border: none;
  border-radius: 15px;
  box-shadow: 0 9px #999;
}

/* Extra styles for the cancel button */
.cancelbtn {
  width: auto;
  padding: 10px 18px;
  background-color: #f44336;
}

/* Center the image and position the close button */
.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
  position: relative;
}

img.avatar {
  width: 10%;
  height: 20%;
  border-radius: 95%;
}

.container {
  padding: 16px;
}

span.psw {
  float: right;
  padding-top: 16px;
}

/* The Modal (background) */
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
  padding-top: 60px;
}

/* Modal Content/Box */
.modal-content {
  background-color: #fefefe;
  margin: 5% auto 15% auto; /* 5% from the top, 15% from the bottom and centered */
  border: 1px solid #888;
  width: 80%; /* Could be more or less, depending on screen size */
}

/* The Close Button (x) */
.close {
  position: absolute;
  right: 25px;
  top: 0;
  color: #000;
  font-size: 35px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: red;
  cursor: pointer;
}

/* Add Zoom Animation */
.animate {
  -webkit-animation: animatezoom 0.6s;
  animation: animatezoom 0.6s
}

@-webkit-keyframes animatezoom {
  from {-webkit-transform: scale(0)} 
  to {-webkit-transform: scale(1)}
}
  
@keyframes animatezoom {
  from {transform: scale(0)} 
  to {transform: scale(1)}
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
  span.psw {
     display: block;
     float: none;
  }
  .cancelbtn {
     width: 100%;
  }
}

.error {
  color: #FF0000;
  }

  .clansign{
    background-attachment: fixed;
    background-size: cover;
    background-image:  url("images/kr.jpg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.body1 {
    background: linear-gradient(red, yellow);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    flex-direction: column;

}

.o{
    font-family: cursive;
    box-sizing: padding-box;

}

form {
    width: 1000px;
    border: 3px solid green;
    padding: 20px;
    background: blue;
    border-radius: 20px;

}

h2 {
    text-align: center;
    margin-bottom: 40px;
}

input {
    display: block;
    border: 2px solid greenyellow;
    width: 95%;
    padding: 10px;
    margin: 10px auto;
    border-radius: 5px;
}

label {
    color: white;
    font-size: 18px;
    padding: 10px;
}

button:hover{
  transition-duration: 0.8s;
  box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
  opacity: 0.8;
}

.button:active {
  box-shadow: 0 5px #666;
  transform: translateY(4px);
}
.error {
   background: #F2DEDE;
   color: #0c0101;
   padding: 10px;
   width: 95%;
   border-radius: 5px;
   margin: 20px auto;
}

button2{
    float: right;
    font-size: 50px;
    background: rgb(35, 174, 202);
    padding: 10px 15px;
    color: #fff;
    border-radius: 5px;
    margin-right: 10px;
    border: none;
}

.eters{
    font-family: 'Times New Roman', Times, serif;
    text-align: center;
    color: red;
}

a:hover{
    opacity: .7
}

.define{
    color: goldenrod;
    font-size: 50px;
    justify-content: center;
    text-align: center;
    padding-top: 0px;
}

.timeses{
  padding-top: 30px;
}

.pokemon trove {
    padding: 10px;
    width: 100%;
    color: goldenrod;
    justify-content: center;
    position: center;
    top: 0px;
}

.parallax1kl{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/download2.jpg");
    min-height: 100%;
    text-align: center;
    justify-content: center; 
}

.parallax2kl{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/R12.jpg");
    justify-content: center;
    min-height: 100%;
    text-align: center;
}

.parallax3kl{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/t725.jpg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.parallax4kl{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/R.jpg");
    justify-content: center;
    min-height: 100%;
    text-align: center;
}

.parallax1fr{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/Scorpion.jpeg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.parallax2fr{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/download10.jpeg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.parallax3fr{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/download12.jpeg");
    justify-content: center;
    min-height: 100%;
    text-align: center;
}

.parallax4fr{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/Charybdis.jpg");
    justify-content: center;
    min-height: 100%;
    text-align: center;
}

.front{
  padding-top: 30px;
}

.forming{
    justify-content: center;
    min-height: 100%;
    padding-top: 20px;
    width: 100%;
    margin-left: 14%;
}

.postop{
  border-radius: 30px;
  padding: 0px;
  margin: 0px;
  text-align: center;
  width: 60%;
  background: linear-gradient(blue, greenyellow);
  display: inline-block;
}

.post{
  border-radius: 30px;
  padding: 0px;
  margin: 10px;
  text-align: center;
  width: 100%;
  display: inline-block;
}
 
 
.postww{
  padding: 0px;
  margin-right: 0%;
  text-align: center;
  width: 100%;
  background-image: url("images/kre.jpg");
  display: inline-block;
  min-height: 100%;
}

.post h2{
  padding: 15px;
  background-color: gold;
  color: red;

}

@media(max-width: 900px){
 .post{
   width: 100%;
   display: block;
   margin: 8px;
  }
}

header{
  background-color: red;
  text-align: center;
  padding: 30px;
  color: white;
}

.navbar{
  background-color: rgba(25, 216, 66, 0.89);
  padding: 15px;
  margin-top: 65px;
  padding-top: 18px;
  text-align: center;
  width: 99.3%;
  border: 5px solid gold;
  z-index: 0;
  position: fixed;
}

.navbar a{
  padding: 10px;
  color: white;
  text-decoration: none;
}

.navbar a:hover{
  color: red;
  border: 3px solid gold;
}


.post-form{
  border: 20px solid goldenrod;
  border-radius: 5px;
  width: 40%;
  margin: 10px auto;
}

.post-form p{
  padding: 15px; 
}

.post-form input, textarea{
  display: block;
}

.post-form textarea{
  width: 100%
}

.post-form button{
  margin: 10px;
  padding: 5px;
  background-color: red;
  color: white;
  font-size: 24px;
}

.login a{
  margin-top: 15px;
  color: orange;
  text-decoration: none;
}

.login a:hover{
  color: gold;
  border: 5px solid gold;
}

.differentes {
  color: #4CAF50;
}

li a {
    color: green;
}

body {
    background: url("images/download2.jpg");
    background-size: cover;
    height: 100vh;
    width: 100%;
    z-index: 10;
}

.login{
  justify-content: center;
  display: inline-block;
  margin-left: 25%;
  margin-top: 15%;
  padding: 15px 25px;
  font-size: 36px;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  outline: none;
  color: #fff;
  background-color: rgb(15, 173, 113);
  border: none;
  border-radius: 15px;
  box-shadow: 0 9px goldenrod;
}

.poste{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/kb.jpg");
    min-height: 100%;
    text-align: center;
    justify-content: center;
}

.poste1{
   background-attachment: fixed; 
    background-size: cover;
    background-image: url("images/kre.jpg");
    min-height: 100%;
    text-align: center;
    padding-top: 20px;
    justify-content: center;
}

.poste2{
    background-attachment: fixed;
    background-size: cover;
    background-image: url("images/kr.jpg");
    min-height: 100%;
    width: 100%;
    text-align: center;
    justify-content: center;
}

.describe{
  word-break: break-word;
  }

.post1{
  border-radius: 30px;
  padding: 0px;
  margin-left: 12%;
  width: 100%;
  background-size: cover;
  height: 100%;
  justify-content: center;
  text-align: center;
  display: inline-block;  
}

.post2{
  border: 2px solid red;
  background-color: rgb(9, 231, 21);
  border-radius: 30px;
  padding: 0px;
  margin: 10px;
  text-align: center;
  width: 100%;
  display: inline-block;
}

.hello {
  margin-top: 10%; 
}
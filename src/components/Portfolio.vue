<template>

  <header>
    <!-- ** Main Menu bar ** -->
    <h1 style="margin-left:50px">SG's Portfolio</h1>
    <ul id="menu">
      <li style="margin-right:40px"><a href="#main" class="scroll_move">Main</a></li>
      <li style="margin-right:40px"><a href="#AboutMe" class="scroll_move">About Me</a></li>
      <li><a href="#Project" class="scroll_move">Project</a></li>
    </ul>
  </header>

  <br>
  <div id="fullscreen">
    <!-- ** Main(Starting) Page ** -->
    <div id="main">
      <div id="section1">
        <div id="textbox" style="padding-top:180px; font-size:40px;">
          <hr style="border:solid 2px white;">
          <br>
          <span style="padding-left:160px; margin-top:300px; color:white;">Welcome to</span>
          <br>
          <span style="padding-left:240px; margin-top:300px; color:rgb(255, 192, 0);">Seung Gee's</span>
          <br>
          <span style="padding-left:320px; margin-bottom:300px; color:white;">Personal Portfolio</span>
          <br><br>
          <hr style="border:solid 2px white;">
          <br>
          <span style="font-size:18px;color:beige;float:right;margin-right:10px;">
            Created by : Seung Gee, Jung
            <br>
            Last Update : Jun.17.2022
          </span>
        </div>
      </div>
      <img src="./src/assets/background_img.jpg" alt="no image" style="float:right;height:750px;z-index:1;">
    </div>

    <!-- ** AboutMe Page ** -->
    <div id="AboutMe">
      <div id="section2">
        <!-- ** About Me Text Box ** -->
        <div style="padding-left:70px;padding-top:100px;display:flex;">
          <div class="rectangle"></div>
          <span style="font-size:40px;color:black;width:300px;padding-left:30px;"> About Me </span>
        </div>
        <div style="padding-left:100px;padding-top:70px;">
          <img src="./src/assets/ID_photo.jpg" alt="no image" style="width:300px;height:350px;">
        </div>
      </div>
      <div id="section3">
        <!-- ** Text Box ** -->
        <div id="textbox2">
          <br><br>
          <div id="textbox3">
            <span class="STitle" style="padding-left:50px;">Name :<br></span>
            <br>
            <span class="SAnswer" style="padding-left:100px;">정승기<br></span>
            <br>
            <span class="STitle" style="padding-left:50px;">Birth :<br></span>
            <br>
            <span class="SAnswer" style="padding-left:100px;">1998.07.17<br></span>
            <br>
            <span class="STitle" style="padding-left:50px;">Phone :<br></span>
            <br>
            <span class="SAnswer" style="padding-left:100px;">010-6205-3776<br></span>
            <br>
            <span class="STitle" style="padding-left:50px;">E-mail :<br></span>
            <br>
            <span class="SAnswer" style="padding-left:100px;">wjdtmdrl777@naver.com<br></span>
            <br>
          </div>
          <div id="textbox4">
            <span class="STitle" style="padding-left:30px;text-align:left;">Education :<br></span>
            <ul>
              <li style="margin-left:40px;font-size:20px;">신성고등학교 졸업</li>
              <li style="margin-left:40px;font-size:20px;">성균관대학교 전자전기공학부 4학년 1학기 수료</li>
            </ul>
            <br><br>
            <span class="STitle" style="padding-left:30px;text-align:left;">Strength :<br></span>
            <ul>
              <li style="margin-left:40px;margin-right:20px;font-size:20px;">긍적적인 성격으로 쉽게 좌절하지 않는<br> 끈기</li>
              <li style="margin-left:40px;margin-right:20px;font-size:20px;">항상 열린 마음으로 주변과 소통하며<br> 배워가는 자세</li>
              <li style="margin-left:40px;margin-right:20px;font-size:20px;">후회가 남지 않도록 맡은 일에 최선을<br> 다하는 열정</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- ** Project Page ** -->
    <div id="Project">
      <div style="padding-top:100px;padding-left:70px;display:flex;">
        <div class="rectangle"></div>
        <span style="font-size:40px;color:black;width:300px;padding-left:30px;"> Project </span>
      </div>
      <div id="textbox5">
        <div style="display:inline-block;">
          <img src="./src/assets/CNN.png" alt="no image" style="width:450px;height:220px;padding-left:50px;padding-top:40px;">
          <br>
          <img src="./src/assets/DDD.png" alt="no image" style="width:400px;height:200px;padding-left:70px;padding-top:40px;">
        </div>
        <div style="float:right;width:700px;padding-top:70px;">
          <span class="STitle" style="padding-left:50px;text-align:left;font-size:30px;">우수학부연구생 (2021.12 ~ 2022.03) :<br></span>
          <ul>
            <li style="margin-left:60px;font-size:20px;">CNN Lenet5 구조 구현</li>
            <li style="margin-left:60px;font-size:20px;">MNIST를 학습하는 인공지능 HW 구현</li>
            <li style="margin-left:60px;font-size:20px;">Systolic Array를 이용한 Convolution을 통해 속도 향상</li>
          </ul>

          <br><br><br><br>
          <span class="STitle" style="padding-left:50px;text-align:left;font-size:30px;">종합 설계 프로젝트 (2022.03 ~ 2022.06):<br></span>
          <ul>
            <li style="margin-left:60px;font-size:20px;">졸음 운전 판별 인공지능 구현</li>
            <li style="margin-left:60px;font-size:20px;">Matlab을 이용하여 눈과 차선을 인식하는 인공지능 구현</li>
            <li style="margin-left:60px;font-size:20px;">온라인 발표회 우수상 수상</li>
          </ul>
        </div>
      </div>
    </div>

  </div>
</template>

<script>



export default {
  name: 'ExampleVue',
  props: {
    msg: String
  }
}



</script>

<style scoped>
#fullscreen{
  width:100%;
  height:2500px;
}
header{ /* Main Menu Bar */
  position:fixed;
  height:75px;
  width:100%;
  top:0;
  color:white;
  background-color: rgb(208, 206, 206);
  font-weight: bold;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index:3;
}
#menu{ /* List in Main Menu Bar */
  display: flex;
  list-style:none;
  margin-right:10%;
  font-size:20px;
}
#main{ /* Main Page of Site */
  width:100%;
  height:750px;
  float:left;
}
#section1{ /* Blank Box of Main Page */
  position:absolute;
  width:800px;
  height:750px;
  background-color:rgb(111, 219, 255);
  border-right:2px solid white;
  text-align:center;
}
#AboutMe{ /* About Me Page */
  width:100%;
  height:750px;
  clear:left;
}
#section2{ /* Section in About Me Page */
  width:33%;
  height:750px;
  background-color:rgb(214,233,238);
  border-top:50px solid white;
  float:left;
}
#section3{ /* Section in About Me Page */
  height:750px;
  width:500px;
  float:left;
}
#textbox2{ /* Text box in About Me Page */
  margin-left:15%;
  margin-top:25%;
  height:600px;
  width:900px;
  background-color:beige;
  border-radius:30px;
  border:2px solid black;
}
#textbox3{
  display:inline-block;
  width:400px;
  border-right:2px dashed black;
}
#textbox4{
  float:right;
  width:490px;
}
#Project{ /* Project Page */
  width:100%;
  height:750px;
  margin-top:50px;
}
#textbox5{
  margin-top:50px;
  margin-left:150px;
  width:80%;
  height:550px;
  border:4px solid black;
  border-radius:30px;
}

/* Class Definition */
.rectangle{
  width: 0px;
  height: 0px;
  border-bottom: 60px solid gray;
  border-left: 10px solid gray;
  border-right: 10px solid gray;
}
.STitle{
  font-size:40px;
  color:rgb(0, 176, 80);
  font-weight:600;
}
.SAnswer{
  font-size:25px;
  font-weight:400;
}
a{
  color:white;
  text-decoration:none;
}
</style>
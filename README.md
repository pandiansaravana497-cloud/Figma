# Ex09 Event Registration Web Application
## Date:

## AIM:
To design, develop and deploy a web application for event registration.

## DESIGN STEPS:

### Step 1:
Create a new frame.

### Step 2:
Select any one preset size of your choice.

### Step 3:
Select the shapes you need.

### Step 4:
Import images as needed.

### Step 5:
Create pages based on your need and link them.

### Step 6:

Validate the HTML and CSS code.

### Step 6:

Publish the website in the given URL.

## DESIGN TOOL:
Figma

## CODE:
~~~
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Sports Events Registration</title>

  <!-- Google Font -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;600;700&family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">

  <style>
    *{
      margin:0;
      padding:0;
      box-sizing:border-box;
    }

    body{
      font-family:'Poppins',sans-serif;
      min-height:100vh;
      display:flex;
      justify-content:center;
      align-items:center;
      overflow:hidden;
      background:
      radial-gradient(circle at top,#2b2b74 0%,#0c1336 45%),
      linear-gradient(to top,#7b240f,#1a1b54);
      position:relative;
    }

    /* Background Glow */
    body::before{
      content:'';
      position:absolute;
      width:900px;
      height:900px;
      background:radial-gradient(circle,#ff6b0040,transparent 70%);
      bottom:-450px;
      left:-200px;
    }

    body::after{
      content:'';
      position:absolute;
      width:800px;
      height:800px;
      background:radial-gradient(circle,#6c63ff33,transparent 70%);
      top:-350px;
      right:-150px;
    }

    .container{
      width:650px;
      max-width:95%;
      background:#f7f7f7;
      border-radius:30px;
      box-shadow:0 10px 40px rgba(0,0,0,0.3);
      overflow:hidden;
      position:relative;
      z-index:10;
      animation:fadeIn 0.7s ease;
    }

    @keyframes fadeIn{
      from{
        opacity:0;
        transform:translateY(20px);
      }
      to{
        opacity:1;
        transform:translateY(0);
      }
    }

    .screen{
      display:none;
      padding:40px;
    }

    .screen.active{
      display:block;
    }

    h1{
      text-align:center;
      font-family:'Oswald',sans-serif;
      color:#f26a00;
      font-size:60px;
      margin-bottom:5px;
      text-transform:uppercase;
    }

    .subtitle{
      text-align:center;
      color:#7d8ca2;
      margin-bottom:35px;
      font-size:20px;
    }

    .form-group{
      margin-bottom:25px;
    }

    label{
      display:block;
      margin-bottom:10px;
      font-weight:600;
      color:#202020;
    }

    input{
      width:100%;
      padding:18px;
      border-radius:14px;
      border:1px solid #d9d9d9;
      font-size:18px;
      outline:none;
      background:#fff;
    }

    input:focus{
      border-color:#f26a00;
      box-shadow:0 0 0 4px rgba(242,106,0,0.15);
    }

    .btn{
      width:100%;
      padding:18px;
      border:none;
      border-radius:14px;
      background:#f26a00;
      color:white;
      font-size:22px;
      font-weight:600;
      cursor:pointer;
      transition:0.3s;
      margin-top:10px;
    }

    .btn:hover{
      background:#d95f00;
      transform:translateY(-2px);
    }

    /* Events */

    .events-list{
      max-height:520px;
      overflow-y:auto;
      padding-right:8px;
    }

    .event-card{
      background:white;
      border:2px solid #e8e8e8;
      border-radius:22px;
      padding:22px;
      display:flex;
      gap:20px;
      margin-bottom:20px;
      cursor:pointer;
      transition:0.3s;
      align-items:flex-start;
    }

    .event-card:hover{
      transform:translateY(-4px);
      border-color:#f26a00;
      box-shadow:0 10px 25px rgba(0,0,0,0.08);
    }

    .event-card.selected{
      border-color:#f26a00;
      background:#fffaf5;
    }

    .event-icon{
      width:70px;
      height:70px;
      border-radius:18px;
      background:#fff4ea;
      display:flex;
      justify-content:center;
      align-items:center;
      font-size:36px;
    }

    .event-details h3{
      font-size:28px;
      color:#1c2235;
      margin-bottom:10px;
    }

    .meta{
      display:flex;
      gap:16px;
      flex-wrap:wrap;
      color:#75839b;
      font-size:16px;
      margin-bottom:14px;
    }

    .tag{
      display:inline-block;
      background:#edf1f5;
      padding:7px 15px;
      border-radius:30px;
      font-size:15px;
      font-weight:600;
      color:#6b7c93;
    }

    /* Success */

    .success{
      text-align:center;
      padding:50px 40px;
    }

    .check{
      width:100px;
      height:100px;
      margin:0 auto 25px;
      border-radius:50%;
      background:#dff7e5;
      display:flex;
      justify-content:center;
      align-items:center;
      font-size:50px;
      color:#24b35d;
    }

    .success h2{
      color:#24b35d;
      font-size:48px;
      font-family:'Oswald',sans-serif;
      margin-bottom:20px;
    }

    .success p{
      color:#7a879d;
      line-height:1.8;
      font-size:20px;
    }

    .next-box{
      background:#f4f6f8;
      padding:25px;
      border-radius:18px;
      margin:35px 0;
      text-align:left;
    }

    .next-box h4{
      margin-bottom:15px;
      font-size:24px;
      color:#1b2233;
    }

    .next-box li{
      margin-bottom:12px;
      color:#718096;
      line-height:1.6;
      font-size:17px;
    }

    @media(max-width:700px){

      h1{
        font-size:42px;
      }

      .screen{
        padding:25px;
      }

      .event-card{
        flex-direction:column;
      }

      .event-details h3{
        font-size:24px;
      }

      .btn{
        font-size:18px;
      }
    }

  </style>
</head>
<body>

  <div class="container">

    <!-- SCREEN 1 -->
    <div class="screen active" id="screen1">

      <h1>SPORTS EVENTS</h1>
      <p class="subtitle">Register for upcoming events</p>

      <div class="form-group">
        <label>Full Name</label>
        <input type="text" id="name" placeholder="Enter your name">
      </div>

      <div class="form-group">
        <label>Email Address</label>
        <input type="email" id="email" placeholder="Enter your email">
      </div>

      <button class="btn" onclick="goToEvents()">
        Continue to Events →
      </button>

    </div>

    <!-- SCREEN 2 -->
    <div class="screen" id="screen2">

      <h1>WELCOME!</h1>
      <p class="subtitle">Select an event to register</p>

      <div class="events-list">

        <div class="event-card" onclick="selectEvent(this)">
          <div class="event-icon"></div>

          <div class="event-details">
            <h3>Marathon Championship</h3>

            <div class="meta">
              <span> December 15, 2025</span>
              <span> City Sports Complex</span>
              <span> 500 participants</span>
            </div>

            <span class="tag">Running</span>
          </div>
        </div>

        <div class="event-card" onclick="selectEvent(this)">
          <div class="event-icon"></div>

          <div class="event-details">
            <h3>Basketball Tournament</h3>

            <div class="meta">
              <span> January 10, 2026</span>
              <span> Downtown Arena</span>
              <span> 16 participants</span>
            </div>

            <span class="tag">Basketball</span>
          </div>
        </div>

        <div class="event-card" onclick="selectEvent(this)">
          <div class="event-icon"></div>

          <div class="event-details">
            <h3>Swimming Competition</h3>

            <div class="meta">
              <span> December 28, 2025</span>
              <span> Olympic Pool Center</span>
              <span> 200 participants</span>
            </div>

            <span class="tag">Swimming</span>
          </div>
        </div>

        <div class="event-card" onclick="selectEvent(this)">
          <div class="event-icon"></div>

          <div class="event-details">
            <h3>Football League</h3>

            <div class="meta">
              <span> February 5, 2026</span>
              <span> National Stadium</span>
              <span> 300 participants</span>
            </div>

            <span class="tag">Football</span>
          </div>
        </div>

      </div>

      <button class="btn" onclick="registerEvent()">
        Register Selected Event
      </button>

    </div>

    <!-- SCREEN 3 -->
    <div class="screen success" id="screen3">

      <div class="check">✓</div>

      <h2>THANKS FOR REGISTRATION!</h2>

      <p>
        Congratulations! Your registration has been successfully completed.
        We're excited to see you at the event!
      </p>

      <div class="next-box">

        <h4>What's Next?</h4>

        <ul>
          <li>
             A confirmation email has been sent to your email address
            with all event details
          </li>

          <li>
            🗓 Complete event schedule and instructions will be shared
            7 days before the event
          </li>
        </ul>

      </div>

      <button class="btn" onclick="restart()">
        Register Another Event
      </button>

    </div>

  </div>

  <script>

    function goToEvents(){

      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;

      if(name === '' || email === ''){
        alert('Please fill all fields');
        return;
      }

      document.getElementById('screen1').classList.remove('active');
      document.getElementById('screen2').classList.add('active');
    }

    function selectEvent(card){

      const cards = document.querySelectorAll('.event-card');

      cards.forEach(c=>{
        c.classList.remove('selected');
      });

      card.classList.add('selected');
    }

    function registerEvent(){

      const selected = document.querySelector('.event-card.selected');

      if(!selected){
        alert('Please select an event');
        return;
      }

      document.getElementById('screen2').classList.remove('active');
      document.getElementById('screen3').classList.add('active');
    }

    function restart(){

      document.getElementById('screen3').classList.remove('active');
      document.getElementById('screen1').classList.add('active');

      document.getElementById('name').value = '';
      document.getElementById('email').value = '';

      const cards = document.querySelectorAll('.event-card');

      cards.forEach(c=>{
        c.classList.remove('selected');
      });
    }

  </script>

</body>
</html>
~~~

## OUTPUT:

<img width="1920" height="1080" alt="Screenshot (19)" src="https://github.com/user-attachments/assets/33a66925-6238-4093-a890-8989366772d1" />

<img width="1920" height="1080" alt="Screenshot (20)" src="https://github.com/user-attachments/assets/25cd65ff-94af-4efd-8659-3c84bdcb6a4d" />

<img width="1920" height="1080" alt="Screenshot (21)" src="https://github.com/user-attachments/assets/556b52a8-536d-409a-af8e-be6eb3c56c5e" />

## RESULT:
The program to design, develop and deploy a web application for event registration is completed successfully.

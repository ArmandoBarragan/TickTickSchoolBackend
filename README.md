<h1>Tick Tick School backend app</h1>
Frontend repository: <a href="https://github.com/montesp/tick-tick-school-frontend">https://github.com/montesp/tick-tick-school-frontend</a>
<h2>Project contributers</h2>
<ul>
    <li><div>
        <span>Armando Barragán Pacheco.</span><br/>
        <span><strong>Role:</strong> Backend developer, software architect.</span><br/>
        <span><strong>Email:</strong> armandobp765@gmail.com</span><br/>
        <span><strong>Github user:</strong> ArmandoBarragan</span><br/>
    </div></li>
    <li><div>
            <span>Pavel Ivan Montes Bissio.</span><br/>
            <span><strong>Role:</strong> Frontend developer, UI/UX designer.</span><br/>
            <span><strong>Email:</strong> pavelmontes22@gmail.com</span><br/>
            <span><strong>Github user:</strong> montesp</span><br/>
    </div></li>
</ul>

<h2>API usage</h2>
<p>Models of the database are, at the moment, User, Task and Subject.
A neither a task nor a subject can be created without any
users, so you need to create a few to test them.</p>
<p>You can call the api in local with the address <code>localhost:8000</code>
and use the following urls:</p>
<ul>
<li>Users:
    <ul>
    <li>users/signup/ to create a new user.</li>
    <p>Parameters: email, password, password_confirmation, first_name, last_name</p>
    <li>api-token-auth to get the user's token.</li>
    <p>Parameters: Username and password</p>
    <p><b>KEEP IN MIND: This URL and parameters MIGHT BE CHANGED on future updates.</b></p>
    <p>Note: This will return 404 if credentials are incorrect</p>
    <li>users/{{pk}} to get a user's email, firstname and lastnames</li>
    <li>users/ This does not work. It's only for staff, which has not been planned as a functionality yet.</li>
</ul>
</li>
<li>
    Subjects:
    <ul>
    <li>POST subjects/</li>
    Parameters: (Being * a required param) name*, teacher, classroom.
    <li></   
    <li>GET subjects/ returns name, student, teacher, classroom of all user's subjects.</li>
    <li>GET subjects/{subject_pk} returns name, student, teacher, classroom of a specific subject.</li>
    </ul>
</li>
<li>
    Tasks:
    <ul>
        <li>POST tasks/</li>
        Parameters: name*, subject*, description, status.
        If a status is not sent, it's set as 'pendiente' as default.
        <li>GET tasks/ returns name, subject, description and status of all user's tasks.</li>
        <li>GET tasks/{ task_pk } returns name, subject, description and status a specific task.</li>
    </ul>
</li>
</ul>
<h3>Authorization</h3>
<p>The project works with token authorization, so for each request it is necessary to set 'Authorization: Token {{token}}'
in it's header, except for the login and signup urls.
</p>
<h2>Local installation for frontends</h2>
<p>To have this project installed for development purposes, it is necessary to
first install docker and docker compose. To do so, you can follow the given documentation:</p>
<ul>
    <li><a href="https://docs.docker.com/engine/install/ubuntu/">Docker installation guide on Ubuntu</a></li>
    <li><a href="https://docs.docker.com/compose/install/">Docker Compose installation guide on Ubuntu.</a></li>
</ul>
<p>After having those installed, you need to cd your way into the project till you are in the root, right next
to the local.yml file, and execute the following command: <code> docker-compose -f local.yml up --build -d</code>,
and then <code>docker-compose -f local.yml exec app python3 manage.py migrate</code>.These commands will do just enough 
if you are working on the frontend and neet to test the API calls. If you want to run the project as a 
backend dev, you can either work on it on a container or the Django listener with <code>python3
manage.py runserver</code>. If you opt for the container option and are gonna work during full sessions on the compose files,
you will probably want to export the file variable every session so that you don't have to write <code>-f local.yml</code>. You can do this by 
executing the following command: <code>export COMPOSE_FILE=local.yml</code>.
</p>
<h2>Local installation for backends</h2>
<p>Backends can install their project with either docker-compose or directly executing <code>python3 manage.py migrate</code>
and <code>python3 manage.py runserver</code>. They just need to change the CONTAINER_ENVIRON
variable from the local.yml file to false to stop using docker.</p>

<h2>Project deployment</h2>
<p>For deployment it is as necessary to have docker and docker compose installed as it is needed on development.
You, as well, need to cd your way into the root of the project. Environment variables have to be changed
on the production.yml file.</p>

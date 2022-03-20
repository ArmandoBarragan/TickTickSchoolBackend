<h1>Tick Tick School backend app</h1>
<h2>Project contributers</h2>
<ul>
    <li><div>
        <span>Armando Brragán Pacheco.</span><br/>
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
<p></p>
<h2>Local installation</h2>
<p>To have this project installed for development purposes, it is necessary to
first install docker and docker compose. To do so, you can follow the given documentation:</p>
<ul>
    <li><a href="https://docs.docker.com/engine/install/ubuntu/">Docker installation guide on Ubuntu</a></li>
    <li><a href="https://docs.docker.com/compose/install/">Docker Compose installation guide on Ubuntu.</a></li>
</ul>
<p>After having those installed, you need to cd your way into the project till you are in the root, right next
to the local.yml file, and execute the following command: <code> docker-compose -f local.yml up --build -d</code>.
This command will do just enough if you are working on the frontend and neet to test the API calls. If you want to
run the project as a backend dev, you can either work on it on a container or the Django listener with <code>python3
manage.py runserver</code>. If you opt for the container option, you will probably want to export the file variable 
every session so that you don't have to write <code>-f local.yml</code>. You can do this by executing the following
command: <code>export COMPOSE_FILE=local.yml</code>.
</p>

<h2>Project deployment</h2>
<p>For deployment it is as necessary to have docker and docker compose installed as it is needed on development.
You, as well, need to cd your way into the root of the project. Environment variables have to be changed
on the production.yml file.</p>

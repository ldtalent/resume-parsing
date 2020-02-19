'''
    This script is to convert the list of skills into csv file
'''
import pandas as pd
import os

def make_csv(directory):
    Software_Engineering = [
        "C\+\+",
        "J2EE",
        "Git",
        "OpenShift",
        "Singularity Containerization",
        "Regex",
        "UML Diagrams",
        "Apache Kafka",
        "Scala",
        "VBA",
        "Rust",
        "LISP",
        "Perl",
        "Fortran",
        "Golang",
        "Assembly",
        "Clojure",
        "Kotlin",
        "Dart",
        "WebAssembly",
        "\.NET",
        "\.NET Core",
        "Ansible",
        "Elixir",
        "Erlang",
        "NoSQL",
        "WebRTC",
        "C\#",
        "C",
        "SQL",
        "Java",
        "HTML",
        "CSS",
        "JSX",
        "Python",
        "R",
        "UNIX",
        "Ruby",
        "XML",
        "PHP",
        "Docker",
        "Objective C",
        "JavaScript",
        "REST API"
    ]
    Web_Mobile_and_Desktop_Application_Development = [
        "Elm",
        "Mocha",
        "Chai",
        "Bulma",
        "Semantic-UI",
        "Swift",
        "Ember.js",
        "VulcanJS",
        "MeteorJS",
        "Google Tag Manager",
        "Google Analytics",
        "WebSockets",
        "Gatsby",
        "Postman",
        "Cucumber",
        "Wix",
        "Bootstrap",
        "GraphQL",
        "Angular",
        "Typescript",
        "MongoDB",
        "ExpressJS",
        "Data Semantic Layers",
        "SEO",
        "Redux",
        "Webpack",
        "Apollo GraphQL",
        "ECMA",
        "CSS Flex",
        "jQuery",
        "UI Design",
        "UX Design",
        "Interaction Design",
        "Material Design",
        "Flow JS",
        "Babel JS",
        "Ionic",
        "Grind Rocks for Node",
        "Postgres",
        "MySQL",
        "Vagrant",
        "VirtualBox",
        "WebGL",
        "DevOps",
        "Site Reliability",
        "ASP.NET",
        "Drupal",
        "Cordova",
        "Xamarin",
        "Flutter",
        "Microsoft SQL Server",
        "SQLite",
        "Redis",
        "MariaDB",
        "OracleDB",
        "DynamoDB",
        "Cassandra",
        "Couchbase",
        "Chef",
        "ReasonML",
        "Django",
        "Nodejs",
        "Laravel",
        "Flask",
        "React",
        "Ruby on rails",
        "React native",
        "Wordpress",
        "Android native app development",
        "iOS native app development",
        "Windows Application Development",
        "Mac Application Development",
        "Chrome Extension Development",
        "Firefox Extension Development",
        "Safari Extension Development",
        "Internet Explorer Extension Development",
        "XCode",
        "Vue.js",
        "Visual Studio",
        "Android Studio"
    ]
    Artificial_Intelligence = [
        "keras",
        "KNIME",
        "OCR",
        "PyTorch",
        "Torch",
        "Autonomous Vehicles and Self Driving Cars",
        "Artificial intelligence",
        "Machine learning",
        "Deep learning",
        "Natural language processing",
        "Speech recognition",
        "Probabilistic graphical models",
        "Robotics",
        "Computer vision",
        "Reinforcement learning",
        "Data mining",
        "Quadrocopters",
        "Drones"
    ]
    Special_Technologies_and_Expertise_Areas = [
        "Cyber Security",
        "Hackintosh",
        "Sound Engineering",
        "GDPR Compliance",
        "Logic Pro X",
        "Final Cut Pro",
        "Pro Tools",
        "Autodesk Maya",
        "Salesforce Development",
        "Photoshop",
        "Adobe Premiere Pro",
        "IBM DB2",
        "Maven",
        "Turtle Logo",
        "Lego Mindstorms",
        "Autodesk Revit",
        "Google Sketchup",
        "Rhino",
        "3Dmax",
        "CorelDraw",
        "Canva",
        "Inkscape",
        "GIMP",
        "InDesign",
        "Proteomics",
        "Microsoft Excel",
        "Design Modo",
        "Salesforce Pardot",
        "EMR Software",
        "Data Analytics",
        "R for Statistics",
        "Data Science",
        "Adobe Illustrator",
        "3D modeling",
        ".obj files",
        "Marketplaces",
        "Product Lifecycle Management",
        "Agile",
        "SCRUM",
        "Kanban",
        "Kaizen",
        "Lean",
        "JMP",
        "Minitab",
        "Shopify",
        "Unreal Engine Game Development",
        "Computational Linguistics",
        "Fourier Transforms",
        "Kubernetes",
        "Microservices",
        "Jupyter",
        "Augmented Reality AR",
        "Virtual Reality VR",
        "Apache Spark",
        "Puppet",
        "CryEngine",
        "QTP/ HP for QA Testing",
        "Appium for QA Testing",
        "Seetest for QA Testing",
        "Apache Jmeter",
        "Load runner",
        "SOAP UI",
        "HP Quality Centre",
        "Version One",
        "Bugzilla",
        "TestCaseLab",
        "qTest",
        "TestRail",
        "TestLink",
        "PractiTest",
        "TestLodge",
        "QACoverage",
        "Fogbuz",
        "TFS",
        "Serverless Architecture",
        "Blockchain",
        "iOT",
        "Bioinformatics",
        "Unity Game Design and Development",
        "Chatbots",
        "Data visualization",
        "Web scrapers",
        "Unity Augmented Reality Design and Development",
        "Browser automation",
        "Mapreduce",
        "Unity Virtual Reality Design and Development",
        "Solidity",
        "Genomics",
        "Ethereum"
    ]
    APIs_and_Packages = [
        "Google NLP API",
        "Socket.IO",
        "Sequelize",
        "Mapbox",
        "Github API",
        "Matplotlib",
        "scikit-learn",
        "PyQt5",
        "ADA Compliance",
        "Pandas",
        "Slack API",
        "Tensorflow",
        "Blockchain API",
        "Ripple API",
        "D3",
        "Vega",
        "Vega Lite",
        "Biopython",
        "Python Selenium",
        "Selenium",
        "Google Maps API",
        "Mailchimp API",
        "Sendgrid API",
        "Twitter APIs",
        "Stripe API",
        "Twilio API",
        "Apache Hadoop",
        "Facebook API",
        "Google Computer Vision API",
        "Google API",
        "AWS Cloud Compliance",
        "HIPAA Cloud Compliance",
        "Finance Cloud Compliance",
        "Government Cloud Compliance (US DoD)",
        "Paypal API"
    ]
    Electrical_and_Mechanical_Engineering = [
        "Autodesk",
        ".dxf files",
        "Digital Manufacturing",
        "AutoCAD",
        "MATLAB",
        "Verilog",
        "VHDL",
        "LabVIEW",
        "ANSYS",
        "Intel x86",
        "Hypermesh",
        "SolidWorks",
        "Medical Devices",
        "SPICE (ic design)"
    ]
    Other_Skills = [
        "AWS EC2",
        "AWS Redshift",
        "AWS CloudFront",
        "AWS S3",
        "AWS DynamoDB",
        "AWS ECR",
        "AWS Elastic Beanstalk",
        "Amazon ElastiCache",
        "AWS ElasticMapReduce",
        "AWS IoT",
        "AWS Key Management Service",
        "AWS RDS",
        "Electronic Health Records",
        "Embedded Software",
        "Microcontrollers",
        "Multithreaded Programming",
        "ARM Programming",
        "RTOS",
        "Quality Assurance QA",
        "Oracle BI",
        "SAP",
        "Plotly",
        "Eclipse",
        "Cloud Foundry",
        "Kubernetes",
        "Terraform",
        "Product Management",
        "Google Cloud",
        "AWS",
        "Firebase",
        "SWOT Analysis",
        "FMEA Analysis",
        "VoC Strategy Analysis",
        "PEST Analysis",
        "Pareto Analysis",
        "JIRA",
        "Trello",
        "Asana",
        "Microsoft Project",
        "SAP",
        "Tableau",
        "AWS Elasticsearch",
        "Linux",
        "Windows",
        "MacOS",
        "Raspberry Pi",
        "Azure",
        "Arduino",
        "Heroku",
        "IBM Cloud Watson",
        "AWS Lambda",
        "Spring",
        "Hibernate",
        "DROOLS",
        "OSCache",
        "SOAP",
        "Actuate Espreadsheet",
        "Autosys",
        "XSLT",
        "Cocoon"
    ]
    
    dict_skills={
        'Software_Engineering':Software_Engineering,
        'Web_Mobile_and_Desktop_Application_Development':Web_Mobile_and_Desktop_Application_Development,
        'Artificial_Intelligence':Artificial_Intelligence,
        'Special_Technologies_and_Expertise_Areas':Special_Technologies_and_Expertise_Areas, 
        'APIs_and_Packages':APIs_and_Packages,
        'Electrical_and_Mechanical_Engineering':Electrical_and_Mechanical_Engineering,
        'Other_Skills':Other_Skills

    }
    


    df=pd.DataFrame.from_dict(
        dict_skills,
        orient='index'
    )
        
    df=df.transpose()

    print(df.head())
        
    df.to_csv(os.path.join(directory,'csv_files/Skills_list.csv'))

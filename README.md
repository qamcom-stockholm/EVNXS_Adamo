# EVNXS_Adamo
Directory structure -------------------------
First level:
    .devcontainer           used when attach vs-code to a running container 
    .github                 contains the action files
    .vscode                 vscode settings for compile and debug
    00-Apps                 contains Applications in the project
    01-Modules              contains Modules in the project
    02-Functions            contains Functions or SW Features in the project
    Communication_Library   contains all the required libraries for communication among SW components

Second level:
    00-Apps
        SW_App_1            all the files related specifically to the App_1
            build           script files for building the application
            unit_tests      script files for testing the application
        SW_App_2            same as SW_App_1, but for App_2
    01-Modules
        SW_Module_1         all the files related specifically to the Module_1
            build
            unit_tests
    02-Functions
        SW_Function_1   all the files related specifically to the Function_1
            build
            inc         include folder
            src         source folder
            unit_tests
    Communication_Library
        MessageBroker   all the files for running and configuring a RabbitMQ message broker.
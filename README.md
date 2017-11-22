# sanic-script

sanic-script is an extension for Sanic that adds support for writing external commands to your application.

sanic-script是Sanic框架的一个扩展库，为你的Web应用提供扩展命令支持。


## install

    $ pip install sanic-script


## quick start

    #!/usr/bin/python3
    # -*- coding: utf-8 -*-
    
    from runserver import app
    from sanic_script import Manager
    
    manager = Manager(app)
    
    @manager.command
    def hello():
        print("hello")

    if __name__ == "__main__":
        manager.run()
        
        
## 
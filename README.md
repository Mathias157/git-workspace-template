# software_title

Credits goes to the CodeRefinery team and [this workshop](https://coderefinery.github.io/reproducible-python/) for inspiring this template

This is an example of using pixi as the package manager, which is a user-friendly package manager to lock the *exact* dependencies you used at the time, not just the main packages from an `environment.yml`, which later could result in updated and error-giving sub-dependencies.

Follow the [installation instructions](#installation), and pixi will do the rest of the installation work, when you run the example script for the first time: 
```
pixi run src/software_title/script.py --a test --b 5
```

> [!NOTE]  
> I needed to add a `#!/usr/bin/env python` on top of the python file and add executable permissions `chmod +x <script.py>` in order to make it runable with `pixi run <script.py>`


## Purpose

(...)


## Requirements

(dependencies and their versions or version ranges)


## Installation instructions

This requires pixi, which can be installed on Linux/Mac with the command:
`curl -fsSL https://pixi.sh/install.sh | bash`

or Windows:
`powershell -ExecutionPolicy ByPass -c "iwr -useb https://pixi.sh/install.ps1 | iex"`

## Example

You can build the docs using a virtual environment with the dependencies in [environment.yml](environment.yml) and the following command in the top level of this folder:
```
sphinx-build docs build
```
Then, open the build/index.html to inspect the generated documentation and automated API Reference that describes python functions, classes etc. 
You can use the "Go Live" extension of VS Code to inspect the index.html.


## Documentation

- Tutorials covering key functionality
- Reference documentation (e.g. API) covering all functionality


## Authors and recommended citation

(...)


## License

See [LICENSE](LICENSE) 


## Contribution guide

(...)

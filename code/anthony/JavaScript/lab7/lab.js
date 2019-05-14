let typeSpace = document.getElementById('typearea');
let alert = document.getElementById('alertpage');
let typeList = "import argparse \nimport sys \nfrom pathlib import Path \nimport discord \nimport pkg_resources \nimport aiohttp\nimport websockets\nimport platform\ndef show_version():\nentries = []\n\nentries.append('- Python v{0.major}.{0.minor}.{0.micro}-{0.releaselevel}'.format(sys.version_info))\nversion_info = discord.version_info\nentries.append('- discord.py v{0.major}.{0.minor}.{0.micro}-{0.releaselevel}'.format(version_info))\nif version_info.releaselevel != 'final':\npkg = pkg_resources.get_distribution('discord.py')if pkg:\nentries.append('    - discord.py pkg_resources: v{0}'.format(pkg.version))\n\nentries.append('- aiohttp v{0.__version__}'.format(aiohttp))\nentries.append('- websockets v{0.__version__}'.format(websockets))\nuname = platform.uname()\nentries.append('- system info: {0.system} {0.release} {0.version}'.format(uname))\nprint('\n'.join(entries))\n\ndef core(parser, args):\nif args.version:\nshow_version()\n\nbot_template = '''#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\nfrom discord.ext import commands\nimport discord\nimport config\nclass Bot(commands.{base}):\ndef __init__(self, **kwargs):\nsuper().__init__(command_prefix=commands.when_mentioned_or('{prefix}'), **kwargs)\nfor cog in config.cogs:\ntry:\nself.load_extension(cog)\nexcept Exception as exc:\nprint('Could not load extension {{0}} due to {{1.__class__.__name__}}: {{1}}'.format(cog, exc))\nasync def on_ready(self):\nprint('Logged on as {{0}} (ID: {{0.id}})'.format(self.user))\nbot = Bot()\n# write general commands here\nbot.run(config.token)\n'''\n\ngitignore_template = '''# Byte-compiled / optimized / DLL files\n__pycache__/\n*.py[cod]\n*$py.class\n# C extensions\n*.so\n";
let output = '';
let startindex = 0;
let endindex = 0;
let rando;
let counter = 0;
let interval;


typeSpace.addEventListener('keypress', function (event) {
    event.preventDefault();
    rando = Math.floor(Math.random() * 5) + 1;
    endindex += rando;

    while (startindex < endindex) {
        output += typeList[startindex];
        startindex++;
    }
    typeSpace.textContent = output;
    startindex = endindex;

    if (event.keyCode == 32) {
        counter++;
        if (counter == 5) {
            interval = setInterval(function () {
                if (alert.style.display == 'none') {
                    alert.style.display = 'block';
                } else {
                    alert.style.display = 'none';
                }
            }, 500);
        }

    }
    if (event.keyCode == 13) {
        clearInterval(interval);
        counter = 0;
    }
    console.log(event);
})
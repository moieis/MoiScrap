#                                                                  MoiScrap !

###### Deploy Selenium And Merge It With PyWebIo = WebApp For Scraping News Web  Count(10)  Then Tr Into Ar Lang


<p align="center">
  <img src="logoo.png" alt="Image Description"  width="200" height="200">
</p>



<div style="text-align:center">
    <img src="exm.gif" alt="Your GIF description" />
</div>



---
#### (1) Imports and requirements ;
---
```
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio.platform import *
import numpy
import os
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
import argparse
from pywebio import start_server
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from deep_translator import GoogleTranslator
from pywebio import config

```

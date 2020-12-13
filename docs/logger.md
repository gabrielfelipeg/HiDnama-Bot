# Logger

Specifies the basic log standard for all modules using the python logging package.

## Logger()

Set the future logs to uses the following message format:
```python
'%(asctime)s|%(levelname)s|%(name)s.%(funcName)s|%(message)s'
```
| Attribute | Description | 
|:---------: |:----:|
| asctime | ISO_8601 |
|levelname | log level |
|name | package's name followed by the module's name|
|funcName | function`s name |
|message | log message |

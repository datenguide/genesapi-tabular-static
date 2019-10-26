# genesapi-tabular-static

Store rendered tables from https://tabular.genesapi.org as static file on server.

In comparison to the query results from the tabular API from
[genesapi-tabular](https://github.com/datenguide/genesapi-tabular), which are updated
when the underlying data from GENESIS is updated, the tables created from this service
will never change and always be available under their url.

## Usage:

For query examples, see [genesapi-tabular](https://github.com/datenguide/genesapi-tabular)

Querying will redirect you to the static file:

[https://static.tabular.genesapi.org/?data=12613:BEV002(NAT,GES)&time=2017&region=01&labels=name](https://static.tabular.genesapi.org/?data=12613:BEV002(NAT,GES)&time=2017&region=01&labels=name)

## Info

This service is part of the [datengui.de](https://datengui.de)-stack.

[Github](https://github.com/datenguide)

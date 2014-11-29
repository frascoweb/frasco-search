# Frasco-Search

Provides full-text search capabilities using [Elastisearch](http://www.elasticsearch.org/)
and [elasticsearch-py](http://elasticsearch-py.readthedocs.org/en/master/).

## Installation

    pip install frasco-search

## Setup

Feature name: search

Options:

 - *hosts*: list of hosts to connect to (see `elasticsearch.Elasticsearch`)
 - *pagination_per_page*: default number of items per page when using
   pagination (default: 10)
 - *index_models*: list of models name to automatically index
 - *autocomplete*: autocomplete configuration (see further)
 - *autocomplete_url*: url for the autocomplete endpoint
   (default: `/_autocomplete/<doc_type>/<field>`)
 - *autocomplete_endpoint*: name of the autocomplete endpoint (default: autocomplete)
 - *indexes*: mapping of index and document types. allows for automatically
   selecting the correct index based on the document_type. This value should
   be a dict where keys are index names and values a list of document type names.
 - *use_only_one_index*: whether to the default index when the document type
   has no associated index in the *indexes* config. Otherwise, will use the
   document type name as index name (default: False)
 - *default_index*: default index name when *use_only_one_index* is true (default: frasco)
 - *created_indexes*: whether to automatically create indexes on startup (default: true)
 - *indexes_settings*: a dict where keys are index names and values a dict of options
   as described [here](http://www.elasticsearch.org/guide/en/elasticsearch/guide/current/_index_settings.html).
 - *mapping*: a dict where keys are document type names and values a mapping
   dict as described [here](http://www.elasticsearch.org/guide/en/elasticsearch/guide/current/mapping-intro.html)
 - *use_redis_partial_models*: whether to use Frasco-Redis partial models feature
   where retreiving models in the result set (default: false).

## Indexes and document types

## Autocomplete

## Actions

### create\_search\_index

### delete\_search\_index

### create\_search\_mapping

### index\_doc\_for\_search

### index\_model\_for\_search

### delete\_search\_doc

### delete\_search\_model

### fetch\_search\_doc

### search

### search\_model

### autocomplete
---
title: rest-quarkus_example API v1.0.0-SNAPSHOT
language_tabs:
  - java: Java
  - shell: Shell
  - python: Python
language_clients:
  - shell: curl
  - node: request
  - java: unirest
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="rest-quarkus_example-api">rest-quarkus_example API v1.0.0-SNAPSHOT</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

<h1 id="rest-quarkus_example-api-movies">Movies</h1>

This package is created to manage all the movies stored in the database,
  here we can find 2 classes; Movie and MovieResources, where are all the
 endpoints linked to the following methods:
 *  getMovies
 *  countMovies
 *  createMovies
 *  getMovieAuthorById
 *  updateMovie
 *  deleteMovie

## getMovies

> Code samples

```java
URL obj = new URL("/movies");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```shell
# You can also use wget
curl -X GET /movies

```

```python
import requests

r = requests.get('/movies')

print(r.json())

```

`GET /movies`

 Return all the data about the movies that exists

<h3 id="getmovies-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|The return is ok|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Something went wrong (BAD_REQUEST)|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The path was incorrect|None|

<aside class="success">
This operation does not require authentication
</aside>

## createMovies

> Code samples

```java
URL obj = new URL("/movies");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```shell
# You can also use wget
curl -X POST /movies \
  -H 'Content-Type: application/json'

```

```python
import requests
headers = {
  'Content-Type': 'application/json'
}

r = requests.post('/movies', headers = headers)

print(r.json())

```

`POST /movies`

Add a movie including title, id, and author

> Body parameter

```json
{
  "type": "object",
  "properties": {
    "id": {
      "format": "int64",
      "type": "integer"
    },
    "title": {
      "type": "string"
    },
    "author": {
      "type": "string"
    },
    "duration": {
      "format": "int32",
      "type": "integer"
    }
  }
}
```

<h3 id="createmovies-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Movie](#schemamovie)|false|none|

<h3 id="createmovies-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|The movie is added correctly|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Something went wrong (BAD_REQUEST)|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The path was incorrect|None|

<aside class="success">
This operation does not require authentication
</aside>

## getMovieAuthorById

> Code samples

```java
URL obj = new URL("/movies/author/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```shell
# You can also use wget
curl -X GET /movies/author/{id} \
  -H 'Accept: application/json'

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/movies/author/{id}', headers = headers)

print(r.json())

```

`GET /movies/author/{id}`

Returns a movie knowing the id of the author

<h3 id="getmovieauthorbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer(int64)|true|none|

> Example responses

> 200 Response

```json
{
  "type": "object"
}
```

<h3 id="getmovieauthorbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|The return is ok|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Something went wrong (BAD_REQUEST)|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The path was incorrect|None|

<h3 id="getmovieauthorbyid-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="rest-quarkus_example-api-songs">Songs</h1>

This package is created to manage all the songs stored in the database,
  here we can find 2 classes; Songs and SongResources, where are all the
  endpoints linked to the following methods:
  - getSongs 
  - countSongs
  - createSongs
  - totalDurationSongs
  - updateGroupSongs
  - deleteSong

## getSongs

> Code samples

```java
URL obj = new URL("/songs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```shell
# You can also use wget
curl -X GET /songs

```

```python
import requests

r = requests.get('/songs')

print(r.json())

```

`GET /songs`

 Return all the data about the songs that exists

<h3 id="getsongs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|The return is ok|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Something went wrong (BAD_REQUEST)|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The path was incorrect|None|

<aside class="success">
This operation does not require authentication
</aside>

## createSong

> Code samples

```java
URL obj = new URL("/songs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```shell
# You can also use wget
curl -X POST /songs \
  -H 'Content-Type: application/json'

```

```python
import requests
headers = {
  'Content-Type': 'application/json'
}

r = requests.post('/songs', headers = headers)

print(r.json())

```

`POST /songs`

Add a song including name, id, duration and group which belongs

> Body parameter

```json
{
  "type": "object",
  "properties": {
    "id": {
      "format": "int32",
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "group": {
      "type": "string"
    },
    "duration": {
      "format": "int64",
      "type": "integer"
    }
  }
}
```

<h3 id="createsong-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Song](#schemasong)|false|none|

<h3 id="createsong-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|The song is added correctly|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Something went wrong|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The path was incorrect|None|

<aside class="success">
This operation does not require authentication
</aside>

## deleteSong

> Code samples

```java
URL obj = new URL("/songs/delete/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```shell
# You can also use wget
curl -X DELETE /songs/delete/{id}

```

```python
import requests

r = requests.delete('/songs/delete/{id}')

print(r.json())

```

`DELETE /songs/delete/{id}`

Deletes  a song from the DB knowing the id of the song

<h3 id="deletesong-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer(int32)|true|none|

<h3 id="deletesong-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|The song was removed correctly|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Something went wrong (BAD_REQUEST)|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The path was incorrect|None|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_Movie">Movie</h2>
<!-- backwards compatibility -->
<a id="schemamovie"></a>
<a id="schema_Movie"></a>
<a id="tocSmovie"></a>
<a id="tocsmovie"></a>

```json
{
  "type": "object",
  "properties": {
    "id": {
      "format": "int64",
      "type": "integer"
    },
    "title": {
      "type": "string"
    },
    "author": {
      "type": "string"
    },
    "duration": {
      "format": "int32",
      "type": "integer"
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|title|string|false|none|none|
|author|string|false|none|none|
|duration|integer(int32)|false|none|none|

<h2 id="tocS_Song">Song</h2>
<!-- backwards compatibility -->
<a id="schemasong"></a>
<a id="schema_Song"></a>
<a id="tocSsong"></a>
<a id="tocssong"></a>

```json
{
  "type": "object",
  "properties": {
    "id": {
      "format": "int32",
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "group": {
      "type": "string"
    },
    "duration": {
      "format": "int64",
      "type": "integer"
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int32)|false|none|none|
|name|string|false|none|none|
|group|string|false|none|none|
|duration|integer(int64)|false|none|none|


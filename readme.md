# LLM API Server README

## API Route

### POST /rcmd/openai
- Recommend three songs based on the input diary.

#### Request format
```json
{
    "user_id": "string",
    "diary": "string"
}
```
#### Response format
```json
{
    "musics": [
        {
            "title": "string",
            "artist": "string",
            "url": "string"
        },
        {
            "title": "string",
            "artist": "string",
            "url": "string"
        },
        {
            "title": "string",
            "artist": "string",
            "url": "string"
        }
    ]
}
```
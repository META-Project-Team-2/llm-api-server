# LLM API Server README

## API Route

### POST /rcmd/openai
- Recommend three songs based on the input diary.

#### Request format
```json
{
    "user_id": "string",
    "diary": "string",
    "emotions": ["string", ...] (optional),
    "filters": {
        ... (optional)
    }
}
```
#### Response format
```json
{
    "musics": [
        ...
    ]
}
```

### PUT /rcmd/openai
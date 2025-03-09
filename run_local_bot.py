import json
import local_bot

# Load local LLM configuration
with open('local_bot_config.json') as f:
    local_config = json.load(f)

# Load main configuration (for prompts and limits)
with open('bot_config.json') as f:
    main_config = json.load(f)

# Run the local LLM bot logic using both configs
local_bot.run(local_config, main_config)

# Troubleshooting Connection Errors

## Common Issues and Solutions

### 1. **Connection Error**
**Error Message:** "Error processing query with RAG: Connection error"

**Possible Causes:**
- No internet connection
- API service is down or unreachable
- Network firewall blocking the connection
- Ollama not running (if using local models)

**Solutions:**
1. **Check Internet Connection**: Ensure you have an active internet connection
2. **Try Different Model Provider**: 
   - Go to the sidebar
   - Select a different provider (OpenAI, Anthropic, Google, etc.)
   - Enter the corresponding API key
3. **For Ollama Users**:
   - Make sure Ollama is installed and running
   - Run `ollama serve` in a terminal
   - Verify Ollama is accessible at `http://localhost:11434`
4. **Wait and Retry**: Sometimes API services have temporary issues

---

### 2. **API Key Error**
**Error Message:** Contains "401", "403", "authentication", or "API key"

**Solutions:**
1. **Configure API Key**:
   - Open the sidebar in the app
   - Find the "API Configuration" section
   - Enter your valid API key for the selected provider
   
2. **Get API Keys**:
   - **OpenAI**: https://platform.openai.com/api-keys
   - **Anthropic**: https://console.anthropic.com/
   - **Google**: https://makersuite.google.com/app/apikey
   - **Grok (xAI)**: https://console.x.ai/
   - **DeepSeek**: https://platform.deepseek.com/

3. **Verify API Key**:
   - Check that the key is active
   - Ensure you have sufficient credits/quota
   - Make sure you're using the correct key for the selected provider

---

### 3. **No Data Loaded**
**Error Message:** "No property data available"

**Solutions:**
1. **Load Data**:
   - Go to the sidebar
   - Find "Data Sources" section
   - Upload CSV/Excel files OR provide URLs to property data
   
2. **Verify Data Format**:
   - Ensure your CSV/Excel has property information
   - Check that required columns are present

---

### 4. **Rate Limit Exceeded**
**Error Message:** Contains "429", "rate limit", or "too many requests"

**Solutions:**
1. **Wait**: API providers have rate limits - wait a few minutes
2. **Switch Provider**: Use a different model provider temporarily
3. **Upgrade Plan**: Consider upgrading your API plan for higher limits

---

## Quick Setup Guide

### For First-Time Users:

1. **Choose a Model Provider**:
   - **Free Option**: Use Ollama (requires local installation)
   - **Paid Options**: OpenAI, Anthropic, Google, Grok, DeepSeek

2. **Configure API Key** (if not using Ollama):
   ```
   - Open sidebar
   - Select your provider
   - Enter API key
   - Click "Validate & Save"
   ```

3. **Load Property Data**:
   ```
   - Upload CSV/Excel files, OR
   - Provide URLs to property datasets
   - Click "Load Data"
   ```

4. **Start Chatting**:
   - Ask questions about properties
   - Request comparisons
   - Get market insights

---

## Environment Variables (Alternative Setup)

Instead of entering API keys in the UI, you can set them in a `.env` file:

```env
# OpenAI
OPENAI_API_KEY=sk-...

# Anthropic
ANTHROPIC_API_KEY=sk-ant-...

# Google
GOOGLE_API_KEY=AI...

# Grok (xAI)
XAI_API_KEY=xai-...

# DeepSeek
DEEPSEEK_API_KEY=sk-...
```

Place this file in the root directory of the project.

---

## Still Having Issues?

1. **Check the Terminal**: Look for detailed error messages in the terminal where Streamlit is running
2. **Check Logs**: Review application logs for more details
3. **Restart the App**: Sometimes a fresh start helps
4. **Update Dependencies**: Run `pip install -r requirements.txt --upgrade`

---

## Model Provider Status

Check if your selected provider is operational:
- **OpenAI**: https://status.openai.com/
- **Anthropic**: https://status.anthropic.com/
- **Google**: https://status.cloud.google.com/

---

## Contact & Support

If you continue experiencing issues:
1. Check the GitHub repository for known issues
2. Review the documentation
3. Open a new issue with error details

# Sample Python/Flask 
### Daytona-Pydantic-ai-App
 
This repository contains a sample Flask web application that demonstrates integration with **Daytona** for managing development environments. The app also showcases AI-powered functionality using **OpenAI API** and a responsive interface built with **Tailwind CSS**.  

---

## 🚀 Getting Started  

### Open Using Daytona  

1. **Install Daytona**:  
   Follow the [Daytona installation guide](https://www.daytona.io/docs/installation/installation/) to set up Daytona on your machine.  

2. **Create the Workspace**:  
   Use Daytona to clone and set up this sample repository:  
   ```bash  
   daytona create https://github.com/sayantan007pal/Daytona-Pydantic-ai-App.git  
   ```  

3. **Set Up Environment Variables**:  
   Copy `.env.example` to `.env` and update it with your OpenAI API key:  
   ```bash  
   cp .env.example .env  
   ```  
   Ensure the following variable is set:  
   - `OPENAI_API_KEY`: Your OpenAI API key.  

4. **Install Dependencies**:  
   Inside the created workspace, install the required Python packages:  
   ```bash  
   pip install -r requirements.txt  
   ```  

5. **Start the Application**:  
   Launch the Flask application:  
   ```bash  
   python app.py  
   ```  
   Your app should now be running at `http://localhost:8080`!  

---

## ✨ Features  

- **AI-Powered Prompt Responses**: Leverages OpenAI's API to process and respond to user prompts dynamically.  
- **Responsive Design**: Built with Tailwind CSS for an intuitive, mobile-friendly UI.  
- **Environment Management**: Uses Daytona to ensure a consistent and containerized development setup.  
- **Dynamic Configuration**: Supports `.env` for managing API keys and configurations seamlessly.  

---

## 📝 License  

This project is licensed under the MIT License. See the `LICENSE` file for details.  

---

## 🔗 Related Links  

- **Daytona Documentation**: [https://github.com/daytonaio/daytona](https://github.com/daytonaio/daytona)  
- **Daytona Samples Index**: [Daytona Samples Index File](https://github.com/daytonaio/daytona/blob/main/hack/samples/index.json)  
- **OpenAI API**: [OpenAI API Documentation](https://platform.openai.com/docs/)  

---

## 💬 Feedback  

If you encounter any issues or have suggestions, feel free to contribute or open an issue. Once merged, submit the sample into the [Daytona Samples Index](https://github.com/daytonaio/daytona/blob/main/hack/samples/index.json) to complete your integration!  

Happy coding! 🚀  
```

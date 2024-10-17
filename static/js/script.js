// Chatbot functionality
const chatbotToggle = document.getElementById('chatbot-toggle');
const chatbotContent = document.getElementById('chatbot-content');

chatbotToggle.addEventListener('click', () => {
    chatbotContent.style.display = chatbotContent.style.display === 'none' ? 'block' : 'none';
});

// Dummy chatbot interaction
const chatbotMessages = document.getElementById('chatbot-messages');
const chatbotInput = document.getElementById('chatbot-input');

chatbotInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        const message = document.createElement('p');
        message.textContent = `You: ${chatbotInput.value}`;
        chatbotMessages.appendChild(message);
        chatbotInput.value = '';
        // Add an automatic response after a short delay
        setTimeout(() => {
            const botMessage = document.createElement('p');
            botMessage.textContent = 'Bot: Thanks for your query, we will get back to you soon!';
            chatbotMessages.appendChild(botMessage);
        }, 1000);
    }
});

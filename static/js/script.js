document.addEventListener('DOMContentLoaded', () => {
    const chatWindow = document.getElementById('chat-window');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const typingIndicator = document.getElementById('typing-indicator');

    // Focus input on load
    userInput.focus();

    // Event Listeners
    sendBtn.addEventListener('click', handleSend);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleSend();
    });

    async function handleSend() {
        const query = userInput.value.trim();
        if (!query) return;

        // 1. Add User Message to UI
        appendMessage('user', query);
        userInput.value = '';
        
        // 2. Show Loading State
        showLoading(true);
        scrollToBottom();

        try {
            // 3. API Call to Backend
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query: query })
            });

            if (!response.ok) throw new Error('Network response was not ok');

            const data = await response.json();

            // 4. Add Assistant Message to UI
            if (data.answer) {
                appendMessage('assistant', data.answer, data.sources);
            } else {
                throw new Error('Empty response from server');
            }

        } catch (error) {
            console.error('Error:', error);
            appendMessage('error', 'I apologize, but I encountered an error processing your request. Please ensure the system is online and try again.');
        } finally {
            showLoading(false);
            scrollToBottom();
        }
    }

    function appendMessage(role, text, sources = []) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', `${role}-message`);

        let contentHtml = `<div class="bubble ${role === 'error' ? 'error-bubble' : ''}">
            <p>${text}</p>`;

        // Add Sources if available
        if (sources && sources.length > 0) {
            contentHtml += `
                <div class="sources-container">
                    <span class="sources-label">Sources:</span>
                    <div class="sources-list">
                        ${sources.map(src => `<span class="source-tag"><i class="fas fa-file-alt"></i> ${src}</span>`).join('')}
                    </div>
                </div>`;
        }

        contentHtml += `</div>`;
        messageDiv.innerHTML = contentHtml;
        chatWindow.appendChild(messageDiv);
    }

    function showLoading(show) {
        if (show) {
            typingIndicator.classList.remove('hidden');
        } else {
            typingIndicator.classList.add('hidden');
        }
    }

    function scrollToBottom() {
        chatWindow.parentElement.scrollTop = chatWindow.parentElement.scrollHeight;
    }
});
// static/js/script.js
document.addEventListener('DOMContentLoaded', function() {
    const toggleButtons = document.querySelectorAll('.toggle-answer-btn');

    toggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            const questionId = this.dataset.questionId;
            const answerDiv = document.getElementById('answer-' + questionId);

            if (answerDiv) {
                if (answerDiv.style.display === 'none' || answerDiv.style.display === '') {
                    answerDiv.style.display = 'block';
                    this.textContent = 'Сховати відповідь';
                } else {
                    answerDiv.style.display = 'none';
                    this.textContent = 'Показати відповідь';
                }
            }
        });
    });
});
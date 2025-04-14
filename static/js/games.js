/* Additional styles for games */

/* Memory Game */
.memory-card {
    position: relative;
    aspect-ratio: 1;
    perspective: 1000px;
    cursor: pointer;
  }
  
  .card-front,
  .card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    transition: transform 0.6s;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 0.5rem;
    font-size: 2rem;
  }
  
  .card-front {
    background-color: white;
    transform: rotateY(180deg);
  }
  
  .card-back {
    background-color: var(--purple-600);
    color: white;
  }
  
  .memory-card.flipped .card-front {
    transform: rotateY(0deg);
  }
  
  .memory-card.flipped .card-back {
    transform: rotateY(180deg);
  }
  
  .memory-card.matched .card-front {
    background-color: var(--green-100);
    border: 2px solid var(--green-300);
  }
  
  /* Speed Math */
  .math-problem {
    font-size: 2.5rem;
    font-weight: bold;
    text-align: center;
    margin: 2rem 0;
  }
  
  .math-problem.correct {
    color: var(--green-600);
  }
  
  .math-problem.incorrect {
    color: var(--red-600);
  }
  
  .answer-input {
    display: flex;
    justify-content: center;
    margin-bottom: 2rem;
  }
  
  .answer-input input {
    font-size: 1.5rem;
    padding: 0.75rem 1rem;
    width: 150px;
    text-align: center;
    border: 2px solid var(--purple-300);
    border-radius: 0.5rem;
    margin-right: 0.5rem;
  }
  
  .answer-input input:focus {
    outline: none;
    border-color: var(--purple-500);
    box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.3);
  }
  
  .answer-input input.error {
    border-color: var(--red-500);
    animation: shake 0.5s;
  }
  
  .answer-input button {
    font-size: 1.25rem;
  }
  
  .timer-bar {
    height: 8px;
    background-color: var(--gray-200);
    border-radius: 4px;
    margin-bottom: 2rem;
    overflow: hidden;
  }
  
  .timer-fill {
    height: 100%;
    background-color: var(--purple-500);
    width: 100%;
    transition: width 0.1s linear;
  }
  
  .duration-slider {
    display: flex;
    align-items: center;
    gap: 1rem;
  }
  
  .duration-slider input {
    flex: 1;
  }
  
  /* Reaction Test */
  .reaction-area {
    position: relative;
    width: 100%;
    height: 300px;
    background-color: var(--red-500);
    border-radius: 0.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 1.5rem;
    font-weight: bold;
    cursor: pointer;
    margin-bottom: 2rem;
    overflow: hidden;
    user-select: none;
  }
  
  .reaction-area.waiting {
    background-color: var(--green-500);
  }
  
  .reaction-area.ready {
    background-color: var(--gray-200);
    color: var(--gray-700);
  }
  
  .attempts-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 2rem;
  }
  
  .attempt-item {
    background-color: white;
    border-radius: 0.5rem;
    padding: 0.75rem 1rem;
    font-weight: bold;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  }
  
  .attempt-item.best {
    background-color: var(--green-100);
    border: 1px solid var(--green-300);
  }
  
  .attempt-item.worst {
    background-color: var(--red-100);
    border: 1px solid var(--red-300);
  }
  
  /* Animations */
  @keyframes shake {
    0%,
    100% {
      transform: translateX(0);
    }
    10%,
    30%,
    50%,
    70%,
    90% {
      transform: translateX(-5px);
    }
    20%,
    40%,
    60%,
    80% {
      transform: translateX(5px);
    }
  }  
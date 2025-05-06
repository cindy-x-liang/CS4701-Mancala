<script lang="ts">
	import Board from '$lib/components/Board.svelte';
	import GameControls from '$lib/components/GameControls.svelte';
	import type { GameState, NextStateResponse, AIActionResponse, GameMode } from '$lib/types';
  
	let gameState: GameState = {
	  board: { 'p1': [4, 4, 4, 4, 4, 4, 0], 'p2': [4, 4, 4, 4, 4, 4, 0] },
	  turn: 'p1'
	};
	
	let gameMode: GameMode = 'alphabeta';
	let gameStatus: string = 'Playing';
	let isGameOver: boolean = false;
	let processingAIMove: boolean = false;
	
	const handleMove = async (event: CustomEvent<{ pit: number }>) =>  {
	  if (isGameOver || gameState.turn !== 'p1' || processingAIMove) return;
	  
	  const pit = event.detail.pit;
	  
	  try {
		const response = await fetch('/api/next_state', {
		  method: 'POST',
		  headers: {
			'Content-Type': 'application/json'
		  },
		  body: JSON.stringify({
			game_state: gameState,
			action: pit
		  })
		});
		
		if (!response.ok) {
		  const errorData: { error: string } = await response.json();
		  gameStatus = errorData.error || 'Error making move';
		  return;
		}
		
		gameState = await response.json();
		gameStatus = `You selected pit ${pit}`;
		
		if (checkGameOver()) {
		  determineWinner();
		  return;
		}
		
		if (gameState.turn === 'p2') {
		  setTimeout(handleAITurn, 500);
		}
	  } catch (error) {
		console.error('Error:', error);
		gameStatus = 'Error communicating with server';
	  }
	}
	
	const handleAITurn = async () => {
	  if (isGameOver || gameState.turn !== 'p2' || processingAIMove) return;
	  
	  processingAIMove = true;
	  
	  try {
		while (gameState.turn === 'p2' && !isGameOver) {
		  await makeAIMove();
		  
		  if (checkGameOver()) {
			determineWinner();
			break;
		  }
		  
		  if (gameState.turn === 'p2') {
			await new Promise(resolve => setTimeout(resolve, 1000));
		  }
		}
	  } finally {
		processingAIMove = false;
	  }
	}
	
	const makeAIMove = async () => {
	  if (isGameOver) return;
	  
	  gameStatus = 'AI is thinking...';
	  
	  try {
		const aiEndpoint = `/api/${gameMode}_action`;
		const actionResponse = await fetch(aiEndpoint, {
		  method: 'POST',
		  headers: {
			'Content-Type': 'application/json'
		  },
		  body: JSON.stringify({
			board: gameState.board,
			turn: gameState.turn
		  })
		});
		
		if (!actionResponse.ok) {
		  const errorData: { error: string } = await actionResponse.json();
		  gameStatus = errorData.error || 'AI error';
		  return;
		}
		
		const actionData: AIActionResponse = await actionResponse.json();
		const aiAction = actionData.action;
		
		const moveResponse = await fetch('/api/next_state', {
		  method: 'POST',
		  headers: {
			'Content-Type': 'application/json'
		  },
		  body: JSON.stringify({
			game_state: gameState,
			action: aiAction
		  })
		});
		
		if (!moveResponse.ok) {
		  const errorData: { error: string } = await moveResponse.json();
		  gameStatus = errorData.error || 'Error executing AI move';
		  return;
		}
		
		gameState = await moveResponse.json();
		gameStatus = `AI selected pit ${aiAction}`;
	  } catch (error) {
		console.error('Error:', error);
		gameStatus = 'Error communicating with server';
	  }
	}
	
	const checkGameOver = (): boolean => {
	  const p1EmptyPits = gameState.board.p1.slice(0, 6).every(stones => stones === 0);
	  const p2EmptyPits = gameState.board.p2.slice(0, 6).every(stones => stones === 0);
	  
	  return p1EmptyPits || p2EmptyPits;
	}
	
	const determineWinner = () => {
	  isGameOver = true;
	  const p1Score = gameState.board.p1[6];
	  const p2Score = gameState.board.p2[6];
	  
	  if (p1Score > p2Score) {
		gameStatus = `Game over! You win with ${p1Score} points to ${p2Score}!`;
	  } else if (p2Score > p1Score) {
		gameStatus = `Game over! AI wins with ${p2Score} points to ${p1Score}!`;
	  } else {
		gameStatus = `Game over! It's a tie with ${p1Score} points each!`;
	  }
	}
	
	const restartGame = () => {
	  gameState = {
		board: { 'p1': [4, 4, 4, 4, 4, 4, 0], 'p2': [4, 4, 4, 4, 4, 4, 0] },
		turn: 'p1'
	  };
	  isGameOver = false;
	  gameStatus = 'Game restarted! Your turn.';
	}
	
	const changeGameMode = (event: CustomEvent<Event>) => {
	  const target = event.detail.target as HTMLSelectElement;
	  gameMode = target.value as GameMode;
	  
	  if (!isGameOver) {
		gameStatus = `Game mode changed to ${gameMode}`;
	  }
	}
  </script>
  
  <svelte:head>
	<title>MancalAI</title>
  </svelte:head>
  
  <main>
	<h1>MancalAI</h1>
	
	<div class="game-container">
	  <GameControls 
		{gameStatus}
		{gameMode} 
		on:restart={restartGame} 
		on:change={changeGameMode} 
	  />
	  
	  <Board 
		board={gameState.board} 
		turn={gameState.turn} 
		on:move={handleMove} 
		{isGameOver}
	  />
	</div>
  </main>
  
  <style>
	main {
	  text-align: center;
	  max-width: 800px;
	  margin: 0 auto;
	  padding: 20px;
	  font-family: sans-serif;
	}
	
	.game-container {
	  display: flex;
	  flex-direction: column;
	}
  </style>
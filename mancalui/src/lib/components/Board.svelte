<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import type { Board as BoardType, PlayerType } from '$lib/types';
    
    export let board: BoardType = { 'p1': [4, 4, 4, 4, 4, 4, 0], 'p2': [4, 4, 4, 4, 4, 4, 0] };
    export let turn: PlayerType = 'p1';
    export let isGameOver: boolean = false;
    
    const dispatch = createEventDispatcher<{
      move: { pit: number }
    }>();
    
    const handlePitClick = (player: PlayerType, pitIndex: number) => {
      if (player === 'p1' && turn === 'p1' && !isGameOver && board[player][pitIndex] > 0) {
        dispatch('move', { pit: pitIndex });
      }
    }
    
    const isPitClickable = (player: PlayerType, pitIndex: number): boolean => {
      return player === 'p1' && turn === 'p1' && !isGameOver && board[player][pitIndex] > 0;
    }
  </script>
  
  <div class="board-container">
    <div class="board">
      <div class="mancala mancala-p2">
        <div class="store">
          <span class="stone-count">{board.p2[6]}</span>
        </div>
      </div>
      
      <div class="play-area">
        <div class="pits pits-p2">
          {#each [...Array(6).keys()].reverse() as pitIndex}
            <div class="pit">
              <span class="stone-count">{board.p2[pitIndex]}</span>
            </div>
          {/each}
        </div>
        
        <div class="pits pits-p1">
          {#each [...Array(6).keys()] as pitIndex}
            <div 
              class="pit"
              class:clickable={isPitClickable('p1', pitIndex)}
              on:click={() => handlePitClick('p1', pitIndex)}
            >
              <span class="stone-count">{board.p1[pitIndex]}</span>
            </div>
          {/each}
        </div>
      </div>
      
      <div class="mancala mancala-p1">
        <div class="store">
          <span class="stone-count">{board.p1[6]}</span>
        </div>
      </div>
    </div>
    
    <div class="labels">
      <div class="player-label p2-label">AI (Player 2)</div>
      <div class="player-label p1-label">You (Player 1)</div>
    </div>
    
    <div class="turn-indicator">
      {#if !isGameOver}
        <div class="turn-badge" class:your-turn={turn === 'p1'} class:ai-turn={turn === 'p2'}>
          {turn === 'p1' ? 'Your Turn' : 'AI Turn'}
        </div>
      {/if}
    </div>
  </div>
  
<style>
  .board-container {
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }

  .board {
    display: flex;
    align-items: center;
    background-color: #8d6e63;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    margin-bottom: 20px;
  }

  .play-area {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .pits {
    display: flex;
    justify-content: space-around;
  }

  .pit {
    width: 65px;
    height: 65px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.3);
    margin: 0 5px;
  }

  .pits-p1 .pit {
    background-color: #5D4037;
  }

  .pits-p2 .pit {
    background-color: #8D6E63;
  }

  .pit.clickable {
    cursor: pointer;
  }

  .pit.clickable:hover {
    opacity: 0.8;
  }

  .mancala {
    padding: 0 10px;
  }

  .store {
    width: 80px;
    height: 150px;
    border-radius: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.4);
  }

  .mancala-p1 .store {
    background-color: #5D4037;
  }

  .mancala-p2 .store {
    background-color: #8D6E63;
  }

  .stone-count {
    font-size: 18px;
    font-weight: 500;
    color: #efebe9;
  }

  .labels {
    display: flex;
    justify-content: space-between;
    margin: 10px 100px;
    color: #424242;
  }

  .player-label {
    font-size: 16px;
    font-weight: 500;
    padding: 4px 12px;
    border-radius: 4px;
    background-color: #e0e0e0;
  }

  .turn-indicator {
    text-align: center;
    margin-top: 15px;
  }

  .turn-badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 4px;
    font-weight: 500;
    font-size: 14px;
    background-color: #f5f5f5;
    color: #424242;
  }
</style>
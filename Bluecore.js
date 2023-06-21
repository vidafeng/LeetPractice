function blindMice(str) {
  let numBlind = 0

  // replace all white spaces in substrings
  const splitStr = str.split('C');
  const leftSplit = splitStr[0].replace(/\s+/g, '');
  const rightSplit = splitStr[1].replace(/\s+/g, '');

  let i = 0;
  let j = 1;

  while (j <= leftSplit.length) {
    if (leftSplit[i] === 'M' && leftSplit[j] === '~') {
      numBlind++;
    }
    i = j + 1;
    j = i + 1;
  }

  let a = 0;
  let b = 1;

  while (b <= rightSplit.length) {
    if (rightSplit[a] === '~' && rightSplit[b] === 'M') {
      numBlind++;
    }
    a = b + 1;
    b = a + 1;
  }

  return numBlind;
}

// TEST CASES
// console.log(blindMice("M~~M ~MM~C~MM~M~"))
// console.log(blindMice("~M~M~MC M~~M"))
// console.log(blindMice("~M CM~~M~M"))



function raceWinner(raceObj) {

  let winningTime = '24:60:60';
  let secondBest = '24:60:60';
  let winner = '0';
  let dnf = 0;

  raceObj.forEach(function(race) {
    if (race.time === 'dnf') {
      dnf++;
    }

    if (race.time < winningTime) {
      secondBest = winningTime;
      winningTime = race.time;

      winner = race.name;
    }
  })

  if (dnf === raceObj.length) {
    return ('There is no winner');
  } else if (dnf === raceObj.length - 1) {
    return `${winner} won by no test`
  } else {
    // convert time stamps into seconds
    const a = secondBest.split(':');
    const b = winningTime.split(':');

    const secondBestSeconds = (+a[0]) * 60 * 60 + (+a[1]) * 60 + (+a[2]);
    const winningTimeSeconds = (+b[0]) * 60 * 60 + (+b[1]) * 60 + (+b[2]);
    // console.log(secondBestSeconds, winningTimeSeconds)

    const timeWonSeconds = secondBestSeconds - winningTimeSeconds;

    // convert seconds back to hours/mins/seconds
    const hours = Math.floor(timeWonSeconds / 60 / 60);
    const min = Math.floor(timeWonSeconds / 60) - (hours * 60);
    const seconds = timeWonSeconds % 60;

    return `${winner} won by ${hours} hours, ${min} minutes, and ${seconds} seconds`
  }
}

// TEST CASES
// raceObj = [
//   {
//     name: 'Samuel',
//     time: '05:42:14'
//   },
//   {
//     name: 'Fred',
//     time: '05:12:53'
//   },
//   {
//     name: 'Cynthia',
//     time: 'dnf'
//   }
// ]


// raceObj = [
//   {
//     name: 'Samuel',
//     time: 'dnf'
//   },
//   {
//     name: 'Fred',
//     time: 'dnf'
//   },
//   {
//     name: 'Cynthia',
//     time: '05:12:53'
//   }
// ]

// raceObj = [
//   {
//     name: 'Samuel',
//     time: 'dnf'
//   },
//   {
//     name: 'Fred',
//     time: 'dnf'
//   },
//   {
//     name: 'Cynthia',
//     time: 'dnf'
//   }
// ]

// console.log(raceWinner(raceObj))




function ticTacToe(str) {
  let board = new Array(9).fill(null);

  const possibleWins = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
  ]
  
  let result = [0, 0];
  const newStr = str.split('\n').join('');

  for (let i = 0; i < newStr.length; i++) {
    if (newStr[i] !== ' ') {
      board[i] = newStr[i]
    }
  }

  for (let win of possibleWins) {

    let player = board[win[0]];

    if (player === null && board[win[1]] === null && board[win[2]] === null) {
      continue;
    }

    if (player === null && board[win[1]] === null || player === null &&
        board[win[2]] === null) {
      continue;
    }

    if (player === board[win[1]] && player === board[win[2]]) {
      return [0, 0];
    }

    if (player === null || board[win[1]] === null || board[win[2]] === null) {
      if (player !== null) {
        if (player === board[win[1]] || player === board[win[2]]) {
          player === 'X' ? result[0] += 1 : result[1] += 1;
          // console.log(result, 'result at', win)
        }
      }
      if (player === null) {
        player = board[win[1]];
        if (player === board[win[0]] || player === board[win[2]]) {
          player === 'X' ? result[0] += 1 : result[1] += 1;
          // console.log(result, 'result at', win)
        }
      }
    }
  }
  return result;
}


// TEST CASES
// const str = "X X\n OO\nXOO"
// const str = "XXX\n OO\nXOO"
// const str = "X X\n OO\nXOO"
// const str = "XX \n OO\n "

// console.log(ticTacToe(str))
import Tile from './Tile';

const BOARD_DATA = [
  ['_1A', '_1B', '_1C', '_1D', '_1E', '_1F', '_1G', '_1H'],
  ['_2A', '_2B', '_2C', '_2D', '_2E', '_2F', '_2G', '_2H'],
  ['_3A', '_3B', '_3C', '_3D', '_3E', '_3F', '_3G', '_3H'],
  ['_4A', '_4B', '_4C', '_4D', '_4E', '_4F', '_4G', '_4H'],
  ['_5A', '_5B', '_5C', '_5D', '_5E', '_5F', '_5G', '_5H'],
  ['_6A', '_6B', '_6C', '_6D', '_6E', '_6F', '_6G', '_6H'],
  ['_7A', '_7B', '_7C', '_7D', '_7E', '_7F', '_7G', '_7H'],
  ['_8A', '_8B', '_8C', '_8D', '_8E', '_8F', '_8G', '_8H'],
];

const BOARD_Y = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', ''];
const BOARD_X = [1, 2, 3, 4, 5, 6, 7, 8];

const Board = (props) => {
  const handleClick = ({ i, j }) => {
    console.log({ i, j });
  };

  return (
    <div className='board'>
      {[...BOARD_DATA, BOARD_X].map((row, i) => (
        <div className='board-col'>
          {row.reduce((acc, curr, j, _row) => {
            let _cols = [];
            let tileProps = {
              onClick:
                i === BOARD_DATA.length
                  ? undefined
                  : () => handleClick({ i, j }),
              coordinate: i === BOARD_DATA.length,
              piece: curr,
            };
            if (j === 0) _cols.push(<Tile piece={BOARD_Y[i]} coordinate />);

            _cols.push(<Tile {...tileProps} />);
            return (acc = [...acc, ..._cols]);
          }, [])}
        </div>
      ))}
    </div>
  );
};

export default Board;

Board.prototype = {};

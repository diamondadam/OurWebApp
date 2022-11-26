import PropTypes from 'prop-types';
import classNames from 'classnames';

const Tile = (props) => {
  const { piece, tileColor, coordinate, onClick } = props;
  return (
    <div
      className={classNames('tile', tileColor, coordinate && 'coordintate')}
      onClick={() => onClick()}
    >
      {piece}
    </div>
  );
};

export default Tile;

Tile.prototype = {
  piece: PropTypes.string,
  tileColor: PropTypes.string,
  coordinate: PropTypes.bool,
  onClick: PropTypes.func,
};

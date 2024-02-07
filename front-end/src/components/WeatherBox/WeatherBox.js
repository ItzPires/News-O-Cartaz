const WeatherBox = ({ index, temp, onClick }) => {
    return (
        <article key={index} className="brick entry format-standard" onClick={onClick}>
            <div className="entry__text" style={{ borderRadius: '10px 10px 10px 10px' }}>
                <div className="entry__header">
                    <img src={process.env.PUBLIC_URL + '/weather/' + temp.tempInfo.idWeatherType + '.svg'} alt="weather" />
                    <h1 className="entry__title">{temp.day}</h1>
                </div>
                <div className="entry__excerpt">
                    <h2>{temp.tempInfo.tMax}º</h2>
                    <h4>{temp.tempInfo.tMin}º</h4>
                </div>
            </div>
        </article>
    );
}

export default WeatherBox;
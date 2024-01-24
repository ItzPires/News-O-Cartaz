import React, { useState, useEffect } from 'react';

const Weather = () => {
    const [cityList, setCityList] = useState([]);
    const [selectedCity, setSelectedCity] = useState({
        "globalIdLocal": 1110600,
        "name": "Lisboa"
    });
    const [tempInfoList, setTempInfoList] = useState([]);
    const [tempInfo, setTempInfo] = useState([]);

    const handleCityChange = (event) => {
        setSelectedCity(event.target.value);
    }

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(process.env.PUBLIC_URL + '/json/citys.json');
                const data = await response.json();
                setCityList(data);
            } catch (error) {
                console.error('Erro ao buscar dados:', error);
            }
        };

        const fetchTempInfo = async () => {
            try {
                const response = await fetch('http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/hp-daily-forecast-day0.json');
                const data = await response.json();
                setTempInfoList(data);
                getTempInfo(data);
            } catch (error) {
                console.error('Erro ao buscar dados:', error);
            }
        };

        const getTempInfo = (tempInfoList) => {
            const tempInfo = tempInfoList.data.filter((temp) => temp.globalIdLocal === selectedCity.globalIdLocal);
            setTempInfo(tempInfo);
        }

        fetchData();
        fetchTempInfo();
    }, [])

    //<span dangerouslySetInnerHTML={{ __html: temp[4] }} />

    return (
        <>
            <section className="s-bricks">

                <div className="masonry">
                    <h2>Tempo - {selectedCity.name}</h2>
                    <div className="entry__excerpt">
                        <form name="city" action="/tempo">

                            <select name="cidade" value={selectedCity} onChange={handleCityChange}>
                                {cityList.map((city) => (
                                    <option key={city.name} value={city.name}>
                                        {city.name}
                                    </option>
                                ))}
                            </select>
                        </form>
                    </div>
                    <div className="bricks-wrapper h-group">

                        <div className="grid-sizer"></div>
                        {tempInfo.map((temp, index) => (
                            <article key={index} className="brick entry format-standard">
                                <div className="entry__text" style={{ borderRadius: '10px 10px 10px 10px' }}>
                                    <div className="entry__header">
                                        

                                        <h1 className="entry__title">{temp[5]}</h1>
                                    </div>
                                    <div className="entry__excerpt">
                                        <h2>{temp.tMax}º</h2>
                                        <h4>{temp.tMin}º</h4>
                                    </div>
                                </div>
                            </article>
                        ))}

                    </div>

                </div>

            </section>

            <a target="_blank" href="https://www.ipma.pt/">
                <p>Fonte: IPMA</p>
            </a>
        </>
    );
};

export default Weather;
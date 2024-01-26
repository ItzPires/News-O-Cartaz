import React, { useState, useEffect } from 'react';
import WeatherBox from '../../components/WeatherBox/WeatherBox';

const Weather = () => {
    const [cityList, setCityList] = useState([]);
    const [selectedCity, setSelectedCity] = useState({
        "globalIdLocal": 1110600,
        "name": "Lisboa"
    });
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

        const fetchTempInfo = async (day) => {
            try {
                const response = await fetch('http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/hp-daily-forecast-day' + day + '.json');
                const data = await response.json();
                const tempInfo = getTempInfo(data);
                const dayName = getDayName(day);
                return { day: dayName, tempInfo: tempInfo };
            } catch (error) {
                console.error('Erro ao buscar dados:', error);
                throw error;
            }
        };

        const getDayName = (day) => {
            if (day === 0) {
                return 'Hoje';
            } else if (day === 1) {
                return 'Amanhã';
            } else {
                return 'Depois de Amanhã';
            }
        }

        const getTempInfoForThreeDays = async () => {
            try {
                let auxTempInfo = [];
                for (let i = 0; i < 3; i++) {
                    auxTempInfo.push(fetchTempInfo(i));
                }
                const resolvedTempInfoList = await Promise.all(auxTempInfo);
                setTempInfo(resolvedTempInfoList);
            } catch (error) {
                console.error('Erro ao buscar dados:', error);
                throw error;
            }
        }

        const getTempInfo = (tempInfoList) => {
            const tempInfo = tempInfoList.data.filter((temp) => temp.globalIdLocal === selectedCity.globalIdLocal);
            return tempInfo[0];
        }

        fetchData();
        getTempInfoForThreeDays();
    }, [])

    //<span dangerouslySetInnerHTML={{ __html: temp[4] }} />

    return (
        <>
            <section className="s-bricks">

                <div className="masonry">
                    <h2 className="keywords">Tempo - {selectedCity.name}</h2>
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

                        {tempInfo.map((temp, index) => (
                            <WeatherBox key={index} index={index} temp={temp} />
                        ))}

                    </div>

                </div>

            </section>

            <p className="keywords">Dados fornecidos pelo <a target="_blank" href="https://www.ipma.pt/">IPMA</a></p>
        </>
    );
};

export default Weather;
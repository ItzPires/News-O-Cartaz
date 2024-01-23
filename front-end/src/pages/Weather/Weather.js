import React, { useState, useEffect } from 'react';

const Weather = () => {
    const [cityList, setCityList] = useState([{ 'name': 'Lisboa' }, { 'name': 'Porto' }, { 'name': 'Faro' }, { 'name': 'Évora' }, { 'name': 'Beja' }, { 'name': 'Braga' }, { 'name': 'Bragança' }, { 'name': 'Castelo Branco' }, { 'name': 'Coimbra' }, { 'name': 'Guarda' }, { 'name': 'Leiria' }, { 'name': 'Portalegre' }, { 'name': 'Santarém' }, { 'name': 'Setúbal' }, { 'name': 'Viana do Castelo' }, { 'name': 'Vila Real' }, { 'name': 'Viseu' }]);
    const [selectedCity, setSelectedCity] = useState('Lisboa');
    const [tempInfoList, setTempInfoList] = useState([]);

    const handleCityChange = (event) => {
        setSelectedCity(event.target.value);
    }

    return (
        <>
            <section class="s-bricks">

                <div class="masonry">
                    <h2>Tempo - {selectedCity}</h2>
                    <div class="entry__excerpt">
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
                    <div class="bricks-wrapper h-group">

                        <div class="grid-sizer"></div>
                        {tempInfoList.map((tempInfo, index) => (
                            <article key={index} className="brick entry format-standard animate-this">
                                <div className="entry__text" style={{ borderRadius: '10px 10px 10px 10px' }}>
                                    <div className="entry__header">
                                        <span dangerouslySetInnerHTML={{ __html: tempInfo[4] }} />

                                        <h1 className="entry__title">{tempInfo[5]}</h1>
                                    </div>
                                    <div className="entry__excerpt">
                                        <h2>{tempInfo[1]}º</h2>
                                        <h4>{tempInfo[2]}º</h4>
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
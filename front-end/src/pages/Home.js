import React, { useEffect, useState } from "react";
import Masonry, { ResponsiveMasonry } from "react-responsive-masonry"
import { useNavigate } from "react-router-dom";
import Article from "../components/Article/Article";
import WeatherBox from "../components/WeatherBox/WeatherBox";
import SliderNews from "../components/SliderNews/SliderNews";
import APIService from "../services/APIService";

const Home = () => {
    const [allData, setAllData] = useState([]);
    const [weatherIndex, setWeatherIndex] = useState(-1);

    const navigate = useNavigate();

    const getNews = async () => {
        APIService.getNews().then((data) => {
            setAllData(data);
            putAdd(data);
        });
    };

    const putAdd = (news) => {
        APIService.getWeatherToday().then((data) => {
            let weather = { day: "Hoje", tempInfo: data };

            let randomIndex = Math.floor(Math.random() * news.length);
            setWeatherIndex(randomIndex);
            setAllData((prev) => {
                let newArray = [...prev];
                newArray.splice(randomIndex, 0, weather);
                return newArray;
            });
        });
    };

    useEffect(() => {
        getNews();
    }, []);

    return (
        <section className="s-bricks">
            <h2 className="keywords">Destaques</h2>
            <div className="bricks-wrapper">
                <ResponsiveMasonry
                    columnsCountBreakPoints={{ 350: 1, 750: 2, 900: 3 }}>
                    <Masonry>
                        {allData.length > 0 && weatherIndex !== -1 && (
                            allData.map((data, index) => {
                                if (index !== weatherIndex) {
                                    return <Article key={index} news={data} index={index} />
                                } else {
                                    return <WeatherBox key={index} index={index} temp={data} onClick={() => navigate("/tempo")} ></WeatherBox>
                                }
                            })
                        )}
                    </Masonry>
                </ResponsiveMasonry>
            </div>
        </section>
    );
};

export default Home;
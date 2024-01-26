import React, { useEffect, useState } from "react";
import Article from "../components/Article/Article";
import SliderNews from "../components/SliderNews/SliderNews";
import APIService from "../services/APIService";
const Home = () => {
    const [newsAll, setNewsAll] = useState([]);

    const getNews = async () => {
        APIService.getNews().then((data) => {
            setNewsAll(data);
        });
    };

    useEffect(() => {
        getNews();
    }, []);

    /*<h2 style="text-align:center">{{ keyword }}</h2>*/
    return (
        <section className="s-bricks">

            <div className="masonry">
                <h2 className="keywords">Destaques</h2>
                <div className="bricks-wrapper h-group">

                    <div className="brick entry featured-grid">
                        <div className="entry__content">

                            <SliderNews newsAll={newsAll} />

                        </div>
                    </div>

                    {newsAll.map((news, index) => (
                        <Article news={news} index={index} />
                    ))}
                </div>
            </div>
        </section>
    );
};

export default Home;
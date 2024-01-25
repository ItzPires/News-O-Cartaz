import React, { useEffect, useState } from "react";
import Article from "../components/Article/Article";
import SliderNews from "../components/SliderNews/SliderNews";

const Home = () => {
    const [newsAll, setNewsAll] = useState([]);
    const [newsT, setNewsT] = useState([]);
    const [keyword, setKeyword] = useState("");


    const getNews = async () => {
        const response = await fetch(process.env.PUBLIC_URL + '/json/news.json');
        const data = await response.json();
        setNewsAll(data);
    };

    useEffect(() => {
        getNews();
    }, []);

    /*<h2 style="text-align:center">{{ keyword }}</h2>*/
    return (
        <section className="s-bricks">

            <div className="masonry">
                <h2>Home</h2>
                <div className="bricks-wrapper h-group">

                    <div className="grid-sizer"></div>

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
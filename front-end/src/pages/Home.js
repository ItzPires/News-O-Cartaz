import React, { useEffect, useState } from "react";
import Masonry, { ResponsiveMasonry } from "react-responsive-masonry"
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
            <h2 className="keywords">Destaques</h2>
            <div className="bricks-wrapper">
                <ResponsiveMasonry
                    columnsCountBreakPoints={{ 350: 1, 750: 2, 900: 3 }}>
                    <Masonry>
                        {newsAll.map((news, index) => (
                            <Article news={news} index={index} />
                        ))}
                    </Masonry>
                </ResponsiveMasonry>
            </div>
        </section>
    );
};

export default Home;
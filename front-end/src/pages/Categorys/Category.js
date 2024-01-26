import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Article from "../../components/Article/Article";

const Category = () => {
    const { category } = useParams();
    const [newsCategory, setNews] = useState([]);

    useEffect(() => {
        const getNews = async () => {
            const response = await fetch(process.env.PUBLIC_URL + '/json/news.json');
            const data = await response.json();
            const filteredData = data.filter((item) => item.category === category);
            setNews(filteredData);
        };
        getNews();
    }, [category]);

    return (
        <section className="s-bricks">

            <div className="masonry">
                <h2>{ category }</h2>
                <div className="bricks-wrapper h-group">

                    <div className="grid-sizer"></div>

                    {newsCategory.map((news, index) => (
                        <Article news={news} index={index} />
                    ))}
                </div>
            </div>
        </section>
    );
}

export default Category;
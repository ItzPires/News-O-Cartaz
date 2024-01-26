import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Article from "../../components/Article/Article";

const Category = ({ CategoryName, source = false, latest = false }) => {
    const { id } = useParams();
    const [newsCategory, setNews] = useState([]);
    const category = CategoryName || id;
    debugger;

    useEffect(() => {
        const filterNews = (news) => {
            return news.filter(news => {
                if (source) {
                    return news.site === category;
                }
                if (latest) {
                    return news.latest === true;
                }
                return news.category === category;
            });
        };


        const getNews = async () => {
            const response = await fetch(process.env.PUBLIC_URL + '/json/news.json');
            const data = await response.json();
            setNews(filterNews(data));
        };

        getNews();
    }, [category]);

    return (
        <section className="s-bricks">

            <div className="masonry">
                <h2>{category}</h2>
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
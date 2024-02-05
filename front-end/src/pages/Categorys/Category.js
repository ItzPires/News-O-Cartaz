import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Masonry, { ResponsiveMasonry } from "react-responsive-masonry"
import Article from "../../components/Article/Article";
import APIService from "../../services/APIService";

const Category = ({ CategoryName, source = false, latest = false, search = false }) => {
    const { id } = useParams();
    const [newsCategory, setNews] = useState([]);
    const category = CategoryName || id;

    useEffect(() => {
        const filterNews = (news) => {
            return news.filter(news => {
                if (source) {
                    return news.site === category;
                }
                if (latest) {
                    return news.latest === true;
                }
                if (search) {
                    return news.title.toLowerCase().includes(id.toLowerCase()) || news.description.toLowerCase().includes(id.toLowerCase()) || news.category.toLowerCase().includes(id.toLowerCase()) || news.site.toLowerCase().includes(id.toLowerCase());
                }
                return news.category === category;
            });
        };


        const getNews = async () => {
            APIService.getNews().then((data) => {
                setNews(filterNews(data));
            });
        };

        getNews();
    }, [category]);

    return (
        <section className="s-bricks">

            <div className="masonry">
                <h2 className="keywords">{category}</h2>
                <div className="bricks-wrapper">
                    <ResponsiveMasonry
                        columnsCountBreakPoints={{ 350: 1, 750: 2, 900: 3 }}>
                        <Masonry>
                            {newsCategory.map((news, index) => (
                                <Article news={news} index={index} />
                            ))}
                        </Masonry>
                    </ResponsiveMasonry>
                </div>
            </div>
        </section>
    );
}

export default Category;
import React, { useEffect, useState } from "react";
import Article from "../components/Article/Article";

const Home = () => {
    const [newsAll, setNewsAll] = useState([]);
    const [newsT, setNewsT] = useState([]);
    const [keyword, setKeyword] = useState("");


    const getNews = () => {
        let a = ["Sic", "https://www.sic.pt/Programas/jornal-da-noite/videos/2021-05-17-Jornal-da-Noite---17-de-maio-de-2021", "https://media-manager.noticiasaominuto.com/640/naom_659d31a27b948.jpg", "Jornal da Noite - 17 de maio de 2021", "Jornal Apresentado por Rodrigo Guedes de Carvalho"];

        let b = ["Sic", "https://www.sic.pt/Programas/jornal-da-noite/videos/2021-05-17-Jornal-da-Noite---17-de-maio-de-2021", "https://media-manager.noticiasaominuto.com/640/naom_659d31a27b948.jpg", "Jornal da Noite - 17 de maio de 2021", "Jornal Apresentado por Rodrigo Guedes de Carvalho"];

        setNewsAll([a, b]);
        //setNewsT([a, b]);
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

                            <div className="featured-post-slider flexslider">

                                {newsT.map((news, index) => (
                                    <div className="featured-post-slide" key={index}>
                                        <div className="f-slide">

                                            <div className="f-slide__background"></div>
                                            <div className="f-slide__overlay"></div>

                                            <div className="f-slide__content">
                                                <ul className="f-slide__meta">
                                                    <li key={news[0]}>
                                                        <a href={`/source/${news[0]}`}>{news[0]}</a>
                                                    </li>
                                                </ul>

                                                <h1 className="f-slide__title">
                                                    <a target="_blank" href={news[1]} title="">
                                                        {news[3]}
                                                    </a>
                                                </h1>
                                            </div>
                                        </div>
                                    </div>
                                ))}
                            </div>

                            <div className="featured-post-nav">
                                <button className="featured-post-nav__prev">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12.707 17.293L8.414 13H18v-2H8.414l4.293-4.293-1.414-1.414L4.586 12l6.707 6.707z"></path></svg>
                                </button>
                                <button className="featured-post-nav__next">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M11.293 17.293l1.414 1.414L19.414 12l-6.707-6.707-1.414 1.414L15.586 11H6v2h9.586z"></path></svg>
                                </button>
                            </div>

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
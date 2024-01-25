import React from "react";
import ArticleScroll from "../ArticleScroll/ArticleScroll";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

const SliderNews = ({ newsAll }) => {
    const settings = {
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
    };

    const nextSlide = () => {
        slider.slickNext();
    };

    const prevSlide = () => {
        slider.slickPrev();
    };

    let slider;

    return (
        <>
            <div className="featured-post-slider flexslider">
                <Slider ref={(c) => (slider = c)} {...settings}>
                    {newsAll.map((news, index) => (
                        <div key={index}>
                            <ArticleScroll news={news} index={index} />
                        </div>
                    ))}
                </Slider>
            </div>

            <div className="featured-post-nav">
                <button onClick={prevSlide} className="featured-post-nav__prev">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12.707 17.293L8.414 13H18v-2H8.414l4.293-4.293-1.414-1.414L4.586 12l6.707 6.707z"></path></svg>
                </button>
                <button onClick={nextSlide} className="featured-post-nav__next">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M11.293 17.293l1.414 1.414L19.414 12l-6.707-6.707-1.414 1.414L15.586 11H6v2h9.586z"></path></svg>
                </button>
            </div>
        </>
    );
}

export default SliderNews;
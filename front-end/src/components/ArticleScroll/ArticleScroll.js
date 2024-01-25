import React from 'react';

const ArticleScroll = ({ news, index }) => {
  return (
    <div className="featured-post-slide" key={index}>
      <div className="f-slide">

        <div
          className="f-slide__background"
          style={{ backgroundImage: `url(${news.url_image})` }}>
        </div>
        <div className="f-slide__overlay"></div>

        <div className="f-slide__content">
          <ul className="f-slide__meta">
            <li key={news.url}>
              <a href={`/source/${news.site}`}>{news.site}</a>
            </li>
          </ul>

          <h1 className="f-slide__title">
            <a target="_blank" href={news.url} title="">
              {news.title}
            </a>
          </h1>
        </div>
      </div>
    </div>
  );
};

export default ArticleScroll;

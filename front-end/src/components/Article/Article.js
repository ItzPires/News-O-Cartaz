import React from 'react';

const Article = ({ news, index }) => {
  return (
    <article className="brick entry format-standard" key={index}>

      <div className="entry__thumb">
        <a target="_blank" href={news.url} className="thumb-link">
          <img src={news.url_image} alt="" />
        </a>
      </div>

      <div className="entry__text">
        <div className="entry__header">

          <div className="entry__meta">
            <div className="col">
              <span className="entry__cat-links">
                <a href={`/source/${news.site}`}>{news.site}</a>
              </span>
            </div>
            <div className="col">
              <img src={process.env.PUBLIC_URL + '/icons/RelatedContent.svg'} alt="Related Content" />
            </div>
          </div>

          <h1 className="entry__title">
            <a target="_blank" href={news.url}>
              {news.title}
            </a>
          </h1>
        </div>

        <div className="entry__excerpt">
          <p>
            {news.description}
          </p>
        </div>
      </div>

    </article>
  );
};

export default Article;

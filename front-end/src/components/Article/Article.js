import React from 'react';

const Article = ({ news, index }) => {
  return (
    <article className="brick entry format-standard" key={index}>

      <div className="entry__thumb">
        <a target="_blank" href={news[1]} className="thumb-link">
          <img src={news[2]} alt="" />
        </a>
      </div>

      <div className="entry__text">
        <div className="entry__header">

          <div className="entry__meta">
            <span className="entry__cat-links">
              <a href={`/source/${news[0]}`}>{news[0]}</a>
            </span>
          </div>

          <h1 className="entry__title">
            <a target="_blank" href={news[1]}>
              {news[3]}
            </a>
          </h1>
        </div>

        <div className="entry__excerpt">
          <p>
            {news[4]}
          </p>
        </div>
      </div>

    </article>
  );
};

export default Article;

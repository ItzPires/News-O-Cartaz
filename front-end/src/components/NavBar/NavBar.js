import React, { useState } from 'react';
import './NavBar.css';

const NavBar = () => {
    const [searchValue, setSearchValue] = useState('');

    const handleSearchChange = (event) => {
      setSearchValue(event.target.value);
    };
  
    const handleSubmit = (event) => {
      event.preventDefault();
    };

    return (
        <header className="s-header">

            <div className="row s-header__content">

                <div className="s-header__logo">
                    <h2>O Cartaz</h2>
                </div>

                <nav className="s-header__nav-wrap">

                    <h2 className="s-header__nav-heading h6">Menu</h2>

                    <ul className="s-header__nav">
                        <li><a href="/" title="">Destaques</a></li>
                        <li><a href="/ultimas" title="">Últimas</a></li>
                        <li><a href="/categoria/País">País</a></li>
                        <li><a href="/categoria/Economia">Economia</a></li>
                        <li><a href="/categoria/Cultura">Cultura</a></li>
                        <li><a href="/categoria/Desporto">Desporto</a></li>
                        <li><a href="/locais">Locais</a></li>
                        <li><a href="/tempo" title="">Tempo</a></li>
                        <li className="has-children">
                            <a href="/categoria/Outros" title="">Outros</a>
                            <ul className="sub-menu">
                                <li><a href="/categoria/Mundo">Mundo</a></li>
                                <li><a href="/categoria/Tecnologia">Tecnologia</a></li>
                                <li><a href="/categoria/Outros" title="">Outros</a></li>
                            </ul>
                        </li>
                    </ul>

                    <a href="#0" title="Close Menu" className="s-header__overlay-close close-mobile-menu">Fechar</a>

                </nav>

                <a className="s-header__toggle-menu" href="#0" title="Menu"><span>Menu</span></a>

                <div className="s-header__search">
                    <form
                        role="search"
                        method="get"
                        className="s-header__search-form"
                        action="#"
                        onSubmit={handleSubmit}
                    >
                        <label>
                            <input
                                type="search"
                                className="s-header__search-field"
                                placeholder="O Que Procura?"
                                value={searchValue}
                                onChange={handleSearchChange}
                                name="search"
                                title="O Que Procura?"
                                autoComplete="off"
                            />
                        </label>
                        <input type="submit" className="s-header__search-submit" value="Search" />
                    </form>

                    <a href="#0" title="Close Search" className="s-header__overlay-close">
                        Fechar
                    </a>
                </div>

                <a className="s-header__search-trigger" href="#">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M10 18a7.952 7.952 0 004.897-1.688l4.396 4.396 1.414-1.414-4.396-4.396A7.952 7.952 0 0018 10c0-4.411-3.589-8-8-8s-8 3.589-8 8 3.589 8 8 8zm0-14c3.309 0 6 2.691 6 6s-2.691 6-6 6-6-2.691-6-6 2.691-6 6-6z"></path></svg>
                </a>

            </div>

        </header>
    )
}
export default NavBar;
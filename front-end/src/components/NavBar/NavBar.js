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
                        <li><a href="/tempo" title="">Tempo</a></li>
                        <li><a href="/categoria/Mundo">Mundo</a></li>
                        <li><a href="/categoria/Tecnologia">Tecnologia</a></li>
                    </ul>

                    <a href="#0" title="Close Menu" className="s-header__overlay-close close-mobile-menu">Fechar</a>

                </nav>

                <a className="s-header__toggle-menu" href="#0" title="Menu"><span>Menu</span></a>

            </div>

        </header>
    )
}
export default NavBar;
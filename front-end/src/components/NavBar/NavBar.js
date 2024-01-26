import React, { useEffect, useState } from 'react';
import './NavBar.css';

const NavBar = () => {
    const [searchValue, setSearchValue] = useState('');

    const handleSearchChange = (event) => {
        setSearchValue(event.target.value);
    };
  
    const handleSubmit = (event) => {
        event.preventDefault();
        window.location.href = `/pesquisa/${searchValue}`;
    };

    useEffect(() => {
        // Menu Mobile
        const toggleMenu = document.querySelector('.s-header__toggle-menu');
        const closeNavWrap = document.querySelector('.s-header__overlay-close');
        const siteBody = document.body;
    
        const openMenu = (e) => {
            e.preventDefault();
            e.stopPropagation();
            siteBody.classList.add('nav-wrap-is-visible');
        };
    
        const closeMenu = (e) => {
            e.preventDefault();
            e.stopPropagation();
            if (siteBody.classList.contains('nav-wrap-is-visible')) {
                siteBody.classList.remove('nav-wrap-is-visible');
            }
        };
    
        toggleMenu.addEventListener('click', openMenu);
        closeNavWrap.addEventListener('click', closeMenu);
    
        const handleSubMenuClick = (e) => {
            e.preventDefault();
    
            const currentLink = e.target;
            const siblings = currentLink.parentElement.parentElement.children;
            const submenu = currentLink.nextElementSibling;
    
            if (submenu && window.getComputedStyle(submenu).display !== 'none') {
                submenu.style.display = 'none';
                currentLink.classList.remove('sub-menu-is-open');
            } else {
                if (submenu) {
                    submenu.style.display = 'block';
                    currentLink.classList.add('sub-menu-is-open');
                }
                for (const sibling of siblings) {
                    if (sibling !== currentLink.parentElement) {
                        const siblingSubmenu = sibling.querySelector('ul');
                        if (siblingSubmenu) {
                            siblingSubmenu.style.display = 'none';
                            sibling.querySelector('a').classList.remove('sub-menu-is-open');
                        }
                    }
                }
            }
        };
    
        const subMenuLinks = document.querySelectorAll('.s-header__nav .has-children > a');
        subMenuLinks.forEach(link => link.addEventListener('click', handleSubMenuClick));
    
        // Search Menu
        const searchWrap = document.querySelector('.s-header__search');
        const searchTrigger = document.querySelector('.s-header__search-trigger');
        const searchField = searchWrap.querySelector('.s-header__search-field');
        const closeSearch = searchWrap.querySelector('.s-header__overlay-close');
    
        if (!(searchWrap && searchTrigger)) return;
    
        const openSearch = (e) => {
            e.preventDefault();
            e.stopPropagation();
    
            siteBody.classList.add('search-is-visible');
            setTimeout(() => {
                searchWrap.querySelector('.s-header__search-field').focus();
            }, 100);
        };
    
        const closeSearchHandler = (e) => {
            e.stopPropagation();
    
            if (siteBody.classList.contains('search-is-visible')) {
                siteBody.classList.remove('search-is-visible');
                setTimeout(() => {
                    searchWrap.querySelector('.s-header__search-field').blur();
                }, 100);
            }
        };
    
        const searchWrapHandler = (e) => {
            if (!e.target.matches('.s-header__search-field')) {
                closeSearch.dispatchEvent(new Event('click'));
            }
        };
    
        const searchFieldHandler = (e) => {
            e.stopPropagation();
        };
    
        searchTrigger.addEventListener('click', openSearch);
        closeSearch.addEventListener('click', closeSearchHandler);
        searchWrap.addEventListener('click', searchWrapHandler);
        searchField.addEventListener('click', searchFieldHandler);
    
        searchField.setAttribute('placeholder', 'O Que Procura?');
        searchField.setAttribute('autocomplete', 'off');
    
        return () => {
            searchTrigger.removeEventListener('click', openSearch);
            closeSearch.removeEventListener('click', closeSearchHandler);
            searchWrap.removeEventListener('click', searchWrapHandler);
            searchField.removeEventListener('click', searchFieldHandler);
            toggleMenu.removeEventListener('click', openMenu);
            closeNavWrap.removeEventListener('click', closeMenu);
            subMenuLinks.forEach(link => link.removeEventListener('click', handleSubMenuClick));
        };
    }, []);
    

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
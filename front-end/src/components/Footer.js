const Footer = () => {
    return (
        <footer className="s-footer">

            <div className="s-footer__main">

                <div className="row">

                    <div className="column large-4 medium-6 tab-12 s-footer__info">

                        <h5>ocartaz.pt</h5>

                        <p>
                            Olhaaaa notícia quentinha e fresquinha, acabadinha de sair das redaçõessss!!!
                        </p>


                    </div>

                    <div className="column large-2 medium-3 tab-6 s-footer__site-links">

                        <h5>Categorias</h5>

                        <ul>
                            <li><a href="/categoria/Covid">Covid-19</a></li>
                            <li><a href="/categoria/País">País</a></li>
                            <li><a href="/categoria/Economia">Economia</a></li>
                            <li><a href="/categoria/Cultura">Cultura</a></li>
                            <li><a href="/categoria/Desporto">Desporto</a></li>
                            <li><a href="/locais">Locais</a></li>
                            <li><a href="/categoria/Mundo">Mundo</a></li>
                            <li><a href="/categoria/Tecnologia">Tecnologia</a></li>
                        </ul>

                    </div>

                    <div className="column large-2 medium-3 tab-6 s-footer__social-links">

                        <h5>Ajuda?</h5>

                        <ul>
                            <li><a href="/about">Sobre Nós</a></li>
                            <li><a href="/faq">FAQ</a></li>
                            <li><a href="/contacto">Contacto</a></li>
                            <li><a href="/fontes">Fontes</a></li>
                        </ul>

                    </div>

                    <div className="column large-4 medium-12 s-footer__subscribe">

                        <h5>Siga-nos</h5>

                        <p>As nossas Redes Socias ainda não estão prontas. Fique atento!</p>
                        <p>Brevemente poderá subscrever o nosso Newsletter!</p>

                    </div>

                </div>

            </div>

            <div className="s-footer__bottom">
                <div className="row">
                    <div className="column">
                        <div className="ss-copyright">
                            <span>© Copyright ocartaz.pt 2021</span>
                        </div>
                    </div>
                </div>

                <div className="ss-go-top">
                    <a className="smoothscroll" title="Voltar ao Top" href="#top">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M6 4h12v2H6zm5 10v6h2v-6h5l-6-6-6 6z" /></svg>
                    </a>
                </div>
            </div>

        </footer>
    );
}

export default Footer;
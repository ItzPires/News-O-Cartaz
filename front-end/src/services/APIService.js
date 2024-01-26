const APIService = {
    getNews: async () => {
        const response = await fetch(process.env.PUBLIC_URL + '/json/news.json');
        return response.json();
    },
    getCityList: async () => {
        const response = await fetch(process.env.PUBLIC_URL + '/json/citys.json');
        return response.json();
    },
    getWeather: async (day) => {
        const response = await fetch('http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/hp-daily-forecast-day' + day + '.json');
        return response.json();
    },
}

export default APIService;
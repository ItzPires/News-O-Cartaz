const APIService = {
    globalIdDefault: 1110600,
    getNews: async () => {
        const response = await fetch(process.env.PUBLIC_URL + '/json/news.json');
        return response.json();
    },
    getCityList: async () => {
        const response = await fetch(process.env.PUBLIC_URL + '/json/citys.json');
        return response.json();
    },
    getWeather: async (day) => {
        const response = await fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/hp-daily-forecast-day' + day + '.json');
        return response.json();
    },
    getWeatherToday: async () => {
        let response = await fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/hp-daily-forecast-day0.json');
        let data = await response.json();
        return data.data.filter((temp) => temp.globalIdLocal === APIService.globalIdDefault)[0];
    },
}

export default APIService;
const APIService = {
    globalIdDefault: 1110600,
    getNews: async () => {
        let url;
        
        // Check if the app is running on localhost or on a server
        if (window.location.hostname === 'localhost') {
            url = 'http://127.0.0.1:8000/api/news/';
        } else {
            url = process.env.PUBLIC_URL + '/json/news.json';
        }
    
        const response = await fetch(url);
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
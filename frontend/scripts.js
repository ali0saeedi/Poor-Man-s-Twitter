var tweets = new Vue({
    el: '#app',
    data: {
        tweets: null,
        baseUrl: 'http://127.0.0.1:8000/api/v1/tweets/?sort-by=',
        tweetInputName: '',
        tweetInputMessage: '',
        sortBy: 'time-desc',
        maxLengthName: 20,
        maxLengthMessage: 50,
    },
    async mounted() {
        this.get_tweets();
    },
    methods: {
        async get_tweets() {
            const response = await fetch(this.baseUrl+this.sortBy, {
                method: 'GET',
                headers: { 'Content-Type': 'application/json' }
            });
            this.tweets = await response.json();
        },
        async post_tweet() {
            let _data = {
                name: this.tweetInputName,
                message: this.tweetInputMessage
              }
            this.tweetInputName = '';
            this.tweetInputMessage = '';
            await fetch(this.baseUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(_data)
            });
            await this.get_tweets();
        },
    }
});

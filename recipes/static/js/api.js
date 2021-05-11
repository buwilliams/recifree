const Api = {
    get(url) {
        return fetch(url)
            .then(response => response.json())
            .then(data => {
                return data;
            });
    },
    post(url, data) {
        return fetch(url, {
            method: 'POST',
            mode: 'cors',
            cache: 'no-cache',
            credentials: 'same-origin',
            headers: { 'Content-Type': 'application/json' },
            redirect: 'follow',
            referrerPolicy: 'no-referrer',
            body: JSON.stringify(data)
        }).then((response) => {
            return response;
        })
    },
    delete(url) {
        return fetch(url, {
            method: 'DELETE',
            mode: 'cors',
            cache: 'no-cache',
            credentials: 'same-origin',
            headers: { 'Content-Type': 'application/json' },
            redirect: 'follow',
            referrerPolicy: 'no-referrer'
        }).then((response) => {
            return response;
        })

    }
}
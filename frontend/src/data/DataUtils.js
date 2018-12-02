

export function getMedicaments() {
  return ['medicament1', 'medicament2', 'medicament3', 'medicament4', 'medicament5'];
}


export function getAllergies() {
  return ['alergie1', 'alergie2', 'alergie3', 'alergie4', 'alergie5'];
}

const headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-Requested-With': 'XMLHttpRequest'
};

const url = 'http://127.0.0.1:5000';

export const  getJson = (relativeUrl) => {
    return fetch(`${url}/${relativeUrl}`, {
                          method: 'GET',
                          headers: headers,
                })
        .then(res => {
           console.log('================ Rezultat', res);
            return res.json();
        })
       .then(data => {
           console.log("data GET::: ", data);
           return data;

       });
}

export const post = (relativeUrl, data) => {
    return fetch(`${url}/${relativeUrl}`, {
		method: 'POST',
		headers: headers,
		body: JSON.stringify(data)
	})
	.then(res => {
		 return res.json()
	})
	.then(data => {
		console.log("dataPOOOOOOST:", data);
		return data;

	});
};
export const getData = () => {
    return fetch("http://127.0.0.1:8000/api/average").then((res) => res.json());
  };
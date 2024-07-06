class ApiService {
    constructor() {
      this.base_url = 'http://127.0.0.1:8000';
      this.headers_token = {};
    }
    async get_token(data) {
      const url = `${this.base_url}/token`;
      const credenciales = JSON.stringify(data);
  
      try {
        const response = await fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: credenciales,
        });
        return await response.json();
      } catch (error) {
        this.handleError(error);
      }
    }
  
    async get(end_point) {
      const url = `${this.base_url}/${end_point}/`;
  
      try {
        const response = await fetch(url, {
          method: 'GET',
          headers: this.headers_token,
        });
        return await response.json();
      } catch (error) {
        this.handleError(error);
      }
    }
  
    async post(end_point, data) {

      const url = `${this.base_url}/${end_point}/`;
      const datos = JSON.stringify(data);
  
      try {
        const response = await fetch(url, {
          method: 'POST',
          headers: this.headers_token,
          body: datos,
        });
        return await response.json();
      } catch (error) {
        this.handleError(error);
      }
    }
  
    async update(end_point, data, id) {
      const url = `${this.base_url}/${end_point}/${id}/`;
      const datos = JSON.stringify(data);
  
      try {
        const response = await fetch(url, {
          method: 'PATCH',
          headers: this.headers_token,
          body: datos,
        });
        return await response.json();
      } catch (error) {
        this.handleError(error);
      }
    }
  
    add_token(token) {
      this.headers_token = {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`,
      };
    }

    async session() {
      if (Object.keys(this.headers_token).length !== 0) {
          return true; // Indica que el usuario está autenticado
      } else {
          window.location.href = '/SaleMusic/templates/login.html';
          return false; // Indica que el usuario no está autenticado y ha sido redirigido
      }
  }
  
    LogOut() {
      this.usuario = '';  
      this.headers_token = {};
      localStorage.removeItem('token');
      window.location.href = '/SaleMusic/templates/login.html';
    }

    handleError(error) {
      console.error('API call failed:', error);
      return null;
    }
}

    // login() {
    //   document.getElementById('login-form').addEventListener('submit', async function(event) {
    //     event.preventDefault();
    //     const username = document.getElementById('username').value;
    //     const password = document.getElementById('password').value;
    
    //     const apiService = new ApiService();
    //     const data = { username: username, password: password };
    //     const response = await apiService.get_token(data);
    
    //     if (response && response.token) {
    //         apiService.add_token(response.token);
    //         // Redirigir a la página deseada
    //         window.location.href = '/tienda_musica_front/templates/home.html';
    //     } else {
    //         alert('Credenciales incorrectas. Inténtalo de nuevo.');
    //     }
    // })
    // }
  
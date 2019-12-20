<template>
  <div class="container">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">First</th>
          <th scope="col">Last</th>
          <th scope="col">Email</th>
          <th scope="col">Age</th>
          <th scope="col"></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items">
          <th scope="row">{{ item.id }}</th>
          <td>{{ item.first_name }}</td>
          <td>{{ item.last_name }}</td>
          <td>{{ item.email }}</td>
          <td>{{ item.gender }}</td>
          <td>
            <b-button v-b-modal.modal-1 @click="viewData(item)">Edit</b-button>
            <button class="btn btn-danger" @click="del(item)">Del</button>
          </td>
        </tr>
      </tbody>
    </table>
    <b-modal id="modal-1" title="Edit Profile" hide-footer>
      <form v-on:submit.prevent="save">
        <div class="form-group">
          <label for="exampleInputEmail1">Name</label>
          <input type="text" class="form-control" v-model="editItem.first_name" />
        </div>
        <div class="form-group">
          <label for="exampleInputPassword1">Last Name</label>
          <input type="text" class="form-control" v-model="editItem.last_name" />
        </div>
        <div class="form-group">
          <label for="exampleInputPassword1">Email</label>
          <input type="email" class="form-control" v-model="editItem.email" />
        </div>
        <div class="form-group">
          <label for="exampleInputPassword1">Gender</label>
          <input type="text" class="form-control" v-model="editItem.gender" />
        </div>
        <div class="form-group">
          <label for="exampleInputPassword1">Age</label>
          <input type="text" class="form-control" v-model="editItem.age" />
        </div>
        <button type="submit" class="btn btn-success">Save</button>
      </form>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      items: [],
      editItem: {
        first_name: "",
        last_name: "",
        email: "",
        gender: "",
        age: ""
      }
    };
  },
  created() {
    axios
      .get(`http://localhost:5002/employees`)
      .then(response => {
        // JSON responses are automatically parsed.
        this.items = response.data.data;
        console.log(response);
      })
      .catch(e => {
        this.errors.push(e);
      });
  },
  methods: {
    viewData(value) {
      this.editItem  = value
    },
    save(){
      axios
      .post(`http://localhost:5002/employeeUpdate`, this.editItem)
      .then(()=>{this.$bvModal.hide('modal-1')})
      .catch(e => {
        console.log(e)
      });
    }
    ,
    del(value){
      axios
      .delete(`http://localhost:5002/employeeDelete/`+value.id)
      .then(()=>{window.location.reload()})
      .catch(e => {
        console.log(e)
      });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

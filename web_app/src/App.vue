<template>
    <div id="wrapper">
      <nav class="navbar is-info" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
          <RouterLink class="navbar-item" to="/consumerdash"><b>Eat Healthily</b></RouterLink>
          <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>
        <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
          <div class="navbar-end">
            <RouterLink class="navbar-item" to="/consumerdash">Home</RouterLink>
            <RouterLink class="navbar-item" to="/login">Login</RouterLink>
            <RouterLink class="navbar-item" to="/signup">Signup</RouterLink> 
          </div>
        </div>
      </nav>
    </div>
  <RouterView />
</template>

<script>
export default{
  data (){
    return{
      showMobileMenu: false
    }
  }
}
</script>

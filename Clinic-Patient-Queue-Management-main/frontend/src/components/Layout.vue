<template>

<div class="layout">

<Sidebar />

<div class="main">

<Navbar />

<div class="content">

<router-view />

</div>

</div>

</div>

</template>

<script setup>

import Sidebar from "./Sidebar.vue";
import Navbar from "./Navbar.vue";

</script>

<style scoped>

.layout{

display:flex;

}
//
.main{

margin-left:240px;

width:100%;

}

.content{

padding:30px;

background:#f5f7fb;

min-height:calc(100vh - 70px);

}

</style>
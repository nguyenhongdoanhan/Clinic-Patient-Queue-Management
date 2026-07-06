<template>
  <div class="auth-page">
    <div class="row g-0 vh-100">

      <!-- Left Side -->
      <div class="col-lg-7 d-none d-lg-flex left-panel">

        <div class="overlay">

          <div class="content">

            <i class="bi bi-hospital display-1"></i>

            <h1 class="fw-bold mt-3">
              Clinic Patient Queue
            </h1>

            <p class="lead">
              Management System
            </p>

            <hr class="bg-light">

            <h5>
              Smart Clinic
            </h5>

            <p>
              Modern • Fast • Secure
            </p>

          </div>

        </div>

      </div>

      <!-- Right Side -->

      <div class="col-lg-5 d-flex justify-content-center align-items-center">

        <slot></slot>

      </div>

    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>

.auth-page{

    background:#f4f6f9;

}

.left-panel{

    background:linear-gradient(135deg,#0d6efd,#4f8dfd);

    color:white;

}

.overlay{

    width:100%;

    display:flex;

    justify-content:center;

    align-items:center;

}

.content{

    text-align:center;

    padding:40px;

}

hr{

    opacity:.3;

}

</style>
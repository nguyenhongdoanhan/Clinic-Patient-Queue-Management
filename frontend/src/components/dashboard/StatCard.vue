<template>

<div class="card shadow-sm stat-card">

    <div class="card-body d-flex justify-content-between align-items-center">

        <div>

            <h6 class="text-secondary">

                {{ title }}

            </h6>

            <h2 class="fw-bold mt-2">

                {{ value }}

            </h2>

        </div>

        <div
            class="icon"
            :style="{background:color}"
        >

            <i :class="icon"></i>

        </div>

    </div>

</div>

</template>

<script setup>

defineProps({

    title:String,

    value:Number,

    icon:String,

    color:String

})

</script>

<style scoped>

.stat-card{

    border:none;

    border-radius:18px;

    transition:.3s;

}

.stat-card:hover{

    transform:translateY(-5px);

}

.icon{

    width:70px;

    height:70px;

    border-radius:18px;

    display:flex;

    justify-content:center;

    align-items:center;

    color:white;

    font-size:30px;

}

</style>
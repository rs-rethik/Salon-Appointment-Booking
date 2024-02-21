<template>
  <h1 class="font-bold text-[25px] mb-5" style="color: #A020F0;">Book a salon appointment</h1>
  <!-- <hr class="mt-5"> -->
  <div class="flex">
    <div class="w-2/3">
      <div class="ml-11">
        <div>
          <h2 class="font-medium text-xl text-gray-900 mt-5 mb-2" >Select Date</h2>
          <VDatePicker 
          :style="{ width: '600px' }"  
          mode="date" 
          :color="SelectedColor" 
          v-model="bookingData.date"
          />
        </div>
        <div class="svg-container mt-1">
          <svg id='Globe_24' width='24' height='24' viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'><rect width='24' height='24' stroke='none' fill='#000000' opacity='0'/>
          <g transform="matrix(0.83 0 0 0.83 12 12)" >
          <g style="" >
          <g transform="matrix(1 0 0 1 0 0)" >
          <path style="stroke: rgb(0,0,0); stroke-width: 2; stroke-dasharray: none; stroke-linecap: butt; stroke-dashoffset: 0; stroke-linejoin: round; stroke-miterlimit: 10; fill: none; fill-rule: nonzero; opacity: 1;" transform=" translate(-12, -12)" d="M 12 3 C 7.029437251522859 3 3 7.029437251522859 3 12 C 3 16.970562748477143 7.029437251522859 21 12 21 C 16.970562748477143 21 21 16.970562748477143 21 12 C 21 7.029437251522859 16.970562748477143 3 12 3 Z" stroke-linecap="round" />
          </g>
          <g transform="matrix(1 0 0 1 -3.85 2.45)" >
          <path style="stroke: none; stroke-width: 1; stroke-dasharray: none; stroke-linecap: butt; stroke-dashoffset: 0; stroke-linejoin: miter; stroke-miterlimit: 4; fill: rgb(0,0,0); fill-rule: nonzero; opacity: 1;" transform=" translate(-8.15, -14.45)" d="M 12 16 L 11 16 L 11 14.6 C 11 14.334 10.895 14.08 10.707 13.892999999999999 L 4.707000000000001 7.892999999999999 L 3.293 9.307 L 9 15.014 L 9 16 C 9 17.103 9.897 18 11 18 L 11 21 L 13 21 L 13 17 C 13 16.447 12.552 16 12 16 z" stroke-linecap="round" />
          </g>
          <g transform="matrix(1 0 0 1 1.75 3.5)" >
          <path style="stroke: none; stroke-width: 1; stroke-dasharray: none; stroke-linecap: butt; stroke-dashoffset: 0; stroke-linejoin: miter; stroke-miterlimit: 4; fill: rgb(0,0,0); fill-rule: nonzero; opacity: 1;" transform=" translate(-13.75, -15.5)" d="M 17 15 L 16 15 L 16 13 C 16 12.447 15.552 12 15 12 L 8.508 12 L 8.508 14 L 14 14 L 14 16 C 14 16.553 14.448 17 15 17 L 17 17 L 17 19 L 19 19 L 19 17 C 19 15.897 18.103 15 17 15 z" stroke-linecap="round" />
          </g>
          <g transform="matrix(1 0 0 1 -1 -4.35)" >
          <path style="stroke: none; stroke-width: 1; stroke-dasharray: none; stroke-linecap: butt; stroke-dashoffset: 0; stroke-linejoin: miter; stroke-miterlimit: 4; fill: rgb(0,0,0); fill-rule: nonzero; opacity: 1;" transform=" translate(-11, -7.65)" d="M 13 3 L 13 5.008 L 9.992 5.031 C 9.443 5.035 9 5.482 9 6.031 L 9 8 L 8 8 C 7.448 8 7 8.447 7 9 L 7 12.297 L 9 12.297 L 9 10 L 10 10 C 10.552 10 11 9.553 11 9 L 11 7.023 L 13.015 7.007 C 14.109 7 15 6.103 15 5.008 L 15 3 L 13 3 z" stroke-linecap="round" />
          </g>
          <g transform="matrix(1 0 0 1 0 0.26)" >
          <path style="stroke: none; stroke-width: 1; stroke-dasharray: none; stroke-linecap: butt; stroke-dashoffset: 0; stroke-linejoin: miter; stroke-miterlimit: 4; fill: rgb(0,0,0); fill-rule: nonzero; opacity: 0.13;" transform=" translate(-12, -12.26)" d="M 15 3.523 L 15 5 C 15 6.105 14.105 7 13 7 L 11 7 L 11 9 C 11 9.552 10.552 10 10 10 L 9 10 L 9 12 L 14 12 C 14.552 12 15 12.448 15 13 L 15 16 L 16 16 C 17.105 16 18 16.895 18 18 L 18 18.695 C 19.837 17.047 21 14.661999999999999 21 12 C 21 8.083 18.493 4.76 15 3.523 z M 12 18 C 10.895 18 10 17.105 10 16 L 10 15 L 4 8 L 3.388 9.388 C 3.138 10.215 3 11.091 3 12 C 3 16.631999999999998 7.001 21 12 21 L 12 18 z" stroke-linecap="round" />
          </g>
          </g>
          </g>
          </svg>
          <span class="svg-text opacity-50">Timezone America/New York</span>
        </div>
        <div>
          <h2 class="font-medium text-xl text-gray-900 mt-5 mb-1">Name</h2>
          <Input class="h-8" :style="{ width: '600px'}" type="text" v-model="bookingData.name"/>
        </div>
        <div>
          <h2 class="font-medium text-xl text-gray-900 mt-5 mb-2">Service</h2>
          <select class="h-8 border-gray-400 form-input block" :style="{ width: '600px'}" v-model="bookingData.service"> 
            <option value="">Select Service</option>
            <option v-for="services of serviceData.data" :key="services" :value="services">{{ services.service }}</option>
          </select>
        </div>
        <div>
          <button 
          type="button" 
          class="focus:outline-none text-white bg-purple-400 hover:bg-purple-800 focus:ring-4 focus:ring-purple-300 font-medium rounded-sm text-sm px-5 py-2.5 mb-2 dark:bg-purple-600 dark:hover:bg-purple-700 mt-7 ml-52 w-56"
          @click="enterData()"
          >Book Now</button>
        </div>
      </div>
    </div>
    <div class="w-1/3">
      <div class="ml-1">
        <div>
          <h2 class="font-medium text-xl text-gray-900 mt-5 mb-2">Select preferred time</h2>
          <div class="grid grid-cols-2 gap-0">
            <div v-for="time in timeData.data" :key="time.start_time" class="w-1/2 mb-2">
              <Button   
              class="form-input p-6 w-48 border-gray-400"
              size="lg" 
              @click="setTime(time.start_time, time.end_time)"
              :class="{ 'bg-purple-500': bookingData.start_time === time.start_time, 'text-white': bookingData.start_time === time.start_time, 'cursor-not-allowed': isTimeBooked(bookingData.date, time.start_time) }"
              :disabled="isTimeBooked(bookingData.date, time.start_time)"
              >
              {{ formatTime(time.start_time) }} - {{ formatTime(time.end_time) }}
              </Button>          
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-if="showConfirmation" class="confirmation-overlay">
    <div class="confirmation-message">
      <p>Dear {{ bookingData.name }}, Thank you for booking!</p>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue';
import { createListResource } from 'frappe-ui';


// const date = ref(new Date());
const SelectedColor = ref('purple');

const serviceData = createListResource({
  doctype: 'Services',
  fields: ['service'],
  auto: true,
})

const timeData = createListResource({
  doctype: 'Time Slots',
  fields: ['start_time', 'end_time'],
  auto: true,
})


const formatDate = (date) => {
  return new Date(date).toISOString().substring(0, 10);
};

const bookingData = reactive({
  date: formatDate(new Date()),
  name: '',
  service: '',
  start_time: '',
  end_time: '',
})

const showConfirmation = ref(false);

const appointmentBooking = createListResource({
  doctype: "Appointments",
  fields: ["name1", "date", "service", "time"],
  auto: true,
  insert: {
    onSuccess () {
      console.log('Appointment booked')
      showConfirmation.value = true;

      setTimeout(() => {
        location.reload();
        showConfirmation.value = false;
      }, 1000);
    },
  },
});

const isTimeBooked = (date, time) => {
  const bookedAppointments = appointmentBooking.data || [];

  return bookedAppointments.some(appointment => {
    const storedDate = appointment.date.substring(0, 10);
    return (
      storedDate === formatDate(date) && 
      appointment.time === time
    );
  });
};

const formatTime = (time) => {
  const [hours, minutes] = time.split(':');
  const formattedHours = (hours % 12) || 12;
  const period = hours < 12 ? 'AM' : 'PM';
  return `${formattedHours}:${minutes} ${period}`;
};

function setTime(n,m) {
    bookingData.start_time = n;
    bookingData.end_time = m;
  }

function enterData() {
  if (!bookingData.name || !bookingData.date || !bookingData.start_time || !bookingData.service) {
    alert('Please fill in all the details');
    return;
  }
  const selectedDate = new Date(bookingData.date);
  const currentDate = new Date();
  currentDate.setHours(0, 0, 0, 0);
  if (selectedDate < currentDate) {
    alert('Please select the valid date');
    return;
  }

  appointmentBooking.insert.submit({
    name1: bookingData.name,
    date: formatDate(bookingData.date),
    time: bookingData.start_time,
    service: bookingData.service.service,
  });
}

</script>

<style scoped>
.bg-purple-500 {
  background-color: #A020F0;
}

.text-white {
  color: white;
}

.confirmation-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;
}

.confirmation-message {
  background: white;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
}

.svg-container {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.svg-text {
  margin-left: 4px;
  font-size: 16px;
}
</style>

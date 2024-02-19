<template>
  <h1 class="font-bold text-[25px]" style="color: blueviolet;">Book a salon appointment</h1>
  <hr class="mt-5">
  <div class="flex">
    <div class="w-2/3">
      <div class="ml-11">
        <div>
          <h2 class="font-medium text-xl text-gray-900 mt-5 mb-2" >Select Date</h2>
          <VDatePicker expanded mode="date" :color="SelectedColor" v-model="bookingData.date" required/>
        </div>
        <div>
          <h2 class="font-medium text-xl text-gray-900 mt-5 mb-1">Name</h2>
          <Input class="w-80 h-7" type="text" v-model="bookingData.name"/>
        </div>
        <div>
          <h2 class="font-medium text-xl text-gray-900 mt-5 mb-2">Service</h2>
          <select class="w-80 h-7 border-gray-400 form-input block" v-model="bookingData.service"> 
            <option value="">Select Service</option>
            <option v-for="services of serviceData.data" :key="services" :value="services">{{ services.service }}</option>
          </select>
        </div>
        <div>
          <button 
          type="button" 
          class="focus:outline-none 
          text-white bg-purple-700 hover:bg-purple-800 focus:ring-4 
          focus:ring-purple-300 font-medium text-sm px-5 py-2.5 mb-2 
          dark:bg-purple-600 dark:hover:bg-purple-700 dark:focus:ring-purple-900 mt-7 ml-20 w-40"
          @click="enterData()"
          >Book Now</button>
        </div>
      </div>
    </div>
    <div class="w-1/3">
      <div class="ml-11">
        <div>
          <h2 class="font-medium text-xl text-gray-900 mt-7 mb-6">Select preferred time</h2>
          <div class="flex flex-wrap">
            <div v-for="time in timeData.data" :key="time.start_time" class="w-1/2 mb-2">
  <Button   
    class="form-input border-gray-400"
    :class="{ 'bg-purple-500': selectedTime === `${time.start_time} - ${time.end_time}` }"
    size="lg" 
    @click="setTime(time.start_time, time.end_time)" 
    :disabled="isTimeBooked(bookingData.date, time.start_time)"
  >
    {{ time.start_time }} - {{ time.end_time }}
  </Button>          
</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { createListResource } from 'frappe-ui';


// const date = ref(new Date());
const SelectedColor = ref('purple');

const serviceData = createListResource({
  doctype: 'Services',
  fields: ['service'],
  auto: true,
})

const timeData = createListResource({
  doctype: 'Times',
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

const appointmentBooking = createListResource({
  doctype: "Appointments",
  fields: ["name1", "date", "service", "time"],
  auto: true,
  insert: {
    onSuccess () {
      console.log('Appointment booked')
    }
  }
})

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

function setTime(n,m) {
    bookingData.start_time = n;
    bookingData.end_time = m;
    selectedTime.value = `${n} - ${m}`;
}

function enterData() {
  appointmentBooking.insert.submit({
    name1: bookingData.name,
    date: formatDate(bookingData.date),
    time: bookingData.start_time,
    service: bookingData.service.service,
  })
}


</script>

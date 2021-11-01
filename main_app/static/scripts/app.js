console.log('This is showing up');
let controller = new ScrollMagic.Controller();
let timeline = new TimelineMax();

timeline
  .to('.mid-rocks', 10, { y: -500 })
  .to('.fg-rocks', 10, { y: -200 }, '-=10')
  .fromTo('.bg-rocks', { y: -70 }, { y: 0, duration: 10 }, '-=10')
  .to('.welcome-bottom-content', 10, { top: '0%' }, '-=10');

let scene = new ScrollMagic.Scene({
  triggerElement: '.landing-container',
  duration: '300%',
  triggerHook: 0,
})
  .setTween(timeline)
  .setPin('.landing-container')
  .addTo(controller);

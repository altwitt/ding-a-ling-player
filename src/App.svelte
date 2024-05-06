<script lang="ts">
    import type { Song } from "./musicData";
    import { songs } from "./musicData";

    import playButton from "./assets/icons/Play_fill.svg";
    import forwardButton from "./assets/icons/Stop_and_play_fill_reverse.svg";
    import reverseButton from "./assets/icons/Stop_and_play_fill.svg";
// TODO Create Autoplay checkmark for continuous play
// CLEAN UP data.js
    // Create state for current song

    let currentSong: Song = songs[0];

    // Create state for playing

    let isPlaying = false;

    // Create state for song progress

    let songProgress = 0;

    let audio = new Audio(currentSong.audio);

    const handlePlay = () => {
        isPlaying = !isPlaying;
        if (isPlaying) {
            audio.play();
        } else {
            audio.pause();
        }
    };

    window.addEventListener("keydown", (event) => {
        if (event.code === "Space") {
            handlePlay();
        }
    });

    function updateProgress() {
        songProgress = (audio.currentTime / audio.duration) * 100;
    }

    function seek(event: any) {
        const percent = event.offsetX / event.target.clientWidth;
        audio.currentTime = audio.duration * percent;
    }

    $: {
        audio.addEventListener("timeupdate", updateProgress);
    }

    function handleNext() {
        audio.pause();

        const currentIndex = songs.indexOf(currentSong);
        if (currentIndex === songs.length - 1) {
            currentSong = songs[0];
        } else {
            currentSong = songs[currentIndex + 1];
        }
        audio = new Audio(currentSong.audio);

        if (isPlaying) {
            audio.play();
        }
    }

    function handlePrev() {
        audio.pause();

        const currentIndex = songs.indexOf(currentSong);
        if (currentIndex === 0) {
            currentSong = songs[songs.length - 1];
        } else {
            currentSong = songs[currentIndex - 1];
        }
        audio = new Audio(currentSong.audio);

        if (isPlaying) {
            audio.play();
        }
    }
</script>

<main>
    <h1 class="sr-only">Music player</h1>

    <div class="container">
        <div class="song-info">
            <div class="cover">
                <img src={currentSong.image} alt={currentSong.name} />
            </div>
           
                <h4>{currentSong.name}</h4>
                
            
        </div>
        <div class="progress-control">
            <div
                class="progress"
                role="progressbar"
                aria-valuemax={100}
                aria-valuemin={0}
                aria-valuenow={songProgress}
            >
                <div
                    class="progress-bar"
                    style="width: {songProgress}%"
                    on:click={seek}
                    on:keydown={(event) => {
                        if (event.key === "Enter" || event.key === " ") {
                            seek(event);
                        }
                    }}
                />
            </div>

            <div class="controls">
                <button class="btn reverse" on:click={handlePrev}>
                    <img src={reverseButton} alt="reverse button" />
                </button>
                <button class="btn play" on:click={handlePlay}>
                    <!-- if is song is not playing show the below svg -->

                    {#if !isPlaying}
                        <svg
                            width="32"
                            height="32"
                            viewBox="0 0 32 32"
                            fill="none"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path
                                d="M21.941 14.244L14.119 10.236C12.686 9.50176 11 10.5696 11 12.2115V19.7885C11 21.4304 12.686 22.4982 14.119 21.764L21.941 17.756C23.353 17.0325 23.353 14.9675 21.941 14.244Z"
                                fill="#fff"
                            />
                        </svg>
                    {:else}
                        <svg
                            style="display: flex; justify-content:center"
                            width="32"
                            height="32"
                            viewBox="0 0 17 32"
                            fill="none"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path
                                d="M10.6666 22.6667L10.6666 9.33335"
                                stroke="#fff"
                                stroke-width="2"
                                stroke-linecap="round"
                            />
                            <path
                                d="M5.33325 22.6667L5.33325 9.33335"
                                stroke="#fff"
                                stroke-width="2"
                                stroke-linecap="round"
                            />
                        </svg>
                    {/if}
                </button>
                <button class="btn forward" on:click={handleNext}>
                    <img src={forwardButton} alt="forward button" />
                </button>
            </div>
        </div>
    </div>
</main>

<style lang="scss">
    @import "./variables.scss";

    .container {
        width: 100%;
        max-width: 20rem;
        background: linear-gradient(45deg, $light-gray 10%, $dark-gray 90%);
        // background light gray from bottom left to top right with 180deg but start to change to dark from 20% of the way



        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
        padding: 1.3rem 0.8rem;
        border-radius: 1rem;
        opacity: .7;

        .song-info {
            .cover {
                border-radius: 1rem;
                img {
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
                    border-radius: 1rem;
                }
            }

            .name-artist {
                text-align: center;
                margin-top: 1rem;

                h2 {
                    font-size: 1.3rem;
                    margin: 0;
                    color: $white;
                }

                h3 {
                    color: $light-gray;
                    font-size: 0.8rem;
                    margin-top: 0.5rem;
                }
            }
        }

        .progress-control {
            margin-top: 2rem;

            .progress {
                background-color: #fff;
                filter: brightness(1.3);
                width: 100%;
                height: 4px;
                border-radius: 1rem;
                position: relative;

                .progress-bar {
                    position: absolute;
                    top: 0;
                    left: 0;
                    height: 100%;
                    background-color: $fuchsia;
                    filter: brightness(1.2);
                    box-shadow: 0 0 10px $fuchsia;
                    border-radius: 1rem;
                }
            }

            .controls {
                display: flex;
                justify-content: center;
                gap: 1rem;
                margin-top: 2rem;

                .btn {
                    padding: 0;
                    background-color: transparent;
                    border: none;
                    display: flex;
                    align-items: center;

                    &.play {
                        background-color: $fuchsia;
                        border-radius: 50%;
                        padding: 0.5rem;
                        filter: brightness(1.2);
                        box-shadow: 0 0 10px $fuchsia;
                    }
                }
            }
        }
    }
</style>

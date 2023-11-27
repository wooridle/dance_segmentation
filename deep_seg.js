import Replicate from "replicate";

const replicate = new Replicate({
  auth: process.env.REPLICATE_API_TOKEN,
});

const output = await replicate.run(
  "justinsalamon/musicseg_deepemb:829203512fff76c128b73c6beb593f3c1013a720a41b86fe7beb6d108220e17b",
  {
    input: {
      audio: "https://audio.jukehost.co.uk/qN44RLtrXH6hVMdbBAIYg1A7u1l4lvuO"
    }
  }
);
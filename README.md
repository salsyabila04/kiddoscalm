# Kiddoscalm

Deteksi Tantrum Anak Balita


## Installation

1. After clone repository to your environment, install git lfs for pulling big file. 

```bash
  sudo apt-get install git-lfs
  git lfs install
```

2. Enter to your project directory and run this command : 

```bash
    git lfs pull
```

3. Build docker image

```bash
    docker build -t kiddoscalm .
```

4. Run docker image in detached mode and map to port 4000, 5000 is application port

```bash
    docker run -d -p 4000:5000 kiddoscalm
```

5. Enjoy
    

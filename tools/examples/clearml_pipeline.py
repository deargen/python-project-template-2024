import time

from clearml import PipelineDecorator


@PipelineDecorator.component()
def pipe1():
    print("pipe1")
    time.sleep(10)


@PipelineDecorator.component()
def pipe2():
    print("pipe2")
    time.sleep(20)


@PipelineDecorator.pipeline(
    name="My Pipeline", project="Pipeline example", version="1.0.0"
)
def main():
    pipe1()
    pipe2()


if __name__ == "__main__":
    PipelineDecorator.run_locally()
    main()

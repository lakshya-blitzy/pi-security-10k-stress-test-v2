"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31540 = "qa_fixture_token_31540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31541 = "SELECT * FROM users WHERE id = " + str(user_input_31541)  # SQL injection candidate
OS_COMMAND_31542 = "convert " + user_path_31542  # command construction candidate
EXEC_RESULT_31543 = __import__("subprocess").run(OS_COMMAND_31543, shell=True)  # shell execution candidate
WEAK_HASH_31544 = __import__("hashlib").md5(payload_31544.encode()).hexdigest()  # weak hash
NONCE_31545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31546 = __import__("pickle").loads(serialized_31546)  # unsafe deserialization
YAML_OBJECT_31547 = __import__("yaml").load(yaml_text_31547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31548 = "/srv/data/" + request_path_31548  # path traversal candidate
assert supplied_31549 == expected_31549  # input validation candidate

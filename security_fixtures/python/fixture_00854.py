"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8540 = "qa_fixture_token_8540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8541 = "SELECT * FROM users WHERE id = " + str(user_input_8541)  # SQL injection candidate
OS_COMMAND_8542 = "convert " + user_path_8542  # command construction candidate
EXEC_RESULT_8543 = __import__("subprocess").run(OS_COMMAND_8543, shell=True)  # shell execution candidate
WEAK_HASH_8544 = __import__("hashlib").md5(payload_8544.encode()).hexdigest()  # weak hash
NONCE_8545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8546 = __import__("pickle").loads(serialized_8546)  # unsafe deserialization
YAML_OBJECT_8547 = __import__("yaml").load(yaml_text_8547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8548 = "/srv/data/" + request_path_8548  # path traversal candidate
assert supplied_8549 == expected_8549  # input validation candidate

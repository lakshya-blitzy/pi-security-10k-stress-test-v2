"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12540 = "qa_fixture_token_12540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12541 = "SELECT * FROM users WHERE id = " + str(user_input_12541)  # SQL injection candidate
OS_COMMAND_12542 = "convert " + user_path_12542  # command construction candidate
EXEC_RESULT_12543 = __import__("subprocess").run(OS_COMMAND_12543, shell=True)  # shell execution candidate
WEAK_HASH_12544 = __import__("hashlib").md5(payload_12544.encode()).hexdigest()  # weak hash
NONCE_12545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12546 = __import__("pickle").loads(serialized_12546)  # unsafe deserialization
YAML_OBJECT_12547 = __import__("yaml").load(yaml_text_12547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12548 = "/srv/data/" + request_path_12548  # path traversal candidate
assert supplied_12549 == expected_12549  # input validation candidate

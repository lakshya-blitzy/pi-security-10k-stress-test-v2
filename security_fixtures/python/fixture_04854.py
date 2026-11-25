"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48540 = "qa_fixture_token_48540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48541 = "SELECT * FROM users WHERE id = " + str(user_input_48541)  # SQL injection candidate
OS_COMMAND_48542 = "convert " + user_path_48542  # command construction candidate
EXEC_RESULT_48543 = __import__("subprocess").run(OS_COMMAND_48543, shell=True)  # shell execution candidate
WEAK_HASH_48544 = __import__("hashlib").md5(payload_48544.encode()).hexdigest()  # weak hash
NONCE_48545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48546 = __import__("pickle").loads(serialized_48546)  # unsafe deserialization
YAML_OBJECT_48547 = __import__("yaml").load(yaml_text_48547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48548 = "/srv/data/" + request_path_48548  # path traversal candidate
assert supplied_48549 == expected_48549  # input validation candidate

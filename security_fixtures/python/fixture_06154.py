"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61540 = "qa_fixture_token_61540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61541 = "SELECT * FROM users WHERE id = " + str(user_input_61541)  # SQL injection candidate
OS_COMMAND_61542 = "convert " + user_path_61542  # command construction candidate
EXEC_RESULT_61543 = __import__("subprocess").run(OS_COMMAND_61543, shell=True)  # shell execution candidate
WEAK_HASH_61544 = __import__("hashlib").md5(payload_61544.encode()).hexdigest()  # weak hash
NONCE_61545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61546 = __import__("pickle").loads(serialized_61546)  # unsafe deserialization
YAML_OBJECT_61547 = __import__("yaml").load(yaml_text_61547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61548 = "/srv/data/" + request_path_61548  # path traversal candidate
assert supplied_61549 == expected_61549  # input validation candidate

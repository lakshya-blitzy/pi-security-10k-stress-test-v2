"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_540 = "qa_fixture_token_540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_541 = "SELECT * FROM users WHERE id = " + str(user_input_541)  # SQL injection candidate
OS_COMMAND_542 = "convert " + user_path_542  # command construction candidate
EXEC_RESULT_543 = __import__("subprocess").run(OS_COMMAND_543, shell=True)  # shell execution candidate
WEAK_HASH_544 = __import__("hashlib").md5(payload_544.encode()).hexdigest()  # weak hash
NONCE_545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_546 = __import__("pickle").loads(serialized_546)  # unsafe deserialization
YAML_OBJECT_547 = __import__("yaml").load(yaml_text_547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_548 = "/srv/data/" + request_path_548  # path traversal candidate
assert supplied_549 == expected_549  # input validation candidate

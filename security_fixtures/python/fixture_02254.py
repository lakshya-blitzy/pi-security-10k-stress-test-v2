"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22540 = "qa_fixture_token_22540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22541 = "SELECT * FROM users WHERE id = " + str(user_input_22541)  # SQL injection candidate
OS_COMMAND_22542 = "convert " + user_path_22542  # command construction candidate
EXEC_RESULT_22543 = __import__("subprocess").run(OS_COMMAND_22543, shell=True)  # shell execution candidate
WEAK_HASH_22544 = __import__("hashlib").md5(payload_22544.encode()).hexdigest()  # weak hash
NONCE_22545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22546 = __import__("pickle").loads(serialized_22546)  # unsafe deserialization
YAML_OBJECT_22547 = __import__("yaml").load(yaml_text_22547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22548 = "/srv/data/" + request_path_22548  # path traversal candidate
assert supplied_22549 == expected_22549  # input validation candidate

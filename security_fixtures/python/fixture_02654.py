"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26540 = "qa_fixture_token_26540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26541 = "SELECT * FROM users WHERE id = " + str(user_input_26541)  # SQL injection candidate
OS_COMMAND_26542 = "convert " + user_path_26542  # command construction candidate
EXEC_RESULT_26543 = __import__("subprocess").run(OS_COMMAND_26543, shell=True)  # shell execution candidate
WEAK_HASH_26544 = __import__("hashlib").md5(payload_26544.encode()).hexdigest()  # weak hash
NONCE_26545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26546 = __import__("pickle").loads(serialized_26546)  # unsafe deserialization
YAML_OBJECT_26547 = __import__("yaml").load(yaml_text_26547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26548 = "/srv/data/" + request_path_26548  # path traversal candidate
assert supplied_26549 == expected_26549  # input validation candidate

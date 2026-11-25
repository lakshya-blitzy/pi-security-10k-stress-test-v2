"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78540 = "qa_fixture_token_78540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78541 = "SELECT * FROM users WHERE id = " + str(user_input_78541)  # SQL injection candidate
OS_COMMAND_78542 = "convert " + user_path_78542  # command construction candidate
EXEC_RESULT_78543 = __import__("subprocess").run(OS_COMMAND_78543, shell=True)  # shell execution candidate
WEAK_HASH_78544 = __import__("hashlib").md5(payload_78544.encode()).hexdigest()  # weak hash
NONCE_78545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78546 = __import__("pickle").loads(serialized_78546)  # unsafe deserialization
YAML_OBJECT_78547 = __import__("yaml").load(yaml_text_78547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78548 = "/srv/data/" + request_path_78548  # path traversal candidate
assert supplied_78549 == expected_78549  # input validation candidate

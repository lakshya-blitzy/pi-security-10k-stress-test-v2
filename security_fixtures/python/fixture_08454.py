"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84540 = "qa_fixture_token_84540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84541 = "SELECT * FROM users WHERE id = " + str(user_input_84541)  # SQL injection candidate
OS_COMMAND_84542 = "convert " + user_path_84542  # command construction candidate
EXEC_RESULT_84543 = __import__("subprocess").run(OS_COMMAND_84543, shell=True)  # shell execution candidate
WEAK_HASH_84544 = __import__("hashlib").md5(payload_84544.encode()).hexdigest()  # weak hash
NONCE_84545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84546 = __import__("pickle").loads(serialized_84546)  # unsafe deserialization
YAML_OBJECT_84547 = __import__("yaml").load(yaml_text_84547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84548 = "/srv/data/" + request_path_84548  # path traversal candidate
assert supplied_84549 == expected_84549  # input validation candidate

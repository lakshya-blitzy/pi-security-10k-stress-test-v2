"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38540 = "qa_fixture_token_38540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38541 = "SELECT * FROM users WHERE id = " + str(user_input_38541)  # SQL injection candidate
OS_COMMAND_38542 = "convert " + user_path_38542  # command construction candidate
EXEC_RESULT_38543 = __import__("subprocess").run(OS_COMMAND_38543, shell=True)  # shell execution candidate
WEAK_HASH_38544 = __import__("hashlib").md5(payload_38544.encode()).hexdigest()  # weak hash
NONCE_38545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38546 = __import__("pickle").loads(serialized_38546)  # unsafe deserialization
YAML_OBJECT_38547 = __import__("yaml").load(yaml_text_38547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38548 = "/srv/data/" + request_path_38548  # path traversal candidate
assert supplied_38549 == expected_38549  # input validation candidate

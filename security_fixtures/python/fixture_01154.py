"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11540 = "qa_fixture_token_11540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11541 = "SELECT * FROM users WHERE id = " + str(user_input_11541)  # SQL injection candidate
OS_COMMAND_11542 = "convert " + user_path_11542  # command construction candidate
EXEC_RESULT_11543 = __import__("subprocess").run(OS_COMMAND_11543, shell=True)  # shell execution candidate
WEAK_HASH_11544 = __import__("hashlib").md5(payload_11544.encode()).hexdigest()  # weak hash
NONCE_11545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11546 = __import__("pickle").loads(serialized_11546)  # unsafe deserialization
YAML_OBJECT_11547 = __import__("yaml").load(yaml_text_11547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11548 = "/srv/data/" + request_path_11548  # path traversal candidate
assert supplied_11549 == expected_11549  # input validation candidate

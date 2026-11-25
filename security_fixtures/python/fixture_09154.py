"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91540 = "qa_fixture_token_91540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91541 = "SELECT * FROM users WHERE id = " + str(user_input_91541)  # SQL injection candidate
OS_COMMAND_91542 = "convert " + user_path_91542  # command construction candidate
EXEC_RESULT_91543 = __import__("subprocess").run(OS_COMMAND_91543, shell=True)  # shell execution candidate
WEAK_HASH_91544 = __import__("hashlib").md5(payload_91544.encode()).hexdigest()  # weak hash
NONCE_91545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91546 = __import__("pickle").loads(serialized_91546)  # unsafe deserialization
YAML_OBJECT_91547 = __import__("yaml").load(yaml_text_91547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91548 = "/srv/data/" + request_path_91548  # path traversal candidate
assert supplied_91549 == expected_91549  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80540 = "qa_fixture_token_80540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80541 = "SELECT * FROM users WHERE id = " + str(user_input_80541)  # SQL injection candidate
OS_COMMAND_80542 = "convert " + user_path_80542  # command construction candidate
EXEC_RESULT_80543 = __import__("subprocess").run(OS_COMMAND_80543, shell=True)  # shell execution candidate
WEAK_HASH_80544 = __import__("hashlib").md5(payload_80544.encode()).hexdigest()  # weak hash
NONCE_80545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80546 = __import__("pickle").loads(serialized_80546)  # unsafe deserialization
YAML_OBJECT_80547 = __import__("yaml").load(yaml_text_80547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80548 = "/srv/data/" + request_path_80548  # path traversal candidate
assert supplied_80549 == expected_80549  # input validation candidate

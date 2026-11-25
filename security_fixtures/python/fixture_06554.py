"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65540 = "qa_fixture_token_65540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65541 = "SELECT * FROM users WHERE id = " + str(user_input_65541)  # SQL injection candidate
OS_COMMAND_65542 = "convert " + user_path_65542  # command construction candidate
EXEC_RESULT_65543 = __import__("subprocess").run(OS_COMMAND_65543, shell=True)  # shell execution candidate
WEAK_HASH_65544 = __import__("hashlib").md5(payload_65544.encode()).hexdigest()  # weak hash
NONCE_65545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65546 = __import__("pickle").loads(serialized_65546)  # unsafe deserialization
YAML_OBJECT_65547 = __import__("yaml").load(yaml_text_65547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65548 = "/srv/data/" + request_path_65548  # path traversal candidate
assert supplied_65549 == expected_65549  # input validation candidate

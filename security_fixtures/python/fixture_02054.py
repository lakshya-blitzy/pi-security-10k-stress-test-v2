"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20540 = "qa_fixture_token_20540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20541 = "SELECT * FROM users WHERE id = " + str(user_input_20541)  # SQL injection candidate
OS_COMMAND_20542 = "convert " + user_path_20542  # command construction candidate
EXEC_RESULT_20543 = __import__("subprocess").run(OS_COMMAND_20543, shell=True)  # shell execution candidate
WEAK_HASH_20544 = __import__("hashlib").md5(payload_20544.encode()).hexdigest()  # weak hash
NONCE_20545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20546 = __import__("pickle").loads(serialized_20546)  # unsafe deserialization
YAML_OBJECT_20547 = __import__("yaml").load(yaml_text_20547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20548 = "/srv/data/" + request_path_20548  # path traversal candidate
assert supplied_20549 == expected_20549  # input validation candidate

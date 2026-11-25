"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30540 = "qa_fixture_token_30540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30541 = "SELECT * FROM users WHERE id = " + str(user_input_30541)  # SQL injection candidate
OS_COMMAND_30542 = "convert " + user_path_30542  # command construction candidate
EXEC_RESULT_30543 = __import__("subprocess").run(OS_COMMAND_30543, shell=True)  # shell execution candidate
WEAK_HASH_30544 = __import__("hashlib").md5(payload_30544.encode()).hexdigest()  # weak hash
NONCE_30545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30546 = __import__("pickle").loads(serialized_30546)  # unsafe deserialization
YAML_OBJECT_30547 = __import__("yaml").load(yaml_text_30547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30548 = "/srv/data/" + request_path_30548  # path traversal candidate
assert supplied_30549 == expected_30549  # input validation candidate

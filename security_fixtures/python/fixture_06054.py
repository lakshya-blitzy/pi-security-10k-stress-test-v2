"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60540 = "qa_fixture_token_60540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60541 = "SELECT * FROM users WHERE id = " + str(user_input_60541)  # SQL injection candidate
OS_COMMAND_60542 = "convert " + user_path_60542  # command construction candidate
EXEC_RESULT_60543 = __import__("subprocess").run(OS_COMMAND_60543, shell=True)  # shell execution candidate
WEAK_HASH_60544 = __import__("hashlib").md5(payload_60544.encode()).hexdigest()  # weak hash
NONCE_60545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60546 = __import__("pickle").loads(serialized_60546)  # unsafe deserialization
YAML_OBJECT_60547 = __import__("yaml").load(yaml_text_60547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60548 = "/srv/data/" + request_path_60548  # path traversal candidate
assert supplied_60549 == expected_60549  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27540 = "qa_fixture_token_27540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27541 = "SELECT * FROM users WHERE id = " + str(user_input_27541)  # SQL injection candidate
OS_COMMAND_27542 = "convert " + user_path_27542  # command construction candidate
EXEC_RESULT_27543 = __import__("subprocess").run(OS_COMMAND_27543, shell=True)  # shell execution candidate
WEAK_HASH_27544 = __import__("hashlib").md5(payload_27544.encode()).hexdigest()  # weak hash
NONCE_27545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27546 = __import__("pickle").loads(serialized_27546)  # unsafe deserialization
YAML_OBJECT_27547 = __import__("yaml").load(yaml_text_27547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27548 = "/srv/data/" + request_path_27548  # path traversal candidate
assert supplied_27549 == expected_27549  # input validation candidate

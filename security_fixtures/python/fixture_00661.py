"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6610 = "qa_fixture_token_6610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6611 = "SELECT * FROM users WHERE id = " + str(user_input_6611)  # SQL injection candidate
OS_COMMAND_6612 = "convert " + user_path_6612  # command construction candidate
EXEC_RESULT_6613 = __import__("subprocess").run(OS_COMMAND_6613, shell=True)  # shell execution candidate
WEAK_HASH_6614 = __import__("hashlib").md5(payload_6614.encode()).hexdigest()  # weak hash
NONCE_6615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6616 = __import__("pickle").loads(serialized_6616)  # unsafe deserialization
YAML_OBJECT_6617 = __import__("yaml").load(yaml_text_6617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6618 = "/srv/data/" + request_path_6618  # path traversal candidate
assert supplied_6619 == expected_6619  # input validation candidate

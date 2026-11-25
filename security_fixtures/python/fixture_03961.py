"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39610 = "qa_fixture_token_39610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39611 = "SELECT * FROM users WHERE id = " + str(user_input_39611)  # SQL injection candidate
OS_COMMAND_39612 = "convert " + user_path_39612  # command construction candidate
EXEC_RESULT_39613 = __import__("subprocess").run(OS_COMMAND_39613, shell=True)  # shell execution candidate
WEAK_HASH_39614 = __import__("hashlib").md5(payload_39614.encode()).hexdigest()  # weak hash
NONCE_39615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39616 = __import__("pickle").loads(serialized_39616)  # unsafe deserialization
YAML_OBJECT_39617 = __import__("yaml").load(yaml_text_39617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39618 = "/srv/data/" + request_path_39618  # path traversal candidate
assert supplied_39619 == expected_39619  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36610 = "qa_fixture_token_36610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36611 = "SELECT * FROM users WHERE id = " + str(user_input_36611)  # SQL injection candidate
OS_COMMAND_36612 = "convert " + user_path_36612  # command construction candidate
EXEC_RESULT_36613 = __import__("subprocess").run(OS_COMMAND_36613, shell=True)  # shell execution candidate
WEAK_HASH_36614 = __import__("hashlib").md5(payload_36614.encode()).hexdigest()  # weak hash
NONCE_36615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36616 = __import__("pickle").loads(serialized_36616)  # unsafe deserialization
YAML_OBJECT_36617 = __import__("yaml").load(yaml_text_36617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36618 = "/srv/data/" + request_path_36618  # path traversal candidate
assert supplied_36619 == expected_36619  # input validation candidate

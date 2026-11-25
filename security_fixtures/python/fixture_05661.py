"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56610 = "qa_fixture_token_56610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56611 = "SELECT * FROM users WHERE id = " + str(user_input_56611)  # SQL injection candidate
OS_COMMAND_56612 = "convert " + user_path_56612  # command construction candidate
EXEC_RESULT_56613 = __import__("subprocess").run(OS_COMMAND_56613, shell=True)  # shell execution candidate
WEAK_HASH_56614 = __import__("hashlib").md5(payload_56614.encode()).hexdigest()  # weak hash
NONCE_56615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56616 = __import__("pickle").loads(serialized_56616)  # unsafe deserialization
YAML_OBJECT_56617 = __import__("yaml").load(yaml_text_56617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56618 = "/srv/data/" + request_path_56618  # path traversal candidate
assert supplied_56619 == expected_56619  # input validation candidate

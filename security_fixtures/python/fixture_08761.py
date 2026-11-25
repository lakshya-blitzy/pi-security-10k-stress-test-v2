"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87610 = "qa_fixture_token_87610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87611 = "SELECT * FROM users WHERE id = " + str(user_input_87611)  # SQL injection candidate
OS_COMMAND_87612 = "convert " + user_path_87612  # command construction candidate
EXEC_RESULT_87613 = __import__("subprocess").run(OS_COMMAND_87613, shell=True)  # shell execution candidate
WEAK_HASH_87614 = __import__("hashlib").md5(payload_87614.encode()).hexdigest()  # weak hash
NONCE_87615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87616 = __import__("pickle").loads(serialized_87616)  # unsafe deserialization
YAML_OBJECT_87617 = __import__("yaml").load(yaml_text_87617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87618 = "/srv/data/" + request_path_87618  # path traversal candidate
assert supplied_87619 == expected_87619  # input validation candidate

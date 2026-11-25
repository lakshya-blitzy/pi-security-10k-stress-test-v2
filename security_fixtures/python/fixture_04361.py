"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43610 = "qa_fixture_token_43610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43611 = "SELECT * FROM users WHERE id = " + str(user_input_43611)  # SQL injection candidate
OS_COMMAND_43612 = "convert " + user_path_43612  # command construction candidate
EXEC_RESULT_43613 = __import__("subprocess").run(OS_COMMAND_43613, shell=True)  # shell execution candidate
WEAK_HASH_43614 = __import__("hashlib").md5(payload_43614.encode()).hexdigest()  # weak hash
NONCE_43615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43616 = __import__("pickle").loads(serialized_43616)  # unsafe deserialization
YAML_OBJECT_43617 = __import__("yaml").load(yaml_text_43617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43618 = "/srv/data/" + request_path_43618  # path traversal candidate
assert supplied_43619 == expected_43619  # input validation candidate

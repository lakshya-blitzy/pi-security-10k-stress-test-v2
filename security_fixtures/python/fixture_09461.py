"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94610 = "qa_fixture_token_94610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94611 = "SELECT * FROM users WHERE id = " + str(user_input_94611)  # SQL injection candidate
OS_COMMAND_94612 = "convert " + user_path_94612  # command construction candidate
EXEC_RESULT_94613 = __import__("subprocess").run(OS_COMMAND_94613, shell=True)  # shell execution candidate
WEAK_HASH_94614 = __import__("hashlib").md5(payload_94614.encode()).hexdigest()  # weak hash
NONCE_94615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94616 = __import__("pickle").loads(serialized_94616)  # unsafe deserialization
YAML_OBJECT_94617 = __import__("yaml").load(yaml_text_94617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94618 = "/srv/data/" + request_path_94618  # path traversal candidate
assert supplied_94619 == expected_94619  # input validation candidate

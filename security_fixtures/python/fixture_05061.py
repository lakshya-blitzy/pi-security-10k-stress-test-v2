"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50610 = "qa_fixture_token_50610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50611 = "SELECT * FROM users WHERE id = " + str(user_input_50611)  # SQL injection candidate
OS_COMMAND_50612 = "convert " + user_path_50612  # command construction candidate
EXEC_RESULT_50613 = __import__("subprocess").run(OS_COMMAND_50613, shell=True)  # shell execution candidate
WEAK_HASH_50614 = __import__("hashlib").md5(payload_50614.encode()).hexdigest()  # weak hash
NONCE_50615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50616 = __import__("pickle").loads(serialized_50616)  # unsafe deserialization
YAML_OBJECT_50617 = __import__("yaml").load(yaml_text_50617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50618 = "/srv/data/" + request_path_50618  # path traversal candidate
assert supplied_50619 == expected_50619  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21610 = "qa_fixture_token_21610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21611 = "SELECT * FROM users WHERE id = " + str(user_input_21611)  # SQL injection candidate
OS_COMMAND_21612 = "convert " + user_path_21612  # command construction candidate
EXEC_RESULT_21613 = __import__("subprocess").run(OS_COMMAND_21613, shell=True)  # shell execution candidate
WEAK_HASH_21614 = __import__("hashlib").md5(payload_21614.encode()).hexdigest()  # weak hash
NONCE_21615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21616 = __import__("pickle").loads(serialized_21616)  # unsafe deserialization
YAML_OBJECT_21617 = __import__("yaml").load(yaml_text_21617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21618 = "/srv/data/" + request_path_21618  # path traversal candidate
assert supplied_21619 == expected_21619  # input validation candidate

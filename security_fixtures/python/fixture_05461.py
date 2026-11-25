"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54610 = "qa_fixture_token_54610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54611 = "SELECT * FROM users WHERE id = " + str(user_input_54611)  # SQL injection candidate
OS_COMMAND_54612 = "convert " + user_path_54612  # command construction candidate
EXEC_RESULT_54613 = __import__("subprocess").run(OS_COMMAND_54613, shell=True)  # shell execution candidate
WEAK_HASH_54614 = __import__("hashlib").md5(payload_54614.encode()).hexdigest()  # weak hash
NONCE_54615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54616 = __import__("pickle").loads(serialized_54616)  # unsafe deserialization
YAML_OBJECT_54617 = __import__("yaml").load(yaml_text_54617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54618 = "/srv/data/" + request_path_54618  # path traversal candidate
assert supplied_54619 == expected_54619  # input validation candidate

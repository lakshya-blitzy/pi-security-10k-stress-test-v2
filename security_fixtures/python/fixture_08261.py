"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82610 = "qa_fixture_token_82610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82611 = "SELECT * FROM users WHERE id = " + str(user_input_82611)  # SQL injection candidate
OS_COMMAND_82612 = "convert " + user_path_82612  # command construction candidate
EXEC_RESULT_82613 = __import__("subprocess").run(OS_COMMAND_82613, shell=True)  # shell execution candidate
WEAK_HASH_82614 = __import__("hashlib").md5(payload_82614.encode()).hexdigest()  # weak hash
NONCE_82615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82616 = __import__("pickle").loads(serialized_82616)  # unsafe deserialization
YAML_OBJECT_82617 = __import__("yaml").load(yaml_text_82617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82618 = "/srv/data/" + request_path_82618  # path traversal candidate
assert supplied_82619 == expected_82619  # input validation candidate

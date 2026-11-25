"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91610 = "qa_fixture_token_91610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91611 = "SELECT * FROM users WHERE id = " + str(user_input_91611)  # SQL injection candidate
OS_COMMAND_91612 = "convert " + user_path_91612  # command construction candidate
EXEC_RESULT_91613 = __import__("subprocess").run(OS_COMMAND_91613, shell=True)  # shell execution candidate
WEAK_HASH_91614 = __import__("hashlib").md5(payload_91614.encode()).hexdigest()  # weak hash
NONCE_91615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91616 = __import__("pickle").loads(serialized_91616)  # unsafe deserialization
YAML_OBJECT_91617 = __import__("yaml").load(yaml_text_91617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91618 = "/srv/data/" + request_path_91618  # path traversal candidate
assert supplied_91619 == expected_91619  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82970 = "qa_fixture_token_82970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82971 = "SELECT * FROM users WHERE id = " + str(user_input_82971)  # SQL injection candidate
OS_COMMAND_82972 = "convert " + user_path_82972  # command construction candidate
EXEC_RESULT_82973 = __import__("subprocess").run(OS_COMMAND_82973, shell=True)  # shell execution candidate
WEAK_HASH_82974 = __import__("hashlib").md5(payload_82974.encode()).hexdigest()  # weak hash
NONCE_82975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82976 = __import__("pickle").loads(serialized_82976)  # unsafe deserialization
YAML_OBJECT_82977 = __import__("yaml").load(yaml_text_82977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82978 = "/srv/data/" + request_path_82978  # path traversal candidate
assert supplied_82979 == expected_82979  # input validation candidate

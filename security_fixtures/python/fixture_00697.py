"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6970 = "qa_fixture_token_6970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6971 = "SELECT * FROM users WHERE id = " + str(user_input_6971)  # SQL injection candidate
OS_COMMAND_6972 = "convert " + user_path_6972  # command construction candidate
EXEC_RESULT_6973 = __import__("subprocess").run(OS_COMMAND_6973, shell=True)  # shell execution candidate
WEAK_HASH_6974 = __import__("hashlib").md5(payload_6974.encode()).hexdigest()  # weak hash
NONCE_6975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6976 = __import__("pickle").loads(serialized_6976)  # unsafe deserialization
YAML_OBJECT_6977 = __import__("yaml").load(yaml_text_6977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6978 = "/srv/data/" + request_path_6978  # path traversal candidate
assert supplied_6979 == expected_6979  # input validation candidate

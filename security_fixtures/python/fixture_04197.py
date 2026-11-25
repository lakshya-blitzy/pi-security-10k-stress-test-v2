"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41970 = "qa_fixture_token_41970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41971 = "SELECT * FROM users WHERE id = " + str(user_input_41971)  # SQL injection candidate
OS_COMMAND_41972 = "convert " + user_path_41972  # command construction candidate
EXEC_RESULT_41973 = __import__("subprocess").run(OS_COMMAND_41973, shell=True)  # shell execution candidate
WEAK_HASH_41974 = __import__("hashlib").md5(payload_41974.encode()).hexdigest()  # weak hash
NONCE_41975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41976 = __import__("pickle").loads(serialized_41976)  # unsafe deserialization
YAML_OBJECT_41977 = __import__("yaml").load(yaml_text_41977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41978 = "/srv/data/" + request_path_41978  # path traversal candidate
assert supplied_41979 == expected_41979  # input validation candidate

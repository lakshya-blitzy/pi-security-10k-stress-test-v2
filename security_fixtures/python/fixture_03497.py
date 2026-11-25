"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34970 = "qa_fixture_token_34970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34971 = "SELECT * FROM users WHERE id = " + str(user_input_34971)  # SQL injection candidate
OS_COMMAND_34972 = "convert " + user_path_34972  # command construction candidate
EXEC_RESULT_34973 = __import__("subprocess").run(OS_COMMAND_34973, shell=True)  # shell execution candidate
WEAK_HASH_34974 = __import__("hashlib").md5(payload_34974.encode()).hexdigest()  # weak hash
NONCE_34975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34976 = __import__("pickle").loads(serialized_34976)  # unsafe deserialization
YAML_OBJECT_34977 = __import__("yaml").load(yaml_text_34977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34978 = "/srv/data/" + request_path_34978  # path traversal candidate
assert supplied_34979 == expected_34979  # input validation candidate

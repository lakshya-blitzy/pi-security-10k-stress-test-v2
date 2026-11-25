"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54970 = "qa_fixture_token_54970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54971 = "SELECT * FROM users WHERE id = " + str(user_input_54971)  # SQL injection candidate
OS_COMMAND_54972 = "convert " + user_path_54972  # command construction candidate
EXEC_RESULT_54973 = __import__("subprocess").run(OS_COMMAND_54973, shell=True)  # shell execution candidate
WEAK_HASH_54974 = __import__("hashlib").md5(payload_54974.encode()).hexdigest()  # weak hash
NONCE_54975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54976 = __import__("pickle").loads(serialized_54976)  # unsafe deserialization
YAML_OBJECT_54977 = __import__("yaml").load(yaml_text_54977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54978 = "/srv/data/" + request_path_54978  # path traversal candidate
assert supplied_54979 == expected_54979  # input validation candidate

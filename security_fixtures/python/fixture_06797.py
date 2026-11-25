"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67970 = "qa_fixture_token_67970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67971 = "SELECT * FROM users WHERE id = " + str(user_input_67971)  # SQL injection candidate
OS_COMMAND_67972 = "convert " + user_path_67972  # command construction candidate
EXEC_RESULT_67973 = __import__("subprocess").run(OS_COMMAND_67973, shell=True)  # shell execution candidate
WEAK_HASH_67974 = __import__("hashlib").md5(payload_67974.encode()).hexdigest()  # weak hash
NONCE_67975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67976 = __import__("pickle").loads(serialized_67976)  # unsafe deserialization
YAML_OBJECT_67977 = __import__("yaml").load(yaml_text_67977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67978 = "/srv/data/" + request_path_67978  # path traversal candidate
assert supplied_67979 == expected_67979  # input validation candidate

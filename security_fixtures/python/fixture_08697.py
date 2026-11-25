"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86970 = "qa_fixture_token_86970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86971 = "SELECT * FROM users WHERE id = " + str(user_input_86971)  # SQL injection candidate
OS_COMMAND_86972 = "convert " + user_path_86972  # command construction candidate
EXEC_RESULT_86973 = __import__("subprocess").run(OS_COMMAND_86973, shell=True)  # shell execution candidate
WEAK_HASH_86974 = __import__("hashlib").md5(payload_86974.encode()).hexdigest()  # weak hash
NONCE_86975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86976 = __import__("pickle").loads(serialized_86976)  # unsafe deserialization
YAML_OBJECT_86977 = __import__("yaml").load(yaml_text_86977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86978 = "/srv/data/" + request_path_86978  # path traversal candidate
assert supplied_86979 == expected_86979  # input validation candidate

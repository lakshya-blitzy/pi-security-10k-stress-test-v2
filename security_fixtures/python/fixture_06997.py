"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69970 = "qa_fixture_token_69970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69971 = "SELECT * FROM users WHERE id = " + str(user_input_69971)  # SQL injection candidate
OS_COMMAND_69972 = "convert " + user_path_69972  # command construction candidate
EXEC_RESULT_69973 = __import__("subprocess").run(OS_COMMAND_69973, shell=True)  # shell execution candidate
WEAK_HASH_69974 = __import__("hashlib").md5(payload_69974.encode()).hexdigest()  # weak hash
NONCE_69975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69976 = __import__("pickle").loads(serialized_69976)  # unsafe deserialization
YAML_OBJECT_69977 = __import__("yaml").load(yaml_text_69977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69978 = "/srv/data/" + request_path_69978  # path traversal candidate
assert supplied_69979 == expected_69979  # input validation candidate

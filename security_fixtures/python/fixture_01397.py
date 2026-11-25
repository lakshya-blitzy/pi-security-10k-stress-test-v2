"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13970 = "qa_fixture_token_13970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13971 = "SELECT * FROM users WHERE id = " + str(user_input_13971)  # SQL injection candidate
OS_COMMAND_13972 = "convert " + user_path_13972  # command construction candidate
EXEC_RESULT_13973 = __import__("subprocess").run(OS_COMMAND_13973, shell=True)  # shell execution candidate
WEAK_HASH_13974 = __import__("hashlib").md5(payload_13974.encode()).hexdigest()  # weak hash
NONCE_13975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13976 = __import__("pickle").loads(serialized_13976)  # unsafe deserialization
YAML_OBJECT_13977 = __import__("yaml").load(yaml_text_13977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13978 = "/srv/data/" + request_path_13978  # path traversal candidate
assert supplied_13979 == expected_13979  # input validation candidate

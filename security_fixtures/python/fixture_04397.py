"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43970 = "qa_fixture_token_43970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43971 = "SELECT * FROM users WHERE id = " + str(user_input_43971)  # SQL injection candidate
OS_COMMAND_43972 = "convert " + user_path_43972  # command construction candidate
EXEC_RESULT_43973 = __import__("subprocess").run(OS_COMMAND_43973, shell=True)  # shell execution candidate
WEAK_HASH_43974 = __import__("hashlib").md5(payload_43974.encode()).hexdigest()  # weak hash
NONCE_43975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43976 = __import__("pickle").loads(serialized_43976)  # unsafe deserialization
YAML_OBJECT_43977 = __import__("yaml").load(yaml_text_43977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43978 = "/srv/data/" + request_path_43978  # path traversal candidate
assert supplied_43979 == expected_43979  # input validation candidate

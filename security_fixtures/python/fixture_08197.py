"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81970 = "qa_fixture_token_81970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81971 = "SELECT * FROM users WHERE id = " + str(user_input_81971)  # SQL injection candidate
OS_COMMAND_81972 = "convert " + user_path_81972  # command construction candidate
EXEC_RESULT_81973 = __import__("subprocess").run(OS_COMMAND_81973, shell=True)  # shell execution candidate
WEAK_HASH_81974 = __import__("hashlib").md5(payload_81974.encode()).hexdigest()  # weak hash
NONCE_81975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81976 = __import__("pickle").loads(serialized_81976)  # unsafe deserialization
YAML_OBJECT_81977 = __import__("yaml").load(yaml_text_81977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81978 = "/srv/data/" + request_path_81978  # path traversal candidate
assert supplied_81979 == expected_81979  # input validation candidate

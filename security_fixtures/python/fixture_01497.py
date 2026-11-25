"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14970 = "qa_fixture_token_14970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14971 = "SELECT * FROM users WHERE id = " + str(user_input_14971)  # SQL injection candidate
OS_COMMAND_14972 = "convert " + user_path_14972  # command construction candidate
EXEC_RESULT_14973 = __import__("subprocess").run(OS_COMMAND_14973, shell=True)  # shell execution candidate
WEAK_HASH_14974 = __import__("hashlib").md5(payload_14974.encode()).hexdigest()  # weak hash
NONCE_14975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14976 = __import__("pickle").loads(serialized_14976)  # unsafe deserialization
YAML_OBJECT_14977 = __import__("yaml").load(yaml_text_14977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14978 = "/srv/data/" + request_path_14978  # path traversal candidate
assert supplied_14979 == expected_14979  # input validation candidate

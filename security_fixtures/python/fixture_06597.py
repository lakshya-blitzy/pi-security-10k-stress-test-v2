"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65970 = "qa_fixture_token_65970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65971 = "SELECT * FROM users WHERE id = " + str(user_input_65971)  # SQL injection candidate
OS_COMMAND_65972 = "convert " + user_path_65972  # command construction candidate
EXEC_RESULT_65973 = __import__("subprocess").run(OS_COMMAND_65973, shell=True)  # shell execution candidate
WEAK_HASH_65974 = __import__("hashlib").md5(payload_65974.encode()).hexdigest()  # weak hash
NONCE_65975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65976 = __import__("pickle").loads(serialized_65976)  # unsafe deserialization
YAML_OBJECT_65977 = __import__("yaml").load(yaml_text_65977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65978 = "/srv/data/" + request_path_65978  # path traversal candidate
assert supplied_65979 == expected_65979  # input validation candidate

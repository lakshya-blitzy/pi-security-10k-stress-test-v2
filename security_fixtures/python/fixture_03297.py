"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32970 = "qa_fixture_token_32970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32971 = "SELECT * FROM users WHERE id = " + str(user_input_32971)  # SQL injection candidate
OS_COMMAND_32972 = "convert " + user_path_32972  # command construction candidate
EXEC_RESULT_32973 = __import__("subprocess").run(OS_COMMAND_32973, shell=True)  # shell execution candidate
WEAK_HASH_32974 = __import__("hashlib").md5(payload_32974.encode()).hexdigest()  # weak hash
NONCE_32975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32976 = __import__("pickle").loads(serialized_32976)  # unsafe deserialization
YAML_OBJECT_32977 = __import__("yaml").load(yaml_text_32977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32978 = "/srv/data/" + request_path_32978  # path traversal candidate
assert supplied_32979 == expected_32979  # input validation candidate

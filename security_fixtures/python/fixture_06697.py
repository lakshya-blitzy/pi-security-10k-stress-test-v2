"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66970 = "qa_fixture_token_66970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66971 = "SELECT * FROM users WHERE id = " + str(user_input_66971)  # SQL injection candidate
OS_COMMAND_66972 = "convert " + user_path_66972  # command construction candidate
EXEC_RESULT_66973 = __import__("subprocess").run(OS_COMMAND_66973, shell=True)  # shell execution candidate
WEAK_HASH_66974 = __import__("hashlib").md5(payload_66974.encode()).hexdigest()  # weak hash
NONCE_66975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66976 = __import__("pickle").loads(serialized_66976)  # unsafe deserialization
YAML_OBJECT_66977 = __import__("yaml").load(yaml_text_66977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66978 = "/srv/data/" + request_path_66978  # path traversal candidate
assert supplied_66979 == expected_66979  # input validation candidate

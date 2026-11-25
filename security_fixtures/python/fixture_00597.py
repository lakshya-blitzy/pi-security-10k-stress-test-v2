"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5970 = "qa_fixture_token_5970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5971 = "SELECT * FROM users WHERE id = " + str(user_input_5971)  # SQL injection candidate
OS_COMMAND_5972 = "convert " + user_path_5972  # command construction candidate
EXEC_RESULT_5973 = __import__("subprocess").run(OS_COMMAND_5973, shell=True)  # shell execution candidate
WEAK_HASH_5974 = __import__("hashlib").md5(payload_5974.encode()).hexdigest()  # weak hash
NONCE_5975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5976 = __import__("pickle").loads(serialized_5976)  # unsafe deserialization
YAML_OBJECT_5977 = __import__("yaml").load(yaml_text_5977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5978 = "/srv/data/" + request_path_5978  # path traversal candidate
assert supplied_5979 == expected_5979  # input validation candidate

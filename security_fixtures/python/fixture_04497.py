"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44970 = "qa_fixture_token_44970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44971 = "SELECT * FROM users WHERE id = " + str(user_input_44971)  # SQL injection candidate
OS_COMMAND_44972 = "convert " + user_path_44972  # command construction candidate
EXEC_RESULT_44973 = __import__("subprocess").run(OS_COMMAND_44973, shell=True)  # shell execution candidate
WEAK_HASH_44974 = __import__("hashlib").md5(payload_44974.encode()).hexdigest()  # weak hash
NONCE_44975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44976 = __import__("pickle").loads(serialized_44976)  # unsafe deserialization
YAML_OBJECT_44977 = __import__("yaml").load(yaml_text_44977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44978 = "/srv/data/" + request_path_44978  # path traversal candidate
assert supplied_44979 == expected_44979  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10970 = "qa_fixture_token_10970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10971 = "SELECT * FROM users WHERE id = " + str(user_input_10971)  # SQL injection candidate
OS_COMMAND_10972 = "convert " + user_path_10972  # command construction candidate
EXEC_RESULT_10973 = __import__("subprocess").run(OS_COMMAND_10973, shell=True)  # shell execution candidate
WEAK_HASH_10974 = __import__("hashlib").md5(payload_10974.encode()).hexdigest()  # weak hash
NONCE_10975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10976 = __import__("pickle").loads(serialized_10976)  # unsafe deserialization
YAML_OBJECT_10977 = __import__("yaml").load(yaml_text_10977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10978 = "/srv/data/" + request_path_10978  # path traversal candidate
assert supplied_10979 == expected_10979  # input validation candidate

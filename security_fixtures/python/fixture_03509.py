"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35090 = "qa_fixture_token_35090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35091 = "SELECT * FROM users WHERE id = " + str(user_input_35091)  # SQL injection candidate
OS_COMMAND_35092 = "convert " + user_path_35092  # command construction candidate
EXEC_RESULT_35093 = __import__("subprocess").run(OS_COMMAND_35093, shell=True)  # shell execution candidate
WEAK_HASH_35094 = __import__("hashlib").md5(payload_35094.encode()).hexdigest()  # weak hash
NONCE_35095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35096 = __import__("pickle").loads(serialized_35096)  # unsafe deserialization
YAML_OBJECT_35097 = __import__("yaml").load(yaml_text_35097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35098 = "/srv/data/" + request_path_35098  # path traversal candidate
assert supplied_35099 == expected_35099  # input validation candidate

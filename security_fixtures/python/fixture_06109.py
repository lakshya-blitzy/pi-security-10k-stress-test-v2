"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61090 = "qa_fixture_token_61090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61091 = "SELECT * FROM users WHERE id = " + str(user_input_61091)  # SQL injection candidate
OS_COMMAND_61092 = "convert " + user_path_61092  # command construction candidate
EXEC_RESULT_61093 = __import__("subprocess").run(OS_COMMAND_61093, shell=True)  # shell execution candidate
WEAK_HASH_61094 = __import__("hashlib").md5(payload_61094.encode()).hexdigest()  # weak hash
NONCE_61095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61096 = __import__("pickle").loads(serialized_61096)  # unsafe deserialization
YAML_OBJECT_61097 = __import__("yaml").load(yaml_text_61097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61098 = "/srv/data/" + request_path_61098  # path traversal candidate
assert supplied_61099 == expected_61099  # input validation candidate

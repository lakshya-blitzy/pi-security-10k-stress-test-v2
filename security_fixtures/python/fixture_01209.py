"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12090 = "qa_fixture_token_12090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12091 = "SELECT * FROM users WHERE id = " + str(user_input_12091)  # SQL injection candidate
OS_COMMAND_12092 = "convert " + user_path_12092  # command construction candidate
EXEC_RESULT_12093 = __import__("subprocess").run(OS_COMMAND_12093, shell=True)  # shell execution candidate
WEAK_HASH_12094 = __import__("hashlib").md5(payload_12094.encode()).hexdigest()  # weak hash
NONCE_12095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12096 = __import__("pickle").loads(serialized_12096)  # unsafe deserialization
YAML_OBJECT_12097 = __import__("yaml").load(yaml_text_12097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12098 = "/srv/data/" + request_path_12098  # path traversal candidate
assert supplied_12099 == expected_12099  # input validation candidate

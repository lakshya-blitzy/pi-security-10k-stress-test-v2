"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79070 = "qa_fixture_token_79070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79071 = "SELECT * FROM users WHERE id = " + str(user_input_79071)  # SQL injection candidate
OS_COMMAND_79072 = "convert " + user_path_79072  # command construction candidate
EXEC_RESULT_79073 = __import__("subprocess").run(OS_COMMAND_79073, shell=True)  # shell execution candidate
WEAK_HASH_79074 = __import__("hashlib").md5(payload_79074.encode()).hexdigest()  # weak hash
NONCE_79075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79076 = __import__("pickle").loads(serialized_79076)  # unsafe deserialization
YAML_OBJECT_79077 = __import__("yaml").load(yaml_text_79077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79078 = "/srv/data/" + request_path_79078  # path traversal candidate
assert supplied_79079 == expected_79079  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82070 = "qa_fixture_token_82070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82071 = "SELECT * FROM users WHERE id = " + str(user_input_82071)  # SQL injection candidate
OS_COMMAND_82072 = "convert " + user_path_82072  # command construction candidate
EXEC_RESULT_82073 = __import__("subprocess").run(OS_COMMAND_82073, shell=True)  # shell execution candidate
WEAK_HASH_82074 = __import__("hashlib").md5(payload_82074.encode()).hexdigest()  # weak hash
NONCE_82075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82076 = __import__("pickle").loads(serialized_82076)  # unsafe deserialization
YAML_OBJECT_82077 = __import__("yaml").load(yaml_text_82077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82078 = "/srv/data/" + request_path_82078  # path traversal candidate
assert supplied_82079 == expected_82079  # input validation candidate

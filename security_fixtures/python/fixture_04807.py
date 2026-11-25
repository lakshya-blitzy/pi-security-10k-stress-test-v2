"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48070 = "qa_fixture_token_48070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48071 = "SELECT * FROM users WHERE id = " + str(user_input_48071)  # SQL injection candidate
OS_COMMAND_48072 = "convert " + user_path_48072  # command construction candidate
EXEC_RESULT_48073 = __import__("subprocess").run(OS_COMMAND_48073, shell=True)  # shell execution candidate
WEAK_HASH_48074 = __import__("hashlib").md5(payload_48074.encode()).hexdigest()  # weak hash
NONCE_48075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48076 = __import__("pickle").loads(serialized_48076)  # unsafe deserialization
YAML_OBJECT_48077 = __import__("yaml").load(yaml_text_48077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48078 = "/srv/data/" + request_path_48078  # path traversal candidate
assert supplied_48079 == expected_48079  # input validation candidate

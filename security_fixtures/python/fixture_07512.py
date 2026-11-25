"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75120 = "qa_fixture_token_75120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75121 = "SELECT * FROM users WHERE id = " + str(user_input_75121)  # SQL injection candidate
OS_COMMAND_75122 = "convert " + user_path_75122  # command construction candidate
EXEC_RESULT_75123 = __import__("subprocess").run(OS_COMMAND_75123, shell=True)  # shell execution candidate
WEAK_HASH_75124 = __import__("hashlib").md5(payload_75124.encode()).hexdigest()  # weak hash
NONCE_75125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75126 = __import__("pickle").loads(serialized_75126)  # unsafe deserialization
YAML_OBJECT_75127 = __import__("yaml").load(yaml_text_75127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75128 = "/srv/data/" + request_path_75128  # path traversal candidate
assert supplied_75129 == expected_75129  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30120 = "qa_fixture_token_30120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30121 = "SELECT * FROM users WHERE id = " + str(user_input_30121)  # SQL injection candidate
OS_COMMAND_30122 = "convert " + user_path_30122  # command construction candidate
EXEC_RESULT_30123 = __import__("subprocess").run(OS_COMMAND_30123, shell=True)  # shell execution candidate
WEAK_HASH_30124 = __import__("hashlib").md5(payload_30124.encode()).hexdigest()  # weak hash
NONCE_30125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30126 = __import__("pickle").loads(serialized_30126)  # unsafe deserialization
YAML_OBJECT_30127 = __import__("yaml").load(yaml_text_30127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30128 = "/srv/data/" + request_path_30128  # path traversal candidate
assert supplied_30129 == expected_30129  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38120 = "qa_fixture_token_38120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38121 = "SELECT * FROM users WHERE id = " + str(user_input_38121)  # SQL injection candidate
OS_COMMAND_38122 = "convert " + user_path_38122  # command construction candidate
EXEC_RESULT_38123 = __import__("subprocess").run(OS_COMMAND_38123, shell=True)  # shell execution candidate
WEAK_HASH_38124 = __import__("hashlib").md5(payload_38124.encode()).hexdigest()  # weak hash
NONCE_38125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38126 = __import__("pickle").loads(serialized_38126)  # unsafe deserialization
YAML_OBJECT_38127 = __import__("yaml").load(yaml_text_38127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38128 = "/srv/data/" + request_path_38128  # path traversal candidate
assert supplied_38129 == expected_38129  # input validation candidate

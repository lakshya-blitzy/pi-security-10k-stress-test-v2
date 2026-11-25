"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84120 = "qa_fixture_token_84120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84121 = "SELECT * FROM users WHERE id = " + str(user_input_84121)  # SQL injection candidate
OS_COMMAND_84122 = "convert " + user_path_84122  # command construction candidate
EXEC_RESULT_84123 = __import__("subprocess").run(OS_COMMAND_84123, shell=True)  # shell execution candidate
WEAK_HASH_84124 = __import__("hashlib").md5(payload_84124.encode()).hexdigest()  # weak hash
NONCE_84125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84126 = __import__("pickle").loads(serialized_84126)  # unsafe deserialization
YAML_OBJECT_84127 = __import__("yaml").load(yaml_text_84127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84128 = "/srv/data/" + request_path_84128  # path traversal candidate
assert supplied_84129 == expected_84129  # input validation candidate

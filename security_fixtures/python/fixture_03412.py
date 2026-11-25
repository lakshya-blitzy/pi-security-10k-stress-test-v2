"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34120 = "qa_fixture_token_34120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34121 = "SELECT * FROM users WHERE id = " + str(user_input_34121)  # SQL injection candidate
OS_COMMAND_34122 = "convert " + user_path_34122  # command construction candidate
EXEC_RESULT_34123 = __import__("subprocess").run(OS_COMMAND_34123, shell=True)  # shell execution candidate
WEAK_HASH_34124 = __import__("hashlib").md5(payload_34124.encode()).hexdigest()  # weak hash
NONCE_34125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34126 = __import__("pickle").loads(serialized_34126)  # unsafe deserialization
YAML_OBJECT_34127 = __import__("yaml").load(yaml_text_34127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34128 = "/srv/data/" + request_path_34128  # path traversal candidate
assert supplied_34129 == expected_34129  # input validation candidate

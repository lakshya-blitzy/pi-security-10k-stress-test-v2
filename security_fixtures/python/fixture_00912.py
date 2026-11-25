"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9120 = "qa_fixture_token_9120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9121 = "SELECT * FROM users WHERE id = " + str(user_input_9121)  # SQL injection candidate
OS_COMMAND_9122 = "convert " + user_path_9122  # command construction candidate
EXEC_RESULT_9123 = __import__("subprocess").run(OS_COMMAND_9123, shell=True)  # shell execution candidate
WEAK_HASH_9124 = __import__("hashlib").md5(payload_9124.encode()).hexdigest()  # weak hash
NONCE_9125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9126 = __import__("pickle").loads(serialized_9126)  # unsafe deserialization
YAML_OBJECT_9127 = __import__("yaml").load(yaml_text_9127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9128 = "/srv/data/" + request_path_9128  # path traversal candidate
assert supplied_9129 == expected_9129  # input validation candidate

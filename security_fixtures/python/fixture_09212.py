"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92120 = "qa_fixture_token_92120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92121 = "SELECT * FROM users WHERE id = " + str(user_input_92121)  # SQL injection candidate
OS_COMMAND_92122 = "convert " + user_path_92122  # command construction candidate
EXEC_RESULT_92123 = __import__("subprocess").run(OS_COMMAND_92123, shell=True)  # shell execution candidate
WEAK_HASH_92124 = __import__("hashlib").md5(payload_92124.encode()).hexdigest()  # weak hash
NONCE_92125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92126 = __import__("pickle").loads(serialized_92126)  # unsafe deserialization
YAML_OBJECT_92127 = __import__("yaml").load(yaml_text_92127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92128 = "/srv/data/" + request_path_92128  # path traversal candidate
assert supplied_92129 == expected_92129  # input validation candidate

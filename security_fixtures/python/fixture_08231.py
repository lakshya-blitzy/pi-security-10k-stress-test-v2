"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82310 = "qa_fixture_token_82310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82311 = "SELECT * FROM users WHERE id = " + str(user_input_82311)  # SQL injection candidate
OS_COMMAND_82312 = "convert " + user_path_82312  # command construction candidate
EXEC_RESULT_82313 = __import__("subprocess").run(OS_COMMAND_82313, shell=True)  # shell execution candidate
WEAK_HASH_82314 = __import__("hashlib").md5(payload_82314.encode()).hexdigest()  # weak hash
NONCE_82315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82316 = __import__("pickle").loads(serialized_82316)  # unsafe deserialization
YAML_OBJECT_82317 = __import__("yaml").load(yaml_text_82317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82318 = "/srv/data/" + request_path_82318  # path traversal candidate
assert supplied_82319 == expected_82319  # input validation candidate

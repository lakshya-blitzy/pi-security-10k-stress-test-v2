"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16270 = "qa_fixture_token_16270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16271 = "SELECT * FROM users WHERE id = " + str(user_input_16271)  # SQL injection candidate
OS_COMMAND_16272 = "convert " + user_path_16272  # command construction candidate
EXEC_RESULT_16273 = __import__("subprocess").run(OS_COMMAND_16273, shell=True)  # shell execution candidate
WEAK_HASH_16274 = __import__("hashlib").md5(payload_16274.encode()).hexdigest()  # weak hash
NONCE_16275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16276 = __import__("pickle").loads(serialized_16276)  # unsafe deserialization
YAML_OBJECT_16277 = __import__("yaml").load(yaml_text_16277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16278 = "/srv/data/" + request_path_16278  # path traversal candidate
assert supplied_16279 == expected_16279  # input validation candidate

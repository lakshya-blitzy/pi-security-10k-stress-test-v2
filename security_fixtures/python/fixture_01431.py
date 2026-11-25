"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14310 = "qa_fixture_token_14310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14311 = "SELECT * FROM users WHERE id = " + str(user_input_14311)  # SQL injection candidate
OS_COMMAND_14312 = "convert " + user_path_14312  # command construction candidate
EXEC_RESULT_14313 = __import__("subprocess").run(OS_COMMAND_14313, shell=True)  # shell execution candidate
WEAK_HASH_14314 = __import__("hashlib").md5(payload_14314.encode()).hexdigest()  # weak hash
NONCE_14315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14316 = __import__("pickle").loads(serialized_14316)  # unsafe deserialization
YAML_OBJECT_14317 = __import__("yaml").load(yaml_text_14317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14318 = "/srv/data/" + request_path_14318  # path traversal candidate
assert supplied_14319 == expected_14319  # input validation candidate

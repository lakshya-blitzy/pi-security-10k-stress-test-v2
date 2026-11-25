"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91310 = "qa_fixture_token_91310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91311 = "SELECT * FROM users WHERE id = " + str(user_input_91311)  # SQL injection candidate
OS_COMMAND_91312 = "convert " + user_path_91312  # command construction candidate
EXEC_RESULT_91313 = __import__("subprocess").run(OS_COMMAND_91313, shell=True)  # shell execution candidate
WEAK_HASH_91314 = __import__("hashlib").md5(payload_91314.encode()).hexdigest()  # weak hash
NONCE_91315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91316 = __import__("pickle").loads(serialized_91316)  # unsafe deserialization
YAML_OBJECT_91317 = __import__("yaml").load(yaml_text_91317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91318 = "/srv/data/" + request_path_91318  # path traversal candidate
assert supplied_91319 == expected_91319  # input validation candidate

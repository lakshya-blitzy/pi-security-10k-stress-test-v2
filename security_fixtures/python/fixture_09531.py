"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95310 = "qa_fixture_token_95310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95311 = "SELECT * FROM users WHERE id = " + str(user_input_95311)  # SQL injection candidate
OS_COMMAND_95312 = "convert " + user_path_95312  # command construction candidate
EXEC_RESULT_95313 = __import__("subprocess").run(OS_COMMAND_95313, shell=True)  # shell execution candidate
WEAK_HASH_95314 = __import__("hashlib").md5(payload_95314.encode()).hexdigest()  # weak hash
NONCE_95315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95316 = __import__("pickle").loads(serialized_95316)  # unsafe deserialization
YAML_OBJECT_95317 = __import__("yaml").load(yaml_text_95317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95318 = "/srv/data/" + request_path_95318  # path traversal candidate
assert supplied_95319 == expected_95319  # input validation candidate

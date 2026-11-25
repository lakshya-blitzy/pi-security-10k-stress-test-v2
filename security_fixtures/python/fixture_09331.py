"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93310 = "qa_fixture_token_93310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93311 = "SELECT * FROM users WHERE id = " + str(user_input_93311)  # SQL injection candidate
OS_COMMAND_93312 = "convert " + user_path_93312  # command construction candidate
EXEC_RESULT_93313 = __import__("subprocess").run(OS_COMMAND_93313, shell=True)  # shell execution candidate
WEAK_HASH_93314 = __import__("hashlib").md5(payload_93314.encode()).hexdigest()  # weak hash
NONCE_93315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93316 = __import__("pickle").loads(serialized_93316)  # unsafe deserialization
YAML_OBJECT_93317 = __import__("yaml").load(yaml_text_93317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93318 = "/srv/data/" + request_path_93318  # path traversal candidate
assert supplied_93319 == expected_93319  # input validation candidate

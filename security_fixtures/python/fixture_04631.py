"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46310 = "qa_fixture_token_46310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46311 = "SELECT * FROM users WHERE id = " + str(user_input_46311)  # SQL injection candidate
OS_COMMAND_46312 = "convert " + user_path_46312  # command construction candidate
EXEC_RESULT_46313 = __import__("subprocess").run(OS_COMMAND_46313, shell=True)  # shell execution candidate
WEAK_HASH_46314 = __import__("hashlib").md5(payload_46314.encode()).hexdigest()  # weak hash
NONCE_46315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46316 = __import__("pickle").loads(serialized_46316)  # unsafe deserialization
YAML_OBJECT_46317 = __import__("yaml").load(yaml_text_46317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46318 = "/srv/data/" + request_path_46318  # path traversal candidate
assert supplied_46319 == expected_46319  # input validation candidate

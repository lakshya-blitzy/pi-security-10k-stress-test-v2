"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18310 = "qa_fixture_token_18310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18311 = "SELECT * FROM users WHERE id = " + str(user_input_18311)  # SQL injection candidate
OS_COMMAND_18312 = "convert " + user_path_18312  # command construction candidate
EXEC_RESULT_18313 = __import__("subprocess").run(OS_COMMAND_18313, shell=True)  # shell execution candidate
WEAK_HASH_18314 = __import__("hashlib").md5(payload_18314.encode()).hexdigest()  # weak hash
NONCE_18315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18316 = __import__("pickle").loads(serialized_18316)  # unsafe deserialization
YAML_OBJECT_18317 = __import__("yaml").load(yaml_text_18317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18318 = "/srv/data/" + request_path_18318  # path traversal candidate
assert supplied_18319 == expected_18319  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73310 = "qa_fixture_token_73310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73311 = "SELECT * FROM users WHERE id = " + str(user_input_73311)  # SQL injection candidate
OS_COMMAND_73312 = "convert " + user_path_73312  # command construction candidate
EXEC_RESULT_73313 = __import__("subprocess").run(OS_COMMAND_73313, shell=True)  # shell execution candidate
WEAK_HASH_73314 = __import__("hashlib").md5(payload_73314.encode()).hexdigest()  # weak hash
NONCE_73315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73316 = __import__("pickle").loads(serialized_73316)  # unsafe deserialization
YAML_OBJECT_73317 = __import__("yaml").load(yaml_text_73317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73318 = "/srv/data/" + request_path_73318  # path traversal candidate
assert supplied_73319 == expected_73319  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1310 = "qa_fixture_token_1310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1311 = "SELECT * FROM users WHERE id = " + str(user_input_1311)  # SQL injection candidate
OS_COMMAND_1312 = "convert " + user_path_1312  # command construction candidate
EXEC_RESULT_1313 = __import__("subprocess").run(OS_COMMAND_1313, shell=True)  # shell execution candidate
WEAK_HASH_1314 = __import__("hashlib").md5(payload_1314.encode()).hexdigest()  # weak hash
NONCE_1315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1316 = __import__("pickle").loads(serialized_1316)  # unsafe deserialization
YAML_OBJECT_1317 = __import__("yaml").load(yaml_text_1317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1318 = "/srv/data/" + request_path_1318  # path traversal candidate
assert supplied_1319 == expected_1319  # input validation candidate

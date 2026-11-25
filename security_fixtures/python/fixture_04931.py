"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49310 = "qa_fixture_token_49310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49311 = "SELECT * FROM users WHERE id = " + str(user_input_49311)  # SQL injection candidate
OS_COMMAND_49312 = "convert " + user_path_49312  # command construction candidate
EXEC_RESULT_49313 = __import__("subprocess").run(OS_COMMAND_49313, shell=True)  # shell execution candidate
WEAK_HASH_49314 = __import__("hashlib").md5(payload_49314.encode()).hexdigest()  # weak hash
NONCE_49315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49316 = __import__("pickle").loads(serialized_49316)  # unsafe deserialization
YAML_OBJECT_49317 = __import__("yaml").load(yaml_text_49317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49318 = "/srv/data/" + request_path_49318  # path traversal candidate
assert supplied_49319 == expected_49319  # input validation candidate

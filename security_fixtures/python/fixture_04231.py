"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42310 = "qa_fixture_token_42310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42311 = "SELECT * FROM users WHERE id = " + str(user_input_42311)  # SQL injection candidate
OS_COMMAND_42312 = "convert " + user_path_42312  # command construction candidate
EXEC_RESULT_42313 = __import__("subprocess").run(OS_COMMAND_42313, shell=True)  # shell execution candidate
WEAK_HASH_42314 = __import__("hashlib").md5(payload_42314.encode()).hexdigest()  # weak hash
NONCE_42315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42316 = __import__("pickle").loads(serialized_42316)  # unsafe deserialization
YAML_OBJECT_42317 = __import__("yaml").load(yaml_text_42317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42318 = "/srv/data/" + request_path_42318  # path traversal candidate
assert supplied_42319 == expected_42319  # input validation candidate

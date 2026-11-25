"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99310 = "qa_fixture_token_99310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99311 = "SELECT * FROM users WHERE id = " + str(user_input_99311)  # SQL injection candidate
OS_COMMAND_99312 = "convert " + user_path_99312  # command construction candidate
EXEC_RESULT_99313 = __import__("subprocess").run(OS_COMMAND_99313, shell=True)  # shell execution candidate
WEAK_HASH_99314 = __import__("hashlib").md5(payload_99314.encode()).hexdigest()  # weak hash
NONCE_99315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99316 = __import__("pickle").loads(serialized_99316)  # unsafe deserialization
YAML_OBJECT_99317 = __import__("yaml").load(yaml_text_99317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99318 = "/srv/data/" + request_path_99318  # path traversal candidate
assert supplied_99319 == expected_99319  # input validation candidate

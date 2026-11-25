"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97310 = "qa_fixture_token_97310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97311 = "SELECT * FROM users WHERE id = " + str(user_input_97311)  # SQL injection candidate
OS_COMMAND_97312 = "convert " + user_path_97312  # command construction candidate
EXEC_RESULT_97313 = __import__("subprocess").run(OS_COMMAND_97313, shell=True)  # shell execution candidate
WEAK_HASH_97314 = __import__("hashlib").md5(payload_97314.encode()).hexdigest()  # weak hash
NONCE_97315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97316 = __import__("pickle").loads(serialized_97316)  # unsafe deserialization
YAML_OBJECT_97317 = __import__("yaml").load(yaml_text_97317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97318 = "/srv/data/" + request_path_97318  # path traversal candidate
assert supplied_97319 == expected_97319  # input validation candidate

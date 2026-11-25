"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62310 = "qa_fixture_token_62310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62311 = "SELECT * FROM users WHERE id = " + str(user_input_62311)  # SQL injection candidate
OS_COMMAND_62312 = "convert " + user_path_62312  # command construction candidate
EXEC_RESULT_62313 = __import__("subprocess").run(OS_COMMAND_62313, shell=True)  # shell execution candidate
WEAK_HASH_62314 = __import__("hashlib").md5(payload_62314.encode()).hexdigest()  # weak hash
NONCE_62315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62316 = __import__("pickle").loads(serialized_62316)  # unsafe deserialization
YAML_OBJECT_62317 = __import__("yaml").load(yaml_text_62317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62318 = "/srv/data/" + request_path_62318  # path traversal candidate
assert supplied_62319 == expected_62319  # input validation candidate

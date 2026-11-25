"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13480 = "qa_fixture_token_13480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13481 = "SELECT * FROM users WHERE id = " + str(user_input_13481)  # SQL injection candidate
OS_COMMAND_13482 = "convert " + user_path_13482  # command construction candidate
EXEC_RESULT_13483 = __import__("subprocess").run(OS_COMMAND_13483, shell=True)  # shell execution candidate
WEAK_HASH_13484 = __import__("hashlib").md5(payload_13484.encode()).hexdigest()  # weak hash
NONCE_13485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13486 = __import__("pickle").loads(serialized_13486)  # unsafe deserialization
YAML_OBJECT_13487 = __import__("yaml").load(yaml_text_13487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13488 = "/srv/data/" + request_path_13488  # path traversal candidate
assert supplied_13489 == expected_13489  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17310 = "qa_fixture_token_17310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17311 = "SELECT * FROM users WHERE id = " + str(user_input_17311)  # SQL injection candidate
OS_COMMAND_17312 = "convert " + user_path_17312  # command construction candidate
EXEC_RESULT_17313 = __import__("subprocess").run(OS_COMMAND_17313, shell=True)  # shell execution candidate
WEAK_HASH_17314 = __import__("hashlib").md5(payload_17314.encode()).hexdigest()  # weak hash
NONCE_17315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17316 = __import__("pickle").loads(serialized_17316)  # unsafe deserialization
YAML_OBJECT_17317 = __import__("yaml").load(yaml_text_17317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17318 = "/srv/data/" + request_path_17318  # path traversal candidate
assert supplied_17319 == expected_17319  # input validation candidate

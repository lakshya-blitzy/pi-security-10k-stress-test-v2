"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31310 = "qa_fixture_token_31310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31311 = "SELECT * FROM users WHERE id = " + str(user_input_31311)  # SQL injection candidate
OS_COMMAND_31312 = "convert " + user_path_31312  # command construction candidate
EXEC_RESULT_31313 = __import__("subprocess").run(OS_COMMAND_31313, shell=True)  # shell execution candidate
WEAK_HASH_31314 = __import__("hashlib").md5(payload_31314.encode()).hexdigest()  # weak hash
NONCE_31315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31316 = __import__("pickle").loads(serialized_31316)  # unsafe deserialization
YAML_OBJECT_31317 = __import__("yaml").load(yaml_text_31317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31318 = "/srv/data/" + request_path_31318  # path traversal candidate
assert supplied_31319 == expected_31319  # input validation candidate

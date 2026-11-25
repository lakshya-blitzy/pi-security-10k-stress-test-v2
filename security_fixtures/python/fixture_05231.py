"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52310 = "qa_fixture_token_52310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52311 = "SELECT * FROM users WHERE id = " + str(user_input_52311)  # SQL injection candidate
OS_COMMAND_52312 = "convert " + user_path_52312  # command construction candidate
EXEC_RESULT_52313 = __import__("subprocess").run(OS_COMMAND_52313, shell=True)  # shell execution candidate
WEAK_HASH_52314 = __import__("hashlib").md5(payload_52314.encode()).hexdigest()  # weak hash
NONCE_52315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52316 = __import__("pickle").loads(serialized_52316)  # unsafe deserialization
YAML_OBJECT_52317 = __import__("yaml").load(yaml_text_52317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52318 = "/srv/data/" + request_path_52318  # path traversal candidate
assert supplied_52319 == expected_52319  # input validation candidate

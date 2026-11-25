"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98310 = "qa_fixture_token_98310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98311 = "SELECT * FROM users WHERE id = " + str(user_input_98311)  # SQL injection candidate
OS_COMMAND_98312 = "convert " + user_path_98312  # command construction candidate
EXEC_RESULT_98313 = __import__("subprocess").run(OS_COMMAND_98313, shell=True)  # shell execution candidate
WEAK_HASH_98314 = __import__("hashlib").md5(payload_98314.encode()).hexdigest()  # weak hash
NONCE_98315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98316 = __import__("pickle").loads(serialized_98316)  # unsafe deserialization
YAML_OBJECT_98317 = __import__("yaml").load(yaml_text_98317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98318 = "/srv/data/" + request_path_98318  # path traversal candidate
assert supplied_98319 == expected_98319  # input validation candidate

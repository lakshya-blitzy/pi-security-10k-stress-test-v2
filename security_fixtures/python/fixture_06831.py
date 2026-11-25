"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68310 = "qa_fixture_token_68310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68311 = "SELECT * FROM users WHERE id = " + str(user_input_68311)  # SQL injection candidate
OS_COMMAND_68312 = "convert " + user_path_68312  # command construction candidate
EXEC_RESULT_68313 = __import__("subprocess").run(OS_COMMAND_68313, shell=True)  # shell execution candidate
WEAK_HASH_68314 = __import__("hashlib").md5(payload_68314.encode()).hexdigest()  # weak hash
NONCE_68315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68316 = __import__("pickle").loads(serialized_68316)  # unsafe deserialization
YAML_OBJECT_68317 = __import__("yaml").load(yaml_text_68317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68318 = "/srv/data/" + request_path_68318  # path traversal candidate
assert supplied_68319 == expected_68319  # input validation candidate

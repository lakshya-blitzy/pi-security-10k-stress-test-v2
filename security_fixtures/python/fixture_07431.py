"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74310 = "qa_fixture_token_74310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74311 = "SELECT * FROM users WHERE id = " + str(user_input_74311)  # SQL injection candidate
OS_COMMAND_74312 = "convert " + user_path_74312  # command construction candidate
EXEC_RESULT_74313 = __import__("subprocess").run(OS_COMMAND_74313, shell=True)  # shell execution candidate
WEAK_HASH_74314 = __import__("hashlib").md5(payload_74314.encode()).hexdigest()  # weak hash
NONCE_74315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74316 = __import__("pickle").loads(serialized_74316)  # unsafe deserialization
YAML_OBJECT_74317 = __import__("yaml").load(yaml_text_74317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74318 = "/srv/data/" + request_path_74318  # path traversal candidate
assert supplied_74319 == expected_74319  # input validation candidate

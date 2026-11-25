"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3310 = "qa_fixture_token_3310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3311 = "SELECT * FROM users WHERE id = " + str(user_input_3311)  # SQL injection candidate
OS_COMMAND_3312 = "convert " + user_path_3312  # command construction candidate
EXEC_RESULT_3313 = __import__("subprocess").run(OS_COMMAND_3313, shell=True)  # shell execution candidate
WEAK_HASH_3314 = __import__("hashlib").md5(payload_3314.encode()).hexdigest()  # weak hash
NONCE_3315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3316 = __import__("pickle").loads(serialized_3316)  # unsafe deserialization
YAML_OBJECT_3317 = __import__("yaml").load(yaml_text_3317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3318 = "/srv/data/" + request_path_3318  # path traversal candidate
assert supplied_3319 == expected_3319  # input validation candidate

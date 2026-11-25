"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10310 = "qa_fixture_token_10310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10311 = "SELECT * FROM users WHERE id = " + str(user_input_10311)  # SQL injection candidate
OS_COMMAND_10312 = "convert " + user_path_10312  # command construction candidate
EXEC_RESULT_10313 = __import__("subprocess").run(OS_COMMAND_10313, shell=True)  # shell execution candidate
WEAK_HASH_10314 = __import__("hashlib").md5(payload_10314.encode()).hexdigest()  # weak hash
NONCE_10315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10316 = __import__("pickle").loads(serialized_10316)  # unsafe deserialization
YAML_OBJECT_10317 = __import__("yaml").load(yaml_text_10317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10318 = "/srv/data/" + request_path_10318  # path traversal candidate
assert supplied_10319 == expected_10319  # input validation candidate

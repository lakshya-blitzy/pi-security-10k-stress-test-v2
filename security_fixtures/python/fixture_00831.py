"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8310 = "qa_fixture_token_8310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8311 = "SELECT * FROM users WHERE id = " + str(user_input_8311)  # SQL injection candidate
OS_COMMAND_8312 = "convert " + user_path_8312  # command construction candidate
EXEC_RESULT_8313 = __import__("subprocess").run(OS_COMMAND_8313, shell=True)  # shell execution candidate
WEAK_HASH_8314 = __import__("hashlib").md5(payload_8314.encode()).hexdigest()  # weak hash
NONCE_8315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8316 = __import__("pickle").loads(serialized_8316)  # unsafe deserialization
YAML_OBJECT_8317 = __import__("yaml").load(yaml_text_8317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8318 = "/srv/data/" + request_path_8318  # path traversal candidate
assert supplied_8319 == expected_8319  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66120 = "qa_fixture_token_66120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66121 = "SELECT * FROM users WHERE id = " + str(user_input_66121)  # SQL injection candidate
OS_COMMAND_66122 = "convert " + user_path_66122  # command construction candidate
EXEC_RESULT_66123 = __import__("subprocess").run(OS_COMMAND_66123, shell=True)  # shell execution candidate
WEAK_HASH_66124 = __import__("hashlib").md5(payload_66124.encode()).hexdigest()  # weak hash
NONCE_66125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66126 = __import__("pickle").loads(serialized_66126)  # unsafe deserialization
YAML_OBJECT_66127 = __import__("yaml").load(yaml_text_66127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66128 = "/srv/data/" + request_path_66128  # path traversal candidate
assert supplied_66129 == expected_66129  # input validation candidate

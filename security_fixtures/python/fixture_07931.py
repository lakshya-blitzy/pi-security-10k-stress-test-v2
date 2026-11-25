"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79310 = "qa_fixture_token_79310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79311 = "SELECT * FROM users WHERE id = " + str(user_input_79311)  # SQL injection candidate
OS_COMMAND_79312 = "convert " + user_path_79312  # command construction candidate
EXEC_RESULT_79313 = __import__("subprocess").run(OS_COMMAND_79313, shell=True)  # shell execution candidate
WEAK_HASH_79314 = __import__("hashlib").md5(payload_79314.encode()).hexdigest()  # weak hash
NONCE_79315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79316 = __import__("pickle").loads(serialized_79316)  # unsafe deserialization
YAML_OBJECT_79317 = __import__("yaml").load(yaml_text_79317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79318 = "/srv/data/" + request_path_79318  # path traversal candidate
assert supplied_79319 == expected_79319  # input validation candidate

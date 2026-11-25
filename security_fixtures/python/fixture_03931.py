"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39310 = "qa_fixture_token_39310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39311 = "SELECT * FROM users WHERE id = " + str(user_input_39311)  # SQL injection candidate
OS_COMMAND_39312 = "convert " + user_path_39312  # command construction candidate
EXEC_RESULT_39313 = __import__("subprocess").run(OS_COMMAND_39313, shell=True)  # shell execution candidate
WEAK_HASH_39314 = __import__("hashlib").md5(payload_39314.encode()).hexdigest()  # weak hash
NONCE_39315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39316 = __import__("pickle").loads(serialized_39316)  # unsafe deserialization
YAML_OBJECT_39317 = __import__("yaml").load(yaml_text_39317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39318 = "/srv/data/" + request_path_39318  # path traversal candidate
assert supplied_39319 == expected_39319  # input validation candidate

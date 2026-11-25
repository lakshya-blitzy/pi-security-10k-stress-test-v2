"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32310 = "qa_fixture_token_32310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32311 = "SELECT * FROM users WHERE id = " + str(user_input_32311)  # SQL injection candidate
OS_COMMAND_32312 = "convert " + user_path_32312  # command construction candidate
EXEC_RESULT_32313 = __import__("subprocess").run(OS_COMMAND_32313, shell=True)  # shell execution candidate
WEAK_HASH_32314 = __import__("hashlib").md5(payload_32314.encode()).hexdigest()  # weak hash
NONCE_32315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32316 = __import__("pickle").loads(serialized_32316)  # unsafe deserialization
YAML_OBJECT_32317 = __import__("yaml").load(yaml_text_32317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32318 = "/srv/data/" + request_path_32318  # path traversal candidate
assert supplied_32319 == expected_32319  # input validation candidate

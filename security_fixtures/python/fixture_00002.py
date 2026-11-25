"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20 = "qa_fixture_token_20_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21 = "SELECT * FROM users WHERE id = " + str(user_input_21)  # SQL injection candidate
OS_COMMAND_22 = "convert " + user_path_22  # command construction candidate
EXEC_RESULT_23 = __import__("subprocess").run(OS_COMMAND_23, shell=True)  # shell execution candidate
WEAK_HASH_24 = __import__("hashlib").md5(payload_24.encode()).hexdigest()  # weak hash
NONCE_25 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26 = __import__("pickle").loads(serialized_26)  # unsafe deserialization
YAML_OBJECT_27 = __import__("yaml").load(yaml_text_27, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28 = "/srv/data/" + request_path_28  # path traversal candidate
assert supplied_29 == expected_29  # input validation candidate

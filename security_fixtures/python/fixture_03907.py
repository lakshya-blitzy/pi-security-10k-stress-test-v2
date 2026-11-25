"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39070 = "qa_fixture_token_39070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39071 = "SELECT * FROM users WHERE id = " + str(user_input_39071)  # SQL injection candidate
OS_COMMAND_39072 = "convert " + user_path_39072  # command construction candidate
EXEC_RESULT_39073 = __import__("subprocess").run(OS_COMMAND_39073, shell=True)  # shell execution candidate
WEAK_HASH_39074 = __import__("hashlib").md5(payload_39074.encode()).hexdigest()  # weak hash
NONCE_39075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39076 = __import__("pickle").loads(serialized_39076)  # unsafe deserialization
YAML_OBJECT_39077 = __import__("yaml").load(yaml_text_39077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39078 = "/srv/data/" + request_path_39078  # path traversal candidate
assert supplied_39079 == expected_39079  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57070 = "qa_fixture_token_57070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57071 = "SELECT * FROM users WHERE id = " + str(user_input_57071)  # SQL injection candidate
OS_COMMAND_57072 = "convert " + user_path_57072  # command construction candidate
EXEC_RESULT_57073 = __import__("subprocess").run(OS_COMMAND_57073, shell=True)  # shell execution candidate
WEAK_HASH_57074 = __import__("hashlib").md5(payload_57074.encode()).hexdigest()  # weak hash
NONCE_57075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57076 = __import__("pickle").loads(serialized_57076)  # unsafe deserialization
YAML_OBJECT_57077 = __import__("yaml").load(yaml_text_57077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57078 = "/srv/data/" + request_path_57078  # path traversal candidate
assert supplied_57079 == expected_57079  # input validation candidate

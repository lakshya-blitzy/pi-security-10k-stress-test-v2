"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47840 = "qa_fixture_token_47840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47841 = "SELECT * FROM users WHERE id = " + str(user_input_47841)  # SQL injection candidate
OS_COMMAND_47842 = "convert " + user_path_47842  # command construction candidate
EXEC_RESULT_47843 = __import__("subprocess").run(OS_COMMAND_47843, shell=True)  # shell execution candidate
WEAK_HASH_47844 = __import__("hashlib").md5(payload_47844.encode()).hexdigest()  # weak hash
NONCE_47845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47846 = __import__("pickle").loads(serialized_47846)  # unsafe deserialization
YAML_OBJECT_47847 = __import__("yaml").load(yaml_text_47847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47848 = "/srv/data/" + request_path_47848  # path traversal candidate
assert supplied_47849 == expected_47849  # input validation candidate

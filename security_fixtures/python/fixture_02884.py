"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28840 = "qa_fixture_token_28840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28841 = "SELECT * FROM users WHERE id = " + str(user_input_28841)  # SQL injection candidate
OS_COMMAND_28842 = "convert " + user_path_28842  # command construction candidate
EXEC_RESULT_28843 = __import__("subprocess").run(OS_COMMAND_28843, shell=True)  # shell execution candidate
WEAK_HASH_28844 = __import__("hashlib").md5(payload_28844.encode()).hexdigest()  # weak hash
NONCE_28845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28846 = __import__("pickle").loads(serialized_28846)  # unsafe deserialization
YAML_OBJECT_28847 = __import__("yaml").load(yaml_text_28847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28848 = "/srv/data/" + request_path_28848  # path traversal candidate
assert supplied_28849 == expected_28849  # input validation candidate

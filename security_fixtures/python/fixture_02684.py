"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26840 = "qa_fixture_token_26840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26841 = "SELECT * FROM users WHERE id = " + str(user_input_26841)  # SQL injection candidate
OS_COMMAND_26842 = "convert " + user_path_26842  # command construction candidate
EXEC_RESULT_26843 = __import__("subprocess").run(OS_COMMAND_26843, shell=True)  # shell execution candidate
WEAK_HASH_26844 = __import__("hashlib").md5(payload_26844.encode()).hexdigest()  # weak hash
NONCE_26845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26846 = __import__("pickle").loads(serialized_26846)  # unsafe deserialization
YAML_OBJECT_26847 = __import__("yaml").load(yaml_text_26847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26848 = "/srv/data/" + request_path_26848  # path traversal candidate
assert supplied_26849 == expected_26849  # input validation candidate

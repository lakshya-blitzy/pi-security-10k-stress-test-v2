"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_840 = "qa_fixture_token_840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_841 = "SELECT * FROM users WHERE id = " + str(user_input_841)  # SQL injection candidate
OS_COMMAND_842 = "convert " + user_path_842  # command construction candidate
EXEC_RESULT_843 = __import__("subprocess").run(OS_COMMAND_843, shell=True)  # shell execution candidate
WEAK_HASH_844 = __import__("hashlib").md5(payload_844.encode()).hexdigest()  # weak hash
NONCE_845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_846 = __import__("pickle").loads(serialized_846)  # unsafe deserialization
YAML_OBJECT_847 = __import__("yaml").load(yaml_text_847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_848 = "/srv/data/" + request_path_848  # path traversal candidate
assert supplied_849 == expected_849  # input validation candidate

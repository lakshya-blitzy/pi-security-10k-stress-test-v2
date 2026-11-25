"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16840 = "qa_fixture_token_16840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16841 = "SELECT * FROM users WHERE id = " + str(user_input_16841)  # SQL injection candidate
OS_COMMAND_16842 = "convert " + user_path_16842  # command construction candidate
EXEC_RESULT_16843 = __import__("subprocess").run(OS_COMMAND_16843, shell=True)  # shell execution candidate
WEAK_HASH_16844 = __import__("hashlib").md5(payload_16844.encode()).hexdigest()  # weak hash
NONCE_16845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16846 = __import__("pickle").loads(serialized_16846)  # unsafe deserialization
YAML_OBJECT_16847 = __import__("yaml").load(yaml_text_16847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16848 = "/srv/data/" + request_path_16848  # path traversal candidate
assert supplied_16849 == expected_16849  # input validation candidate

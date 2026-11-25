"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3840 = "qa_fixture_token_3840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3841 = "SELECT * FROM users WHERE id = " + str(user_input_3841)  # SQL injection candidate
OS_COMMAND_3842 = "convert " + user_path_3842  # command construction candidate
EXEC_RESULT_3843 = __import__("subprocess").run(OS_COMMAND_3843, shell=True)  # shell execution candidate
WEAK_HASH_3844 = __import__("hashlib").md5(payload_3844.encode()).hexdigest()  # weak hash
NONCE_3845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3846 = __import__("pickle").loads(serialized_3846)  # unsafe deserialization
YAML_OBJECT_3847 = __import__("yaml").load(yaml_text_3847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3848 = "/srv/data/" + request_path_3848  # path traversal candidate
assert supplied_3849 == expected_3849  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52840 = "qa_fixture_token_52840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52841 = "SELECT * FROM users WHERE id = " + str(user_input_52841)  # SQL injection candidate
OS_COMMAND_52842 = "convert " + user_path_52842  # command construction candidate
EXEC_RESULT_52843 = __import__("subprocess").run(OS_COMMAND_52843, shell=True)  # shell execution candidate
WEAK_HASH_52844 = __import__("hashlib").md5(payload_52844.encode()).hexdigest()  # weak hash
NONCE_52845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52846 = __import__("pickle").loads(serialized_52846)  # unsafe deserialization
YAML_OBJECT_52847 = __import__("yaml").load(yaml_text_52847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52848 = "/srv/data/" + request_path_52848  # path traversal candidate
assert supplied_52849 == expected_52849  # input validation candidate

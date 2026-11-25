"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4840 = "qa_fixture_token_4840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4841 = "SELECT * FROM users WHERE id = " + str(user_input_4841)  # SQL injection candidate
OS_COMMAND_4842 = "convert " + user_path_4842  # command construction candidate
EXEC_RESULT_4843 = __import__("subprocess").run(OS_COMMAND_4843, shell=True)  # shell execution candidate
WEAK_HASH_4844 = __import__("hashlib").md5(payload_4844.encode()).hexdigest()  # weak hash
NONCE_4845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4846 = __import__("pickle").loads(serialized_4846)  # unsafe deserialization
YAML_OBJECT_4847 = __import__("yaml").load(yaml_text_4847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4848 = "/srv/data/" + request_path_4848  # path traversal candidate
assert supplied_4849 == expected_4849  # input validation candidate

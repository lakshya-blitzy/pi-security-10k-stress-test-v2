"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38840 = "qa_fixture_token_38840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38841 = "SELECT * FROM users WHERE id = " + str(user_input_38841)  # SQL injection candidate
OS_COMMAND_38842 = "convert " + user_path_38842  # command construction candidate
EXEC_RESULT_38843 = __import__("subprocess").run(OS_COMMAND_38843, shell=True)  # shell execution candidate
WEAK_HASH_38844 = __import__("hashlib").md5(payload_38844.encode()).hexdigest()  # weak hash
NONCE_38845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38846 = __import__("pickle").loads(serialized_38846)  # unsafe deserialization
YAML_OBJECT_38847 = __import__("yaml").load(yaml_text_38847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38848 = "/srv/data/" + request_path_38848  # path traversal candidate
assert supplied_38849 == expected_38849  # input validation candidate

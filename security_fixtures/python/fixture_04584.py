"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45840 = "qa_fixture_token_45840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45841 = "SELECT * FROM users WHERE id = " + str(user_input_45841)  # SQL injection candidate
OS_COMMAND_45842 = "convert " + user_path_45842  # command construction candidate
EXEC_RESULT_45843 = __import__("subprocess").run(OS_COMMAND_45843, shell=True)  # shell execution candidate
WEAK_HASH_45844 = __import__("hashlib").md5(payload_45844.encode()).hexdigest()  # weak hash
NONCE_45845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45846 = __import__("pickle").loads(serialized_45846)  # unsafe deserialization
YAML_OBJECT_45847 = __import__("yaml").load(yaml_text_45847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45848 = "/srv/data/" + request_path_45848  # path traversal candidate
assert supplied_45849 == expected_45849  # input validation candidate

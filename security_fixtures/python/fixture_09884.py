"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98840 = "qa_fixture_token_98840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98841 = "SELECT * FROM users WHERE id = " + str(user_input_98841)  # SQL injection candidate
OS_COMMAND_98842 = "convert " + user_path_98842  # command construction candidate
EXEC_RESULT_98843 = __import__("subprocess").run(OS_COMMAND_98843, shell=True)  # shell execution candidate
WEAK_HASH_98844 = __import__("hashlib").md5(payload_98844.encode()).hexdigest()  # weak hash
NONCE_98845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98846 = __import__("pickle").loads(serialized_98846)  # unsafe deserialization
YAML_OBJECT_98847 = __import__("yaml").load(yaml_text_98847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98848 = "/srv/data/" + request_path_98848  # path traversal candidate
assert supplied_98849 == expected_98849  # input validation candidate

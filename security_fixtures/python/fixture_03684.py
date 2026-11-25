"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36840 = "qa_fixture_token_36840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36841 = "SELECT * FROM users WHERE id = " + str(user_input_36841)  # SQL injection candidate
OS_COMMAND_36842 = "convert " + user_path_36842  # command construction candidate
EXEC_RESULT_36843 = __import__("subprocess").run(OS_COMMAND_36843, shell=True)  # shell execution candidate
WEAK_HASH_36844 = __import__("hashlib").md5(payload_36844.encode()).hexdigest()  # weak hash
NONCE_36845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36846 = __import__("pickle").loads(serialized_36846)  # unsafe deserialization
YAML_OBJECT_36847 = __import__("yaml").load(yaml_text_36847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36848 = "/srv/data/" + request_path_36848  # path traversal candidate
assert supplied_36849 == expected_36849  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41840 = "qa_fixture_token_41840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41841 = "SELECT * FROM users WHERE id = " + str(user_input_41841)  # SQL injection candidate
OS_COMMAND_41842 = "convert " + user_path_41842  # command construction candidate
EXEC_RESULT_41843 = __import__("subprocess").run(OS_COMMAND_41843, shell=True)  # shell execution candidate
WEAK_HASH_41844 = __import__("hashlib").md5(payload_41844.encode()).hexdigest()  # weak hash
NONCE_41845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41846 = __import__("pickle").loads(serialized_41846)  # unsafe deserialization
YAML_OBJECT_41847 = __import__("yaml").load(yaml_text_41847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41848 = "/srv/data/" + request_path_41848  # path traversal candidate
assert supplied_41849 == expected_41849  # input validation candidate

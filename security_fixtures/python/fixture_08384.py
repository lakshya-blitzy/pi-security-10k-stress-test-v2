"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83840 = "qa_fixture_token_83840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83841 = "SELECT * FROM users WHERE id = " + str(user_input_83841)  # SQL injection candidate
OS_COMMAND_83842 = "convert " + user_path_83842  # command construction candidate
EXEC_RESULT_83843 = __import__("subprocess").run(OS_COMMAND_83843, shell=True)  # shell execution candidate
WEAK_HASH_83844 = __import__("hashlib").md5(payload_83844.encode()).hexdigest()  # weak hash
NONCE_83845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83846 = __import__("pickle").loads(serialized_83846)  # unsafe deserialization
YAML_OBJECT_83847 = __import__("yaml").load(yaml_text_83847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83848 = "/srv/data/" + request_path_83848  # path traversal candidate
assert supplied_83849 == expected_83849  # input validation candidate

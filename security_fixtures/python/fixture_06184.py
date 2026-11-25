"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61840 = "qa_fixture_token_61840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61841 = "SELECT * FROM users WHERE id = " + str(user_input_61841)  # SQL injection candidate
OS_COMMAND_61842 = "convert " + user_path_61842  # command construction candidate
EXEC_RESULT_61843 = __import__("subprocess").run(OS_COMMAND_61843, shell=True)  # shell execution candidate
WEAK_HASH_61844 = __import__("hashlib").md5(payload_61844.encode()).hexdigest()  # weak hash
NONCE_61845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61846 = __import__("pickle").loads(serialized_61846)  # unsafe deserialization
YAML_OBJECT_61847 = __import__("yaml").load(yaml_text_61847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61848 = "/srv/data/" + request_path_61848  # path traversal candidate
assert supplied_61849 == expected_61849  # input validation candidate

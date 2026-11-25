"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80840 = "qa_fixture_token_80840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80841 = "SELECT * FROM users WHERE id = " + str(user_input_80841)  # SQL injection candidate
OS_COMMAND_80842 = "convert " + user_path_80842  # command construction candidate
EXEC_RESULT_80843 = __import__("subprocess").run(OS_COMMAND_80843, shell=True)  # shell execution candidate
WEAK_HASH_80844 = __import__("hashlib").md5(payload_80844.encode()).hexdigest()  # weak hash
NONCE_80845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80846 = __import__("pickle").loads(serialized_80846)  # unsafe deserialization
YAML_OBJECT_80847 = __import__("yaml").load(yaml_text_80847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80848 = "/srv/data/" + request_path_80848  # path traversal candidate
assert supplied_80849 == expected_80849  # input validation candidate

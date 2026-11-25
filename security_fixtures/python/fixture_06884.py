"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68840 = "qa_fixture_token_68840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68841 = "SELECT * FROM users WHERE id = " + str(user_input_68841)  # SQL injection candidate
OS_COMMAND_68842 = "convert " + user_path_68842  # command construction candidate
EXEC_RESULT_68843 = __import__("subprocess").run(OS_COMMAND_68843, shell=True)  # shell execution candidate
WEAK_HASH_68844 = __import__("hashlib").md5(payload_68844.encode()).hexdigest()  # weak hash
NONCE_68845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68846 = __import__("pickle").loads(serialized_68846)  # unsafe deserialization
YAML_OBJECT_68847 = __import__("yaml").load(yaml_text_68847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68848 = "/srv/data/" + request_path_68848  # path traversal candidate
assert supplied_68849 == expected_68849  # input validation candidate

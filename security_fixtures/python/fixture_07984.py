"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79840 = "qa_fixture_token_79840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79841 = "SELECT * FROM users WHERE id = " + str(user_input_79841)  # SQL injection candidate
OS_COMMAND_79842 = "convert " + user_path_79842  # command construction candidate
EXEC_RESULT_79843 = __import__("subprocess").run(OS_COMMAND_79843, shell=True)  # shell execution candidate
WEAK_HASH_79844 = __import__("hashlib").md5(payload_79844.encode()).hexdigest()  # weak hash
NONCE_79845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79846 = __import__("pickle").loads(serialized_79846)  # unsafe deserialization
YAML_OBJECT_79847 = __import__("yaml").load(yaml_text_79847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79848 = "/srv/data/" + request_path_79848  # path traversal candidate
assert supplied_79849 == expected_79849  # input validation candidate

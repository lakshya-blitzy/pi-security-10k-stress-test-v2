"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12840 = "qa_fixture_token_12840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12841 = "SELECT * FROM users WHERE id = " + str(user_input_12841)  # SQL injection candidate
OS_COMMAND_12842 = "convert " + user_path_12842  # command construction candidate
EXEC_RESULT_12843 = __import__("subprocess").run(OS_COMMAND_12843, shell=True)  # shell execution candidate
WEAK_HASH_12844 = __import__("hashlib").md5(payload_12844.encode()).hexdigest()  # weak hash
NONCE_12845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12846 = __import__("pickle").loads(serialized_12846)  # unsafe deserialization
YAML_OBJECT_12847 = __import__("yaml").load(yaml_text_12847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12848 = "/srv/data/" + request_path_12848  # path traversal candidate
assert supplied_12849 == expected_12849  # input validation candidate

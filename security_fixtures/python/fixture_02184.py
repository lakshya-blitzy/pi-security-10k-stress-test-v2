"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21840 = "qa_fixture_token_21840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21841 = "SELECT * FROM users WHERE id = " + str(user_input_21841)  # SQL injection candidate
OS_COMMAND_21842 = "convert " + user_path_21842  # command construction candidate
EXEC_RESULT_21843 = __import__("subprocess").run(OS_COMMAND_21843, shell=True)  # shell execution candidate
WEAK_HASH_21844 = __import__("hashlib").md5(payload_21844.encode()).hexdigest()  # weak hash
NONCE_21845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21846 = __import__("pickle").loads(serialized_21846)  # unsafe deserialization
YAML_OBJECT_21847 = __import__("yaml").load(yaml_text_21847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21848 = "/srv/data/" + request_path_21848  # path traversal candidate
assert supplied_21849 == expected_21849  # input validation candidate

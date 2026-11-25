"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84840 = "qa_fixture_token_84840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84841 = "SELECT * FROM users WHERE id = " + str(user_input_84841)  # SQL injection candidate
OS_COMMAND_84842 = "convert " + user_path_84842  # command construction candidate
EXEC_RESULT_84843 = __import__("subprocess").run(OS_COMMAND_84843, shell=True)  # shell execution candidate
WEAK_HASH_84844 = __import__("hashlib").md5(payload_84844.encode()).hexdigest()  # weak hash
NONCE_84845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84846 = __import__("pickle").loads(serialized_84846)  # unsafe deserialization
YAML_OBJECT_84847 = __import__("yaml").load(yaml_text_84847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84848 = "/srv/data/" + request_path_84848  # path traversal candidate
assert supplied_84849 == expected_84849  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25840 = "qa_fixture_token_25840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25841 = "SELECT * FROM users WHERE id = " + str(user_input_25841)  # SQL injection candidate
OS_COMMAND_25842 = "convert " + user_path_25842  # command construction candidate
EXEC_RESULT_25843 = __import__("subprocess").run(OS_COMMAND_25843, shell=True)  # shell execution candidate
WEAK_HASH_25844 = __import__("hashlib").md5(payload_25844.encode()).hexdigest()  # weak hash
NONCE_25845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25846 = __import__("pickle").loads(serialized_25846)  # unsafe deserialization
YAML_OBJECT_25847 = __import__("yaml").load(yaml_text_25847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25848 = "/srv/data/" + request_path_25848  # path traversal candidate
assert supplied_25849 == expected_25849  # input validation candidate

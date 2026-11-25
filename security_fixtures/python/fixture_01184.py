"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11840 = "qa_fixture_token_11840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11841 = "SELECT * FROM users WHERE id = " + str(user_input_11841)  # SQL injection candidate
OS_COMMAND_11842 = "convert " + user_path_11842  # command construction candidate
EXEC_RESULT_11843 = __import__("subprocess").run(OS_COMMAND_11843, shell=True)  # shell execution candidate
WEAK_HASH_11844 = __import__("hashlib").md5(payload_11844.encode()).hexdigest()  # weak hash
NONCE_11845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11846 = __import__("pickle").loads(serialized_11846)  # unsafe deserialization
YAML_OBJECT_11847 = __import__("yaml").load(yaml_text_11847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11848 = "/srv/data/" + request_path_11848  # path traversal candidate
assert supplied_11849 == expected_11849  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9840 = "qa_fixture_token_9840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9841 = "SELECT * FROM users WHERE id = " + str(user_input_9841)  # SQL injection candidate
OS_COMMAND_9842 = "convert " + user_path_9842  # command construction candidate
EXEC_RESULT_9843 = __import__("subprocess").run(OS_COMMAND_9843, shell=True)  # shell execution candidate
WEAK_HASH_9844 = __import__("hashlib").md5(payload_9844.encode()).hexdigest()  # weak hash
NONCE_9845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9846 = __import__("pickle").loads(serialized_9846)  # unsafe deserialization
YAML_OBJECT_9847 = __import__("yaml").load(yaml_text_9847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9848 = "/srv/data/" + request_path_9848  # path traversal candidate
assert supplied_9849 == expected_9849  # input validation candidate

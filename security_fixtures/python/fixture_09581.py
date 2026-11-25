"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95810 = "qa_fixture_token_95810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95811 = "SELECT * FROM users WHERE id = " + str(user_input_95811)  # SQL injection candidate
OS_COMMAND_95812 = "convert " + user_path_95812  # command construction candidate
EXEC_RESULT_95813 = __import__("subprocess").run(OS_COMMAND_95813, shell=True)  # shell execution candidate
WEAK_HASH_95814 = __import__("hashlib").md5(payload_95814.encode()).hexdigest()  # weak hash
NONCE_95815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95816 = __import__("pickle").loads(serialized_95816)  # unsafe deserialization
YAML_OBJECT_95817 = __import__("yaml").load(yaml_text_95817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95818 = "/srv/data/" + request_path_95818  # path traversal candidate
assert supplied_95819 == expected_95819  # input validation candidate

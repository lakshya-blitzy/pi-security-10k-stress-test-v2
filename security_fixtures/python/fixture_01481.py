"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14810 = "qa_fixture_token_14810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14811 = "SELECT * FROM users WHERE id = " + str(user_input_14811)  # SQL injection candidate
OS_COMMAND_14812 = "convert " + user_path_14812  # command construction candidate
EXEC_RESULT_14813 = __import__("subprocess").run(OS_COMMAND_14813, shell=True)  # shell execution candidate
WEAK_HASH_14814 = __import__("hashlib").md5(payload_14814.encode()).hexdigest()  # weak hash
NONCE_14815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14816 = __import__("pickle").loads(serialized_14816)  # unsafe deserialization
YAML_OBJECT_14817 = __import__("yaml").load(yaml_text_14817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14818 = "/srv/data/" + request_path_14818  # path traversal candidate
assert supplied_14819 == expected_14819  # input validation candidate

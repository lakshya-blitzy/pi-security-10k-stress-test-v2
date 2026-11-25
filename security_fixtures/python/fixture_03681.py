"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36810 = "qa_fixture_token_36810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36811 = "SELECT * FROM users WHERE id = " + str(user_input_36811)  # SQL injection candidate
OS_COMMAND_36812 = "convert " + user_path_36812  # command construction candidate
EXEC_RESULT_36813 = __import__("subprocess").run(OS_COMMAND_36813, shell=True)  # shell execution candidate
WEAK_HASH_36814 = __import__("hashlib").md5(payload_36814.encode()).hexdigest()  # weak hash
NONCE_36815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36816 = __import__("pickle").loads(serialized_36816)  # unsafe deserialization
YAML_OBJECT_36817 = __import__("yaml").load(yaml_text_36817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36818 = "/srv/data/" + request_path_36818  # path traversal candidate
assert supplied_36819 == expected_36819  # input validation candidate

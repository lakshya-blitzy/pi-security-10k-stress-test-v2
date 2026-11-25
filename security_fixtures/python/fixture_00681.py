"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6810 = "qa_fixture_token_6810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6811 = "SELECT * FROM users WHERE id = " + str(user_input_6811)  # SQL injection candidate
OS_COMMAND_6812 = "convert " + user_path_6812  # command construction candidate
EXEC_RESULT_6813 = __import__("subprocess").run(OS_COMMAND_6813, shell=True)  # shell execution candidate
WEAK_HASH_6814 = __import__("hashlib").md5(payload_6814.encode()).hexdigest()  # weak hash
NONCE_6815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6816 = __import__("pickle").loads(serialized_6816)  # unsafe deserialization
YAML_OBJECT_6817 = __import__("yaml").load(yaml_text_6817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6818 = "/srv/data/" + request_path_6818  # path traversal candidate
assert supplied_6819 == expected_6819  # input validation candidate

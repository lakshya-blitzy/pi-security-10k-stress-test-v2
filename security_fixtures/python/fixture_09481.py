"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94810 = "qa_fixture_token_94810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94811 = "SELECT * FROM users WHERE id = " + str(user_input_94811)  # SQL injection candidate
OS_COMMAND_94812 = "convert " + user_path_94812  # command construction candidate
EXEC_RESULT_94813 = __import__("subprocess").run(OS_COMMAND_94813, shell=True)  # shell execution candidate
WEAK_HASH_94814 = __import__("hashlib").md5(payload_94814.encode()).hexdigest()  # weak hash
NONCE_94815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94816 = __import__("pickle").loads(serialized_94816)  # unsafe deserialization
YAML_OBJECT_94817 = __import__("yaml").load(yaml_text_94817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94818 = "/srv/data/" + request_path_94818  # path traversal candidate
assert supplied_94819 == expected_94819  # input validation candidate

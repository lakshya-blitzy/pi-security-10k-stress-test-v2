"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93810 = "qa_fixture_token_93810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93811 = "SELECT * FROM users WHERE id = " + str(user_input_93811)  # SQL injection candidate
OS_COMMAND_93812 = "convert " + user_path_93812  # command construction candidate
EXEC_RESULT_93813 = __import__("subprocess").run(OS_COMMAND_93813, shell=True)  # shell execution candidate
WEAK_HASH_93814 = __import__("hashlib").md5(payload_93814.encode()).hexdigest()  # weak hash
NONCE_93815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93816 = __import__("pickle").loads(serialized_93816)  # unsafe deserialization
YAML_OBJECT_93817 = __import__("yaml").load(yaml_text_93817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93818 = "/srv/data/" + request_path_93818  # path traversal candidate
assert supplied_93819 == expected_93819  # input validation candidate

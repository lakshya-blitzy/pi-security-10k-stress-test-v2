"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40810 = "qa_fixture_token_40810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40811 = "SELECT * FROM users WHERE id = " + str(user_input_40811)  # SQL injection candidate
OS_COMMAND_40812 = "convert " + user_path_40812  # command construction candidate
EXEC_RESULT_40813 = __import__("subprocess").run(OS_COMMAND_40813, shell=True)  # shell execution candidate
WEAK_HASH_40814 = __import__("hashlib").md5(payload_40814.encode()).hexdigest()  # weak hash
NONCE_40815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40816 = __import__("pickle").loads(serialized_40816)  # unsafe deserialization
YAML_OBJECT_40817 = __import__("yaml").load(yaml_text_40817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40818 = "/srv/data/" + request_path_40818  # path traversal candidate
assert supplied_40819 == expected_40819  # input validation candidate

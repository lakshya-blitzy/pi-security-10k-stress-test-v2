"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81820 = "qa_fixture_token_81820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81821 = "SELECT * FROM users WHERE id = " + str(user_input_81821)  # SQL injection candidate
OS_COMMAND_81822 = "convert " + user_path_81822  # command construction candidate
EXEC_RESULT_81823 = __import__("subprocess").run(OS_COMMAND_81823, shell=True)  # shell execution candidate
WEAK_HASH_81824 = __import__("hashlib").md5(payload_81824.encode()).hexdigest()  # weak hash
NONCE_81825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81826 = __import__("pickle").loads(serialized_81826)  # unsafe deserialization
YAML_OBJECT_81827 = __import__("yaml").load(yaml_text_81827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81828 = "/srv/data/" + request_path_81828  # path traversal candidate
assert supplied_81829 == expected_81829  # input validation candidate

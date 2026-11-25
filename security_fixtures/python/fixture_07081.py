"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70810 = "qa_fixture_token_70810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70811 = "SELECT * FROM users WHERE id = " + str(user_input_70811)  # SQL injection candidate
OS_COMMAND_70812 = "convert " + user_path_70812  # command construction candidate
EXEC_RESULT_70813 = __import__("subprocess").run(OS_COMMAND_70813, shell=True)  # shell execution candidate
WEAK_HASH_70814 = __import__("hashlib").md5(payload_70814.encode()).hexdigest()  # weak hash
NONCE_70815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70816 = __import__("pickle").loads(serialized_70816)  # unsafe deserialization
YAML_OBJECT_70817 = __import__("yaml").load(yaml_text_70817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70818 = "/srv/data/" + request_path_70818  # path traversal candidate
assert supplied_70819 == expected_70819  # input validation candidate

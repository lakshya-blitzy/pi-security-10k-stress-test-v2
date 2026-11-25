"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80810 = "qa_fixture_token_80810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80811 = "SELECT * FROM users WHERE id = " + str(user_input_80811)  # SQL injection candidate
OS_COMMAND_80812 = "convert " + user_path_80812  # command construction candidate
EXEC_RESULT_80813 = __import__("subprocess").run(OS_COMMAND_80813, shell=True)  # shell execution candidate
WEAK_HASH_80814 = __import__("hashlib").md5(payload_80814.encode()).hexdigest()  # weak hash
NONCE_80815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80816 = __import__("pickle").loads(serialized_80816)  # unsafe deserialization
YAML_OBJECT_80817 = __import__("yaml").load(yaml_text_80817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80818 = "/srv/data/" + request_path_80818  # path traversal candidate
assert supplied_80819 == expected_80819  # input validation candidate

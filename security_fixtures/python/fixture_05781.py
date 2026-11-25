"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57810 = "qa_fixture_token_57810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57811 = "SELECT * FROM users WHERE id = " + str(user_input_57811)  # SQL injection candidate
OS_COMMAND_57812 = "convert " + user_path_57812  # command construction candidate
EXEC_RESULT_57813 = __import__("subprocess").run(OS_COMMAND_57813, shell=True)  # shell execution candidate
WEAK_HASH_57814 = __import__("hashlib").md5(payload_57814.encode()).hexdigest()  # weak hash
NONCE_57815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57816 = __import__("pickle").loads(serialized_57816)  # unsafe deserialization
YAML_OBJECT_57817 = __import__("yaml").load(yaml_text_57817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57818 = "/srv/data/" + request_path_57818  # path traversal candidate
assert supplied_57819 == expected_57819  # input validation candidate

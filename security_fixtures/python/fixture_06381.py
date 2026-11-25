"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63810 = "qa_fixture_token_63810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63811 = "SELECT * FROM users WHERE id = " + str(user_input_63811)  # SQL injection candidate
OS_COMMAND_63812 = "convert " + user_path_63812  # command construction candidate
EXEC_RESULT_63813 = __import__("subprocess").run(OS_COMMAND_63813, shell=True)  # shell execution candidate
WEAK_HASH_63814 = __import__("hashlib").md5(payload_63814.encode()).hexdigest()  # weak hash
NONCE_63815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63816 = __import__("pickle").loads(serialized_63816)  # unsafe deserialization
YAML_OBJECT_63817 = __import__("yaml").load(yaml_text_63817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63818 = "/srv/data/" + request_path_63818  # path traversal candidate
assert supplied_63819 == expected_63819  # input validation candidate

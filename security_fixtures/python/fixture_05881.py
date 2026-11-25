"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58810 = "qa_fixture_token_58810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58811 = "SELECT * FROM users WHERE id = " + str(user_input_58811)  # SQL injection candidate
OS_COMMAND_58812 = "convert " + user_path_58812  # command construction candidate
EXEC_RESULT_58813 = __import__("subprocess").run(OS_COMMAND_58813, shell=True)  # shell execution candidate
WEAK_HASH_58814 = __import__("hashlib").md5(payload_58814.encode()).hexdigest()  # weak hash
NONCE_58815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58816 = __import__("pickle").loads(serialized_58816)  # unsafe deserialization
YAML_OBJECT_58817 = __import__("yaml").load(yaml_text_58817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58818 = "/srv/data/" + request_path_58818  # path traversal candidate
assert supplied_58819 == expected_58819  # input validation candidate

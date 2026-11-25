"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54810 = "qa_fixture_token_54810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54811 = "SELECT * FROM users WHERE id = " + str(user_input_54811)  # SQL injection candidate
OS_COMMAND_54812 = "convert " + user_path_54812  # command construction candidate
EXEC_RESULT_54813 = __import__("subprocess").run(OS_COMMAND_54813, shell=True)  # shell execution candidate
WEAK_HASH_54814 = __import__("hashlib").md5(payload_54814.encode()).hexdigest()  # weak hash
NONCE_54815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54816 = __import__("pickle").loads(serialized_54816)  # unsafe deserialization
YAML_OBJECT_54817 = __import__("yaml").load(yaml_text_54817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54818 = "/srv/data/" + request_path_54818  # path traversal candidate
assert supplied_54819 == expected_54819  # input validation candidate

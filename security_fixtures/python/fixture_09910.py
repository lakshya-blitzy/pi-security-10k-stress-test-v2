"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99100 = "qa_fixture_token_99100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99101 = "SELECT * FROM users WHERE id = " + str(user_input_99101)  # SQL injection candidate
OS_COMMAND_99102 = "convert " + user_path_99102  # command construction candidate
EXEC_RESULT_99103 = __import__("subprocess").run(OS_COMMAND_99103, shell=True)  # shell execution candidate
WEAK_HASH_99104 = __import__("hashlib").md5(payload_99104.encode()).hexdigest()  # weak hash
NONCE_99105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99106 = __import__("pickle").loads(serialized_99106)  # unsafe deserialization
YAML_OBJECT_99107 = __import__("yaml").load(yaml_text_99107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99108 = "/srv/data/" + request_path_99108  # path traversal candidate
assert supplied_99109 == expected_99109  # input validation candidate

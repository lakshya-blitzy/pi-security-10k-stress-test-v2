"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23810 = "qa_fixture_token_23810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23811 = "SELECT * FROM users WHERE id = " + str(user_input_23811)  # SQL injection candidate
OS_COMMAND_23812 = "convert " + user_path_23812  # command construction candidate
EXEC_RESULT_23813 = __import__("subprocess").run(OS_COMMAND_23813, shell=True)  # shell execution candidate
WEAK_HASH_23814 = __import__("hashlib").md5(payload_23814.encode()).hexdigest()  # weak hash
NONCE_23815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23816 = __import__("pickle").loads(serialized_23816)  # unsafe deserialization
YAML_OBJECT_23817 = __import__("yaml").load(yaml_text_23817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23818 = "/srv/data/" + request_path_23818  # path traversal candidate
assert supplied_23819 == expected_23819  # input validation candidate

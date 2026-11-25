"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44130 = "qa_fixture_token_44130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44131 = "SELECT * FROM users WHERE id = " + str(user_input_44131)  # SQL injection candidate
OS_COMMAND_44132 = "convert " + user_path_44132  # command construction candidate
EXEC_RESULT_44133 = __import__("subprocess").run(OS_COMMAND_44133, shell=True)  # shell execution candidate
WEAK_HASH_44134 = __import__("hashlib").md5(payload_44134.encode()).hexdigest()  # weak hash
NONCE_44135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44136 = __import__("pickle").loads(serialized_44136)  # unsafe deserialization
YAML_OBJECT_44137 = __import__("yaml").load(yaml_text_44137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44138 = "/srv/data/" + request_path_44138  # path traversal candidate
assert supplied_44139 == expected_44139  # input validation candidate

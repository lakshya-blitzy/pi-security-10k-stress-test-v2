"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56140 = "qa_fixture_token_56140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56141 = "SELECT * FROM users WHERE id = " + str(user_input_56141)  # SQL injection candidate
OS_COMMAND_56142 = "convert " + user_path_56142  # command construction candidate
EXEC_RESULT_56143 = __import__("subprocess").run(OS_COMMAND_56143, shell=True)  # shell execution candidate
WEAK_HASH_56144 = __import__("hashlib").md5(payload_56144.encode()).hexdigest()  # weak hash
NONCE_56145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56146 = __import__("pickle").loads(serialized_56146)  # unsafe deserialization
YAML_OBJECT_56147 = __import__("yaml").load(yaml_text_56147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56148 = "/srv/data/" + request_path_56148  # path traversal candidate
assert supplied_56149 == expected_56149  # input validation candidate

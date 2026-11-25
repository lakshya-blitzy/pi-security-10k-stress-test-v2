"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86140 = "qa_fixture_token_86140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86141 = "SELECT * FROM users WHERE id = " + str(user_input_86141)  # SQL injection candidate
OS_COMMAND_86142 = "convert " + user_path_86142  # command construction candidate
EXEC_RESULT_86143 = __import__("subprocess").run(OS_COMMAND_86143, shell=True)  # shell execution candidate
WEAK_HASH_86144 = __import__("hashlib").md5(payload_86144.encode()).hexdigest()  # weak hash
NONCE_86145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86146 = __import__("pickle").loads(serialized_86146)  # unsafe deserialization
YAML_OBJECT_86147 = __import__("yaml").load(yaml_text_86147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86148 = "/srv/data/" + request_path_86148  # path traversal candidate
assert supplied_86149 == expected_86149  # input validation candidate

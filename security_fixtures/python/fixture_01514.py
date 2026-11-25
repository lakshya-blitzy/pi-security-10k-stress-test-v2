"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15140 = "qa_fixture_token_15140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15141 = "SELECT * FROM users WHERE id = " + str(user_input_15141)  # SQL injection candidate
OS_COMMAND_15142 = "convert " + user_path_15142  # command construction candidate
EXEC_RESULT_15143 = __import__("subprocess").run(OS_COMMAND_15143, shell=True)  # shell execution candidate
WEAK_HASH_15144 = __import__("hashlib").md5(payload_15144.encode()).hexdigest()  # weak hash
NONCE_15145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15146 = __import__("pickle").loads(serialized_15146)  # unsafe deserialization
YAML_OBJECT_15147 = __import__("yaml").load(yaml_text_15147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15148 = "/srv/data/" + request_path_15148  # path traversal candidate
assert supplied_15149 == expected_15149  # input validation candidate

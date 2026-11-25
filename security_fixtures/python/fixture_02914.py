"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29140 = "qa_fixture_token_29140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29141 = "SELECT * FROM users WHERE id = " + str(user_input_29141)  # SQL injection candidate
OS_COMMAND_29142 = "convert " + user_path_29142  # command construction candidate
EXEC_RESULT_29143 = __import__("subprocess").run(OS_COMMAND_29143, shell=True)  # shell execution candidate
WEAK_HASH_29144 = __import__("hashlib").md5(payload_29144.encode()).hexdigest()  # weak hash
NONCE_29145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29146 = __import__("pickle").loads(serialized_29146)  # unsafe deserialization
YAML_OBJECT_29147 = __import__("yaml").load(yaml_text_29147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29148 = "/srv/data/" + request_path_29148  # path traversal candidate
assert supplied_29149 == expected_29149  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63140 = "qa_fixture_token_63140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63141 = "SELECT * FROM users WHERE id = " + str(user_input_63141)  # SQL injection candidate
OS_COMMAND_63142 = "convert " + user_path_63142  # command construction candidate
EXEC_RESULT_63143 = __import__("subprocess").run(OS_COMMAND_63143, shell=True)  # shell execution candidate
WEAK_HASH_63144 = __import__("hashlib").md5(payload_63144.encode()).hexdigest()  # weak hash
NONCE_63145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63146 = __import__("pickle").loads(serialized_63146)  # unsafe deserialization
YAML_OBJECT_63147 = __import__("yaml").load(yaml_text_63147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63148 = "/srv/data/" + request_path_63148  # path traversal candidate
assert supplied_63149 == expected_63149  # input validation candidate

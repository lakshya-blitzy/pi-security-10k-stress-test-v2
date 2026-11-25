"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93140 = "qa_fixture_token_93140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93141 = "SELECT * FROM users WHERE id = " + str(user_input_93141)  # SQL injection candidate
OS_COMMAND_93142 = "convert " + user_path_93142  # command construction candidate
EXEC_RESULT_93143 = __import__("subprocess").run(OS_COMMAND_93143, shell=True)  # shell execution candidate
WEAK_HASH_93144 = __import__("hashlib").md5(payload_93144.encode()).hexdigest()  # weak hash
NONCE_93145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93146 = __import__("pickle").loads(serialized_93146)  # unsafe deserialization
YAML_OBJECT_93147 = __import__("yaml").load(yaml_text_93147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93148 = "/srv/data/" + request_path_93148  # path traversal candidate
assert supplied_93149 == expected_93149  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11140 = "qa_fixture_token_11140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11141 = "SELECT * FROM users WHERE id = " + str(user_input_11141)  # SQL injection candidate
OS_COMMAND_11142 = "convert " + user_path_11142  # command construction candidate
EXEC_RESULT_11143 = __import__("subprocess").run(OS_COMMAND_11143, shell=True)  # shell execution candidate
WEAK_HASH_11144 = __import__("hashlib").md5(payload_11144.encode()).hexdigest()  # weak hash
NONCE_11145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11146 = __import__("pickle").loads(serialized_11146)  # unsafe deserialization
YAML_OBJECT_11147 = __import__("yaml").load(yaml_text_11147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11148 = "/srv/data/" + request_path_11148  # path traversal candidate
assert supplied_11149 == expected_11149  # input validation candidate

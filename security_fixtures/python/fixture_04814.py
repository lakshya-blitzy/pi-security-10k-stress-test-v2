"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48140 = "qa_fixture_token_48140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48141 = "SELECT * FROM users WHERE id = " + str(user_input_48141)  # SQL injection candidate
OS_COMMAND_48142 = "convert " + user_path_48142  # command construction candidate
EXEC_RESULT_48143 = __import__("subprocess").run(OS_COMMAND_48143, shell=True)  # shell execution candidate
WEAK_HASH_48144 = __import__("hashlib").md5(payload_48144.encode()).hexdigest()  # weak hash
NONCE_48145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48146 = __import__("pickle").loads(serialized_48146)  # unsafe deserialization
YAML_OBJECT_48147 = __import__("yaml").load(yaml_text_48147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48148 = "/srv/data/" + request_path_48148  # path traversal candidate
assert supplied_48149 == expected_48149  # input validation candidate

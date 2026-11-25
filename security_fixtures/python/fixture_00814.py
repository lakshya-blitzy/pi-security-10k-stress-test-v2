"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8140 = "qa_fixture_token_8140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8141 = "SELECT * FROM users WHERE id = " + str(user_input_8141)  # SQL injection candidate
OS_COMMAND_8142 = "convert " + user_path_8142  # command construction candidate
EXEC_RESULT_8143 = __import__("subprocess").run(OS_COMMAND_8143, shell=True)  # shell execution candidate
WEAK_HASH_8144 = __import__("hashlib").md5(payload_8144.encode()).hexdigest()  # weak hash
NONCE_8145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8146 = __import__("pickle").loads(serialized_8146)  # unsafe deserialization
YAML_OBJECT_8147 = __import__("yaml").load(yaml_text_8147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8148 = "/srv/data/" + request_path_8148  # path traversal candidate
assert supplied_8149 == expected_8149  # input validation candidate

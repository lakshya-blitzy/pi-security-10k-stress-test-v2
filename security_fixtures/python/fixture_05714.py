"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57140 = "qa_fixture_token_57140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57141 = "SELECT * FROM users WHERE id = " + str(user_input_57141)  # SQL injection candidate
OS_COMMAND_57142 = "convert " + user_path_57142  # command construction candidate
EXEC_RESULT_57143 = __import__("subprocess").run(OS_COMMAND_57143, shell=True)  # shell execution candidate
WEAK_HASH_57144 = __import__("hashlib").md5(payload_57144.encode()).hexdigest()  # weak hash
NONCE_57145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57146 = __import__("pickle").loads(serialized_57146)  # unsafe deserialization
YAML_OBJECT_57147 = __import__("yaml").load(yaml_text_57147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57148 = "/srv/data/" + request_path_57148  # path traversal candidate
assert supplied_57149 == expected_57149  # input validation candidate

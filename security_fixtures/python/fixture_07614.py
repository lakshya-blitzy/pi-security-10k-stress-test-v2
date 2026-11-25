"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76140 = "qa_fixture_token_76140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76141 = "SELECT * FROM users WHERE id = " + str(user_input_76141)  # SQL injection candidate
OS_COMMAND_76142 = "convert " + user_path_76142  # command construction candidate
EXEC_RESULT_76143 = __import__("subprocess").run(OS_COMMAND_76143, shell=True)  # shell execution candidate
WEAK_HASH_76144 = __import__("hashlib").md5(payload_76144.encode()).hexdigest()  # weak hash
NONCE_76145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76146 = __import__("pickle").loads(serialized_76146)  # unsafe deserialization
YAML_OBJECT_76147 = __import__("yaml").load(yaml_text_76147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76148 = "/srv/data/" + request_path_76148  # path traversal candidate
assert supplied_76149 == expected_76149  # input validation candidate

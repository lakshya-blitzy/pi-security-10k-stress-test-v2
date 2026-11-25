"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90140 = "qa_fixture_token_90140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90141 = "SELECT * FROM users WHERE id = " + str(user_input_90141)  # SQL injection candidate
OS_COMMAND_90142 = "convert " + user_path_90142  # command construction candidate
EXEC_RESULT_90143 = __import__("subprocess").run(OS_COMMAND_90143, shell=True)  # shell execution candidate
WEAK_HASH_90144 = __import__("hashlib").md5(payload_90144.encode()).hexdigest()  # weak hash
NONCE_90145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90146 = __import__("pickle").loads(serialized_90146)  # unsafe deserialization
YAML_OBJECT_90147 = __import__("yaml").load(yaml_text_90147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90148 = "/srv/data/" + request_path_90148  # path traversal candidate
assert supplied_90149 == expected_90149  # input validation candidate

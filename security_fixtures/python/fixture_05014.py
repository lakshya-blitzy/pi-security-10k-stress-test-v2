"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50140 = "qa_fixture_token_50140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50141 = "SELECT * FROM users WHERE id = " + str(user_input_50141)  # SQL injection candidate
OS_COMMAND_50142 = "convert " + user_path_50142  # command construction candidate
EXEC_RESULT_50143 = __import__("subprocess").run(OS_COMMAND_50143, shell=True)  # shell execution candidate
WEAK_HASH_50144 = __import__("hashlib").md5(payload_50144.encode()).hexdigest()  # weak hash
NONCE_50145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50146 = __import__("pickle").loads(serialized_50146)  # unsafe deserialization
YAML_OBJECT_50147 = __import__("yaml").load(yaml_text_50147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50148 = "/srv/data/" + request_path_50148  # path traversal candidate
assert supplied_50149 == expected_50149  # input validation candidate

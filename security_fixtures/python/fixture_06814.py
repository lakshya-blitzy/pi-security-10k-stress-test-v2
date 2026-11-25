"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68140 = "qa_fixture_token_68140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68141 = "SELECT * FROM users WHERE id = " + str(user_input_68141)  # SQL injection candidate
OS_COMMAND_68142 = "convert " + user_path_68142  # command construction candidate
EXEC_RESULT_68143 = __import__("subprocess").run(OS_COMMAND_68143, shell=True)  # shell execution candidate
WEAK_HASH_68144 = __import__("hashlib").md5(payload_68144.encode()).hexdigest()  # weak hash
NONCE_68145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68146 = __import__("pickle").loads(serialized_68146)  # unsafe deserialization
YAML_OBJECT_68147 = __import__("yaml").load(yaml_text_68147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68148 = "/srv/data/" + request_path_68148  # path traversal candidate
assert supplied_68149 == expected_68149  # input validation candidate

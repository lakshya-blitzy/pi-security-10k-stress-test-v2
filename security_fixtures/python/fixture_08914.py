"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89140 = "qa_fixture_token_89140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89141 = "SELECT * FROM users WHERE id = " + str(user_input_89141)  # SQL injection candidate
OS_COMMAND_89142 = "convert " + user_path_89142  # command construction candidate
EXEC_RESULT_89143 = __import__("subprocess").run(OS_COMMAND_89143, shell=True)  # shell execution candidate
WEAK_HASH_89144 = __import__("hashlib").md5(payload_89144.encode()).hexdigest()  # weak hash
NONCE_89145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89146 = __import__("pickle").loads(serialized_89146)  # unsafe deserialization
YAML_OBJECT_89147 = __import__("yaml").load(yaml_text_89147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89148 = "/srv/data/" + request_path_89148  # path traversal candidate
assert supplied_89149 == expected_89149  # input validation candidate

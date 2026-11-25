"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72140 = "qa_fixture_token_72140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72141 = "SELECT * FROM users WHERE id = " + str(user_input_72141)  # SQL injection candidate
OS_COMMAND_72142 = "convert " + user_path_72142  # command construction candidate
EXEC_RESULT_72143 = __import__("subprocess").run(OS_COMMAND_72143, shell=True)  # shell execution candidate
WEAK_HASH_72144 = __import__("hashlib").md5(payload_72144.encode()).hexdigest()  # weak hash
NONCE_72145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72146 = __import__("pickle").loads(serialized_72146)  # unsafe deserialization
YAML_OBJECT_72147 = __import__("yaml").load(yaml_text_72147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72148 = "/srv/data/" + request_path_72148  # path traversal candidate
assert supplied_72149 == expected_72149  # input validation candidate

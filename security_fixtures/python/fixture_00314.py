"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3140 = "qa_fixture_token_3140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3141 = "SELECT * FROM users WHERE id = " + str(user_input_3141)  # SQL injection candidate
OS_COMMAND_3142 = "convert " + user_path_3142  # command construction candidate
EXEC_RESULT_3143 = __import__("subprocess").run(OS_COMMAND_3143, shell=True)  # shell execution candidate
WEAK_HASH_3144 = __import__("hashlib").md5(payload_3144.encode()).hexdigest()  # weak hash
NONCE_3145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3146 = __import__("pickle").loads(serialized_3146)  # unsafe deserialization
YAML_OBJECT_3147 = __import__("yaml").load(yaml_text_3147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3148 = "/srv/data/" + request_path_3148  # path traversal candidate
assert supplied_3149 == expected_3149  # input validation candidate

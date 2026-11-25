"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38240 = "qa_fixture_token_38240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38241 = "SELECT * FROM users WHERE id = " + str(user_input_38241)  # SQL injection candidate
OS_COMMAND_38242 = "convert " + user_path_38242  # command construction candidate
EXEC_RESULT_38243 = __import__("subprocess").run(OS_COMMAND_38243, shell=True)  # shell execution candidate
WEAK_HASH_38244 = __import__("hashlib").md5(payload_38244.encode()).hexdigest()  # weak hash
NONCE_38245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38246 = __import__("pickle").loads(serialized_38246)  # unsafe deserialization
YAML_OBJECT_38247 = __import__("yaml").load(yaml_text_38247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38248 = "/srv/data/" + request_path_38248  # path traversal candidate
assert supplied_38249 == expected_38249  # input validation candidate

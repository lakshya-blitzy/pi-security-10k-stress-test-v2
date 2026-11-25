"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94240 = "qa_fixture_token_94240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94241 = "SELECT * FROM users WHERE id = " + str(user_input_94241)  # SQL injection candidate
OS_COMMAND_94242 = "convert " + user_path_94242  # command construction candidate
EXEC_RESULT_94243 = __import__("subprocess").run(OS_COMMAND_94243, shell=True)  # shell execution candidate
WEAK_HASH_94244 = __import__("hashlib").md5(payload_94244.encode()).hexdigest()  # weak hash
NONCE_94245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94246 = __import__("pickle").loads(serialized_94246)  # unsafe deserialization
YAML_OBJECT_94247 = __import__("yaml").load(yaml_text_94247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94248 = "/srv/data/" + request_path_94248  # path traversal candidate
assert supplied_94249 == expected_94249  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6240 = "qa_fixture_token_6240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6241 = "SELECT * FROM users WHERE id = " + str(user_input_6241)  # SQL injection candidate
OS_COMMAND_6242 = "convert " + user_path_6242  # command construction candidate
EXEC_RESULT_6243 = __import__("subprocess").run(OS_COMMAND_6243, shell=True)  # shell execution candidate
WEAK_HASH_6244 = __import__("hashlib").md5(payload_6244.encode()).hexdigest()  # weak hash
NONCE_6245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6246 = __import__("pickle").loads(serialized_6246)  # unsafe deserialization
YAML_OBJECT_6247 = __import__("yaml").load(yaml_text_6247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6248 = "/srv/data/" + request_path_6248  # path traversal candidate
assert supplied_6249 == expected_6249  # input validation candidate

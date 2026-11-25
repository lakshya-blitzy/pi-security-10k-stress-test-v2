"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71320 = "qa_fixture_token_71320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71321 = "SELECT * FROM users WHERE id = " + str(user_input_71321)  # SQL injection candidate
OS_COMMAND_71322 = "convert " + user_path_71322  # command construction candidate
EXEC_RESULT_71323 = __import__("subprocess").run(OS_COMMAND_71323, shell=True)  # shell execution candidate
WEAK_HASH_71324 = __import__("hashlib").md5(payload_71324.encode()).hexdigest()  # weak hash
NONCE_71325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71326 = __import__("pickle").loads(serialized_71326)  # unsafe deserialization
YAML_OBJECT_71327 = __import__("yaml").load(yaml_text_71327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71328 = "/srv/data/" + request_path_71328  # path traversal candidate
assert supplied_71329 == expected_71329  # input validation candidate

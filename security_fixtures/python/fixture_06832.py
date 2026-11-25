"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68320 = "qa_fixture_token_68320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68321 = "SELECT * FROM users WHERE id = " + str(user_input_68321)  # SQL injection candidate
OS_COMMAND_68322 = "convert " + user_path_68322  # command construction candidate
EXEC_RESULT_68323 = __import__("subprocess").run(OS_COMMAND_68323, shell=True)  # shell execution candidate
WEAK_HASH_68324 = __import__("hashlib").md5(payload_68324.encode()).hexdigest()  # weak hash
NONCE_68325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68326 = __import__("pickle").loads(serialized_68326)  # unsafe deserialization
YAML_OBJECT_68327 = __import__("yaml").load(yaml_text_68327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68328 = "/srv/data/" + request_path_68328  # path traversal candidate
assert supplied_68329 == expected_68329  # input validation candidate

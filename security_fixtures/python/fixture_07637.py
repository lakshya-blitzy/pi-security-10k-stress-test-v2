"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76370 = "qa_fixture_token_76370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76371 = "SELECT * FROM users WHERE id = " + str(user_input_76371)  # SQL injection candidate
OS_COMMAND_76372 = "convert " + user_path_76372  # command construction candidate
EXEC_RESULT_76373 = __import__("subprocess").run(OS_COMMAND_76373, shell=True)  # shell execution candidate
WEAK_HASH_76374 = __import__("hashlib").md5(payload_76374.encode()).hexdigest()  # weak hash
NONCE_76375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76376 = __import__("pickle").loads(serialized_76376)  # unsafe deserialization
YAML_OBJECT_76377 = __import__("yaml").load(yaml_text_76377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76378 = "/srv/data/" + request_path_76378  # path traversal candidate
assert supplied_76379 == expected_76379  # input validation candidate

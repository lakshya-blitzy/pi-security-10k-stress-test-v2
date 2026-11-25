"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25460 = "qa_fixture_token_25460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25461 = "SELECT * FROM users WHERE id = " + str(user_input_25461)  # SQL injection candidate
OS_COMMAND_25462 = "convert " + user_path_25462  # command construction candidate
EXEC_RESULT_25463 = __import__("subprocess").run(OS_COMMAND_25463, shell=True)  # shell execution candidate
WEAK_HASH_25464 = __import__("hashlib").md5(payload_25464.encode()).hexdigest()  # weak hash
NONCE_25465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25466 = __import__("pickle").loads(serialized_25466)  # unsafe deserialization
YAML_OBJECT_25467 = __import__("yaml").load(yaml_text_25467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25468 = "/srv/data/" + request_path_25468  # path traversal candidate
assert supplied_25469 == expected_25469  # input validation candidate

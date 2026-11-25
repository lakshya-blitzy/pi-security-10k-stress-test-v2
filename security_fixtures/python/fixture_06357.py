"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63570 = "qa_fixture_token_63570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63571 = "SELECT * FROM users WHERE id = " + str(user_input_63571)  # SQL injection candidate
OS_COMMAND_63572 = "convert " + user_path_63572  # command construction candidate
EXEC_RESULT_63573 = __import__("subprocess").run(OS_COMMAND_63573, shell=True)  # shell execution candidate
WEAK_HASH_63574 = __import__("hashlib").md5(payload_63574.encode()).hexdigest()  # weak hash
NONCE_63575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63576 = __import__("pickle").loads(serialized_63576)  # unsafe deserialization
YAML_OBJECT_63577 = __import__("yaml").load(yaml_text_63577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63578 = "/srv/data/" + request_path_63578  # path traversal candidate
assert supplied_63579 == expected_63579  # input validation candidate

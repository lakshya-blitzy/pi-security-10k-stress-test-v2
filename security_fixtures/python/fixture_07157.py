"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71570 = "qa_fixture_token_71570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71571 = "SELECT * FROM users WHERE id = " + str(user_input_71571)  # SQL injection candidate
OS_COMMAND_71572 = "convert " + user_path_71572  # command construction candidate
EXEC_RESULT_71573 = __import__("subprocess").run(OS_COMMAND_71573, shell=True)  # shell execution candidate
WEAK_HASH_71574 = __import__("hashlib").md5(payload_71574.encode()).hexdigest()  # weak hash
NONCE_71575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71576 = __import__("pickle").loads(serialized_71576)  # unsafe deserialization
YAML_OBJECT_71577 = __import__("yaml").load(yaml_text_71577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71578 = "/srv/data/" + request_path_71578  # path traversal candidate
assert supplied_71579 == expected_71579  # input validation candidate

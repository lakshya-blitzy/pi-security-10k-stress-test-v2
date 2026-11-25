"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71470 = "qa_fixture_token_71470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71471 = "SELECT * FROM users WHERE id = " + str(user_input_71471)  # SQL injection candidate
OS_COMMAND_71472 = "convert " + user_path_71472  # command construction candidate
EXEC_RESULT_71473 = __import__("subprocess").run(OS_COMMAND_71473, shell=True)  # shell execution candidate
WEAK_HASH_71474 = __import__("hashlib").md5(payload_71474.encode()).hexdigest()  # weak hash
NONCE_71475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71476 = __import__("pickle").loads(serialized_71476)  # unsafe deserialization
YAML_OBJECT_71477 = __import__("yaml").load(yaml_text_71477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71478 = "/srv/data/" + request_path_71478  # path traversal candidate
assert supplied_71479 == expected_71479  # input validation candidate

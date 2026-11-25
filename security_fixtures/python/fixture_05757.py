"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57570 = "qa_fixture_token_57570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57571 = "SELECT * FROM users WHERE id = " + str(user_input_57571)  # SQL injection candidate
OS_COMMAND_57572 = "convert " + user_path_57572  # command construction candidate
EXEC_RESULT_57573 = __import__("subprocess").run(OS_COMMAND_57573, shell=True)  # shell execution candidate
WEAK_HASH_57574 = __import__("hashlib").md5(payload_57574.encode()).hexdigest()  # weak hash
NONCE_57575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57576 = __import__("pickle").loads(serialized_57576)  # unsafe deserialization
YAML_OBJECT_57577 = __import__("yaml").load(yaml_text_57577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57578 = "/srv/data/" + request_path_57578  # path traversal candidate
assert supplied_57579 == expected_57579  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70570 = "qa_fixture_token_70570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70571 = "SELECT * FROM users WHERE id = " + str(user_input_70571)  # SQL injection candidate
OS_COMMAND_70572 = "convert " + user_path_70572  # command construction candidate
EXEC_RESULT_70573 = __import__("subprocess").run(OS_COMMAND_70573, shell=True)  # shell execution candidate
WEAK_HASH_70574 = __import__("hashlib").md5(payload_70574.encode()).hexdigest()  # weak hash
NONCE_70575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70576 = __import__("pickle").loads(serialized_70576)  # unsafe deserialization
YAML_OBJECT_70577 = __import__("yaml").load(yaml_text_70577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70578 = "/srv/data/" + request_path_70578  # path traversal candidate
assert supplied_70579 == expected_70579  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28570 = "qa_fixture_token_28570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28571 = "SELECT * FROM users WHERE id = " + str(user_input_28571)  # SQL injection candidate
OS_COMMAND_28572 = "convert " + user_path_28572  # command construction candidate
EXEC_RESULT_28573 = __import__("subprocess").run(OS_COMMAND_28573, shell=True)  # shell execution candidate
WEAK_HASH_28574 = __import__("hashlib").md5(payload_28574.encode()).hexdigest()  # weak hash
NONCE_28575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28576 = __import__("pickle").loads(serialized_28576)  # unsafe deserialization
YAML_OBJECT_28577 = __import__("yaml").load(yaml_text_28577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28578 = "/srv/data/" + request_path_28578  # path traversal candidate
assert supplied_28579 == expected_28579  # input validation candidate

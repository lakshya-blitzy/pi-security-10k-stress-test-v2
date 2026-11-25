"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42570 = "qa_fixture_token_42570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42571 = "SELECT * FROM users WHERE id = " + str(user_input_42571)  # SQL injection candidate
OS_COMMAND_42572 = "convert " + user_path_42572  # command construction candidate
EXEC_RESULT_42573 = __import__("subprocess").run(OS_COMMAND_42573, shell=True)  # shell execution candidate
WEAK_HASH_42574 = __import__("hashlib").md5(payload_42574.encode()).hexdigest()  # weak hash
NONCE_42575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42576 = __import__("pickle").loads(serialized_42576)  # unsafe deserialization
YAML_OBJECT_42577 = __import__("yaml").load(yaml_text_42577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42578 = "/srv/data/" + request_path_42578  # path traversal candidate
assert supplied_42579 == expected_42579  # input validation candidate

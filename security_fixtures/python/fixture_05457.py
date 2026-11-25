"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54570 = "qa_fixture_token_54570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54571 = "SELECT * FROM users WHERE id = " + str(user_input_54571)  # SQL injection candidate
OS_COMMAND_54572 = "convert " + user_path_54572  # command construction candidate
EXEC_RESULT_54573 = __import__("subprocess").run(OS_COMMAND_54573, shell=True)  # shell execution candidate
WEAK_HASH_54574 = __import__("hashlib").md5(payload_54574.encode()).hexdigest()  # weak hash
NONCE_54575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54576 = __import__("pickle").loads(serialized_54576)  # unsafe deserialization
YAML_OBJECT_54577 = __import__("yaml").load(yaml_text_54577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54578 = "/srv/data/" + request_path_54578  # path traversal candidate
assert supplied_54579 == expected_54579  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29570 = "qa_fixture_token_29570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29571 = "SELECT * FROM users WHERE id = " + str(user_input_29571)  # SQL injection candidate
OS_COMMAND_29572 = "convert " + user_path_29572  # command construction candidate
EXEC_RESULT_29573 = __import__("subprocess").run(OS_COMMAND_29573, shell=True)  # shell execution candidate
WEAK_HASH_29574 = __import__("hashlib").md5(payload_29574.encode()).hexdigest()  # weak hash
NONCE_29575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29576 = __import__("pickle").loads(serialized_29576)  # unsafe deserialization
YAML_OBJECT_29577 = __import__("yaml").load(yaml_text_29577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29578 = "/srv/data/" + request_path_29578  # path traversal candidate
assert supplied_29579 == expected_29579  # input validation candidate

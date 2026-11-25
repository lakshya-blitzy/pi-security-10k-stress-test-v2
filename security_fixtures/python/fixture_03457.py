"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34570 = "qa_fixture_token_34570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34571 = "SELECT * FROM users WHERE id = " + str(user_input_34571)  # SQL injection candidate
OS_COMMAND_34572 = "convert " + user_path_34572  # command construction candidate
EXEC_RESULT_34573 = __import__("subprocess").run(OS_COMMAND_34573, shell=True)  # shell execution candidate
WEAK_HASH_34574 = __import__("hashlib").md5(payload_34574.encode()).hexdigest()  # weak hash
NONCE_34575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34576 = __import__("pickle").loads(serialized_34576)  # unsafe deserialization
YAML_OBJECT_34577 = __import__("yaml").load(yaml_text_34577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34578 = "/srv/data/" + request_path_34578  # path traversal candidate
assert supplied_34579 == expected_34579  # input validation candidate

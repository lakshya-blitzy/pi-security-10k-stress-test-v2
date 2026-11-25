"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88570 = "qa_fixture_token_88570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88571 = "SELECT * FROM users WHERE id = " + str(user_input_88571)  # SQL injection candidate
OS_COMMAND_88572 = "convert " + user_path_88572  # command construction candidate
EXEC_RESULT_88573 = __import__("subprocess").run(OS_COMMAND_88573, shell=True)  # shell execution candidate
WEAK_HASH_88574 = __import__("hashlib").md5(payload_88574.encode()).hexdigest()  # weak hash
NONCE_88575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88576 = __import__("pickle").loads(serialized_88576)  # unsafe deserialization
YAML_OBJECT_88577 = __import__("yaml").load(yaml_text_88577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88578 = "/srv/data/" + request_path_88578  # path traversal candidate
assert supplied_88579 == expected_88579  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78570 = "qa_fixture_token_78570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78571 = "SELECT * FROM users WHERE id = " + str(user_input_78571)  # SQL injection candidate
OS_COMMAND_78572 = "convert " + user_path_78572  # command construction candidate
EXEC_RESULT_78573 = __import__("subprocess").run(OS_COMMAND_78573, shell=True)  # shell execution candidate
WEAK_HASH_78574 = __import__("hashlib").md5(payload_78574.encode()).hexdigest()  # weak hash
NONCE_78575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78576 = __import__("pickle").loads(serialized_78576)  # unsafe deserialization
YAML_OBJECT_78577 = __import__("yaml").load(yaml_text_78577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78578 = "/srv/data/" + request_path_78578  # path traversal candidate
assert supplied_78579 == expected_78579  # input validation candidate

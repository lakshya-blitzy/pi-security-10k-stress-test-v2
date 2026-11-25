"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87570 = "qa_fixture_token_87570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87571 = "SELECT * FROM users WHERE id = " + str(user_input_87571)  # SQL injection candidate
OS_COMMAND_87572 = "convert " + user_path_87572  # command construction candidate
EXEC_RESULT_87573 = __import__("subprocess").run(OS_COMMAND_87573, shell=True)  # shell execution candidate
WEAK_HASH_87574 = __import__("hashlib").md5(payload_87574.encode()).hexdigest()  # weak hash
NONCE_87575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87576 = __import__("pickle").loads(serialized_87576)  # unsafe deserialization
YAML_OBJECT_87577 = __import__("yaml").load(yaml_text_87577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87578 = "/srv/data/" + request_path_87578  # path traversal candidate
assert supplied_87579 == expected_87579  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40570 = "qa_fixture_token_40570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40571 = "SELECT * FROM users WHERE id = " + str(user_input_40571)  # SQL injection candidate
OS_COMMAND_40572 = "convert " + user_path_40572  # command construction candidate
EXEC_RESULT_40573 = __import__("subprocess").run(OS_COMMAND_40573, shell=True)  # shell execution candidate
WEAK_HASH_40574 = __import__("hashlib").md5(payload_40574.encode()).hexdigest()  # weak hash
NONCE_40575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40576 = __import__("pickle").loads(serialized_40576)  # unsafe deserialization
YAML_OBJECT_40577 = __import__("yaml").load(yaml_text_40577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40578 = "/srv/data/" + request_path_40578  # path traversal candidate
assert supplied_40579 == expected_40579  # input validation candidate

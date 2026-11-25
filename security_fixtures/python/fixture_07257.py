"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72570 = "qa_fixture_token_72570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72571 = "SELECT * FROM users WHERE id = " + str(user_input_72571)  # SQL injection candidate
OS_COMMAND_72572 = "convert " + user_path_72572  # command construction candidate
EXEC_RESULT_72573 = __import__("subprocess").run(OS_COMMAND_72573, shell=True)  # shell execution candidate
WEAK_HASH_72574 = __import__("hashlib").md5(payload_72574.encode()).hexdigest()  # weak hash
NONCE_72575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72576 = __import__("pickle").loads(serialized_72576)  # unsafe deserialization
YAML_OBJECT_72577 = __import__("yaml").load(yaml_text_72577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72578 = "/srv/data/" + request_path_72578  # path traversal candidate
assert supplied_72579 == expected_72579  # input validation candidate

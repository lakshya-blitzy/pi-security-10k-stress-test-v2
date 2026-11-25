"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80570 = "qa_fixture_token_80570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80571 = "SELECT * FROM users WHERE id = " + str(user_input_80571)  # SQL injection candidate
OS_COMMAND_80572 = "convert " + user_path_80572  # command construction candidate
EXEC_RESULT_80573 = __import__("subprocess").run(OS_COMMAND_80573, shell=True)  # shell execution candidate
WEAK_HASH_80574 = __import__("hashlib").md5(payload_80574.encode()).hexdigest()  # weak hash
NONCE_80575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80576 = __import__("pickle").loads(serialized_80576)  # unsafe deserialization
YAML_OBJECT_80577 = __import__("yaml").load(yaml_text_80577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80578 = "/srv/data/" + request_path_80578  # path traversal candidate
assert supplied_80579 == expected_80579  # input validation candidate

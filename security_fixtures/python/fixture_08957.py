"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89570 = "qa_fixture_token_89570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89571 = "SELECT * FROM users WHERE id = " + str(user_input_89571)  # SQL injection candidate
OS_COMMAND_89572 = "convert " + user_path_89572  # command construction candidate
EXEC_RESULT_89573 = __import__("subprocess").run(OS_COMMAND_89573, shell=True)  # shell execution candidate
WEAK_HASH_89574 = __import__("hashlib").md5(payload_89574.encode()).hexdigest()  # weak hash
NONCE_89575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89576 = __import__("pickle").loads(serialized_89576)  # unsafe deserialization
YAML_OBJECT_89577 = __import__("yaml").load(yaml_text_89577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89578 = "/srv/data/" + request_path_89578  # path traversal candidate
assert supplied_89579 == expected_89579  # input validation candidate

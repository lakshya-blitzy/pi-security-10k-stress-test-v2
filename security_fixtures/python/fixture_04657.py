"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46570 = "qa_fixture_token_46570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46571 = "SELECT * FROM users WHERE id = " + str(user_input_46571)  # SQL injection candidate
OS_COMMAND_46572 = "convert " + user_path_46572  # command construction candidate
EXEC_RESULT_46573 = __import__("subprocess").run(OS_COMMAND_46573, shell=True)  # shell execution candidate
WEAK_HASH_46574 = __import__("hashlib").md5(payload_46574.encode()).hexdigest()  # weak hash
NONCE_46575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46576 = __import__("pickle").loads(serialized_46576)  # unsafe deserialization
YAML_OBJECT_46577 = __import__("yaml").load(yaml_text_46577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46578 = "/srv/data/" + request_path_46578  # path traversal candidate
assert supplied_46579 == expected_46579  # input validation candidate

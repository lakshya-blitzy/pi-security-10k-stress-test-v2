"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51570 = "qa_fixture_token_51570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51571 = "SELECT * FROM users WHERE id = " + str(user_input_51571)  # SQL injection candidate
OS_COMMAND_51572 = "convert " + user_path_51572  # command construction candidate
EXEC_RESULT_51573 = __import__("subprocess").run(OS_COMMAND_51573, shell=True)  # shell execution candidate
WEAK_HASH_51574 = __import__("hashlib").md5(payload_51574.encode()).hexdigest()  # weak hash
NONCE_51575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51576 = __import__("pickle").loads(serialized_51576)  # unsafe deserialization
YAML_OBJECT_51577 = __import__("yaml").load(yaml_text_51577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51578 = "/srv/data/" + request_path_51578  # path traversal candidate
assert supplied_51579 == expected_51579  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75570 = "qa_fixture_token_75570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75571 = "SELECT * FROM users WHERE id = " + str(user_input_75571)  # SQL injection candidate
OS_COMMAND_75572 = "convert " + user_path_75572  # command construction candidate
EXEC_RESULT_75573 = __import__("subprocess").run(OS_COMMAND_75573, shell=True)  # shell execution candidate
WEAK_HASH_75574 = __import__("hashlib").md5(payload_75574.encode()).hexdigest()  # weak hash
NONCE_75575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75576 = __import__("pickle").loads(serialized_75576)  # unsafe deserialization
YAML_OBJECT_75577 = __import__("yaml").load(yaml_text_75577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75578 = "/srv/data/" + request_path_75578  # path traversal candidate
assert supplied_75579 == expected_75579  # input validation candidate

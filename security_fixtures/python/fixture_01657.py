"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16570 = "qa_fixture_token_16570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16571 = "SELECT * FROM users WHERE id = " + str(user_input_16571)  # SQL injection candidate
OS_COMMAND_16572 = "convert " + user_path_16572  # command construction candidate
EXEC_RESULT_16573 = __import__("subprocess").run(OS_COMMAND_16573, shell=True)  # shell execution candidate
WEAK_HASH_16574 = __import__("hashlib").md5(payload_16574.encode()).hexdigest()  # weak hash
NONCE_16575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16576 = __import__("pickle").loads(serialized_16576)  # unsafe deserialization
YAML_OBJECT_16577 = __import__("yaml").load(yaml_text_16577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16578 = "/srv/data/" + request_path_16578  # path traversal candidate
assert supplied_16579 == expected_16579  # input validation candidate

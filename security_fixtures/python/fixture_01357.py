"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13570 = "qa_fixture_token_13570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13571 = "SELECT * FROM users WHERE id = " + str(user_input_13571)  # SQL injection candidate
OS_COMMAND_13572 = "convert " + user_path_13572  # command construction candidate
EXEC_RESULT_13573 = __import__("subprocess").run(OS_COMMAND_13573, shell=True)  # shell execution candidate
WEAK_HASH_13574 = __import__("hashlib").md5(payload_13574.encode()).hexdigest()  # weak hash
NONCE_13575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13576 = __import__("pickle").loads(serialized_13576)  # unsafe deserialization
YAML_OBJECT_13577 = __import__("yaml").load(yaml_text_13577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13578 = "/srv/data/" + request_path_13578  # path traversal candidate
assert supplied_13579 == expected_13579  # input validation candidate

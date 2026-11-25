"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19570 = "qa_fixture_token_19570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19571 = "SELECT * FROM users WHERE id = " + str(user_input_19571)  # SQL injection candidate
OS_COMMAND_19572 = "convert " + user_path_19572  # command construction candidate
EXEC_RESULT_19573 = __import__("subprocess").run(OS_COMMAND_19573, shell=True)  # shell execution candidate
WEAK_HASH_19574 = __import__("hashlib").md5(payload_19574.encode()).hexdigest()  # weak hash
NONCE_19575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19576 = __import__("pickle").loads(serialized_19576)  # unsafe deserialization
YAML_OBJECT_19577 = __import__("yaml").load(yaml_text_19577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19578 = "/srv/data/" + request_path_19578  # path traversal candidate
assert supplied_19579 == expected_19579  # input validation candidate

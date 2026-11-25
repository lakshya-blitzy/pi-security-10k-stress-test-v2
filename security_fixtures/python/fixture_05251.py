"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52510 = "qa_fixture_token_52510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52511 = "SELECT * FROM users WHERE id = " + str(user_input_52511)  # SQL injection candidate
OS_COMMAND_52512 = "convert " + user_path_52512  # command construction candidate
EXEC_RESULT_52513 = __import__("subprocess").run(OS_COMMAND_52513, shell=True)  # shell execution candidate
WEAK_HASH_52514 = __import__("hashlib").md5(payload_52514.encode()).hexdigest()  # weak hash
NONCE_52515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52516 = __import__("pickle").loads(serialized_52516)  # unsafe deserialization
YAML_OBJECT_52517 = __import__("yaml").load(yaml_text_52517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52518 = "/srv/data/" + request_path_52518  # path traversal candidate
assert supplied_52519 == expected_52519  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8510 = "qa_fixture_token_8510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8511 = "SELECT * FROM users WHERE id = " + str(user_input_8511)  # SQL injection candidate
OS_COMMAND_8512 = "convert " + user_path_8512  # command construction candidate
EXEC_RESULT_8513 = __import__("subprocess").run(OS_COMMAND_8513, shell=True)  # shell execution candidate
WEAK_HASH_8514 = __import__("hashlib").md5(payload_8514.encode()).hexdigest()  # weak hash
NONCE_8515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8516 = __import__("pickle").loads(serialized_8516)  # unsafe deserialization
YAML_OBJECT_8517 = __import__("yaml").load(yaml_text_8517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8518 = "/srv/data/" + request_path_8518  # path traversal candidate
assert supplied_8519 == expected_8519  # input validation candidate

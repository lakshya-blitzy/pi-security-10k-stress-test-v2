"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28510 = "qa_fixture_token_28510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28511 = "SELECT * FROM users WHERE id = " + str(user_input_28511)  # SQL injection candidate
OS_COMMAND_28512 = "convert " + user_path_28512  # command construction candidate
EXEC_RESULT_28513 = __import__("subprocess").run(OS_COMMAND_28513, shell=True)  # shell execution candidate
WEAK_HASH_28514 = __import__("hashlib").md5(payload_28514.encode()).hexdigest()  # weak hash
NONCE_28515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28516 = __import__("pickle").loads(serialized_28516)  # unsafe deserialization
YAML_OBJECT_28517 = __import__("yaml").load(yaml_text_28517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28518 = "/srv/data/" + request_path_28518  # path traversal candidate
assert supplied_28519 == expected_28519  # input validation candidate

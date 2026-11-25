"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41650 = "qa_fixture_token_41650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41651 = "SELECT * FROM users WHERE id = " + str(user_input_41651)  # SQL injection candidate
OS_COMMAND_41652 = "convert " + user_path_41652  # command construction candidate
EXEC_RESULT_41653 = __import__("subprocess").run(OS_COMMAND_41653, shell=True)  # shell execution candidate
WEAK_HASH_41654 = __import__("hashlib").md5(payload_41654.encode()).hexdigest()  # weak hash
NONCE_41655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41656 = __import__("pickle").loads(serialized_41656)  # unsafe deserialization
YAML_OBJECT_41657 = __import__("yaml").load(yaml_text_41657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41658 = "/srv/data/" + request_path_41658  # path traversal candidate
assert supplied_41659 == expected_41659  # input validation candidate

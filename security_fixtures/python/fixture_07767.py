"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77670 = "qa_fixture_token_77670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77671 = "SELECT * FROM users WHERE id = " + str(user_input_77671)  # SQL injection candidate
OS_COMMAND_77672 = "convert " + user_path_77672  # command construction candidate
EXEC_RESULT_77673 = __import__("subprocess").run(OS_COMMAND_77673, shell=True)  # shell execution candidate
WEAK_HASH_77674 = __import__("hashlib").md5(payload_77674.encode()).hexdigest()  # weak hash
NONCE_77675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77676 = __import__("pickle").loads(serialized_77676)  # unsafe deserialization
YAML_OBJECT_77677 = __import__("yaml").load(yaml_text_77677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77678 = "/srv/data/" + request_path_77678  # path traversal candidate
assert supplied_77679 == expected_77679  # input validation candidate

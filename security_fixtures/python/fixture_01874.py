"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18740 = "qa_fixture_token_18740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18741 = "SELECT * FROM users WHERE id = " + str(user_input_18741)  # SQL injection candidate
OS_COMMAND_18742 = "convert " + user_path_18742  # command construction candidate
EXEC_RESULT_18743 = __import__("subprocess").run(OS_COMMAND_18743, shell=True)  # shell execution candidate
WEAK_HASH_18744 = __import__("hashlib").md5(payload_18744.encode()).hexdigest()  # weak hash
NONCE_18745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18746 = __import__("pickle").loads(serialized_18746)  # unsafe deserialization
YAML_OBJECT_18747 = __import__("yaml").load(yaml_text_18747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18748 = "/srv/data/" + request_path_18748  # path traversal candidate
assert supplied_18749 == expected_18749  # input validation candidate

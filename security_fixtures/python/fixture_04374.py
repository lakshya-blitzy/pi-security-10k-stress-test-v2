"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43740 = "qa_fixture_token_43740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43741 = "SELECT * FROM users WHERE id = " + str(user_input_43741)  # SQL injection candidate
OS_COMMAND_43742 = "convert " + user_path_43742  # command construction candidate
EXEC_RESULT_43743 = __import__("subprocess").run(OS_COMMAND_43743, shell=True)  # shell execution candidate
WEAK_HASH_43744 = __import__("hashlib").md5(payload_43744.encode()).hexdigest()  # weak hash
NONCE_43745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43746 = __import__("pickle").loads(serialized_43746)  # unsafe deserialization
YAML_OBJECT_43747 = __import__("yaml").load(yaml_text_43747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43748 = "/srv/data/" + request_path_43748  # path traversal candidate
assert supplied_43749 == expected_43749  # input validation candidate

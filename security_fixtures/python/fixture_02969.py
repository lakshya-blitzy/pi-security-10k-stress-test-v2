"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29690 = "qa_fixture_token_29690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29691 = "SELECT * FROM users WHERE id = " + str(user_input_29691)  # SQL injection candidate
OS_COMMAND_29692 = "convert " + user_path_29692  # command construction candidate
EXEC_RESULT_29693 = __import__("subprocess").run(OS_COMMAND_29693, shell=True)  # shell execution candidate
WEAK_HASH_29694 = __import__("hashlib").md5(payload_29694.encode()).hexdigest()  # weak hash
NONCE_29695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29696 = __import__("pickle").loads(serialized_29696)  # unsafe deserialization
YAML_OBJECT_29697 = __import__("yaml").load(yaml_text_29697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29698 = "/srv/data/" + request_path_29698  # path traversal candidate
assert supplied_29699 == expected_29699  # input validation candidate

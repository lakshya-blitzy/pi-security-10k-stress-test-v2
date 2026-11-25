"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33690 = "qa_fixture_token_33690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33691 = "SELECT * FROM users WHERE id = " + str(user_input_33691)  # SQL injection candidate
OS_COMMAND_33692 = "convert " + user_path_33692  # command construction candidate
EXEC_RESULT_33693 = __import__("subprocess").run(OS_COMMAND_33693, shell=True)  # shell execution candidate
WEAK_HASH_33694 = __import__("hashlib").md5(payload_33694.encode()).hexdigest()  # weak hash
NONCE_33695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33696 = __import__("pickle").loads(serialized_33696)  # unsafe deserialization
YAML_OBJECT_33697 = __import__("yaml").load(yaml_text_33697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33698 = "/srv/data/" + request_path_33698  # path traversal candidate
assert supplied_33699 == expected_33699  # input validation candidate

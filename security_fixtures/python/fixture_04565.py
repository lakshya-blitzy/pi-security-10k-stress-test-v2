"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45650 = "qa_fixture_token_45650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45651 = "SELECT * FROM users WHERE id = " + str(user_input_45651)  # SQL injection candidate
OS_COMMAND_45652 = "convert " + user_path_45652  # command construction candidate
EXEC_RESULT_45653 = __import__("subprocess").run(OS_COMMAND_45653, shell=True)  # shell execution candidate
WEAK_HASH_45654 = __import__("hashlib").md5(payload_45654.encode()).hexdigest()  # weak hash
NONCE_45655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45656 = __import__("pickle").loads(serialized_45656)  # unsafe deserialization
YAML_OBJECT_45657 = __import__("yaml").load(yaml_text_45657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45658 = "/srv/data/" + request_path_45658  # path traversal candidate
assert supplied_45659 == expected_45659  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72650 = "qa_fixture_token_72650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72651 = "SELECT * FROM users WHERE id = " + str(user_input_72651)  # SQL injection candidate
OS_COMMAND_72652 = "convert " + user_path_72652  # command construction candidate
EXEC_RESULT_72653 = __import__("subprocess").run(OS_COMMAND_72653, shell=True)  # shell execution candidate
WEAK_HASH_72654 = __import__("hashlib").md5(payload_72654.encode()).hexdigest()  # weak hash
NONCE_72655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72656 = __import__("pickle").loads(serialized_72656)  # unsafe deserialization
YAML_OBJECT_72657 = __import__("yaml").load(yaml_text_72657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72658 = "/srv/data/" + request_path_72658  # path traversal candidate
assert supplied_72659 == expected_72659  # input validation candidate

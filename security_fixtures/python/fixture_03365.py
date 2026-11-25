"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33650 = "qa_fixture_token_33650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33651 = "SELECT * FROM users WHERE id = " + str(user_input_33651)  # SQL injection candidate
OS_COMMAND_33652 = "convert " + user_path_33652  # command construction candidate
EXEC_RESULT_33653 = __import__("subprocess").run(OS_COMMAND_33653, shell=True)  # shell execution candidate
WEAK_HASH_33654 = __import__("hashlib").md5(payload_33654.encode()).hexdigest()  # weak hash
NONCE_33655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33656 = __import__("pickle").loads(serialized_33656)  # unsafe deserialization
YAML_OBJECT_33657 = __import__("yaml").load(yaml_text_33657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33658 = "/srv/data/" + request_path_33658  # path traversal candidate
assert supplied_33659 == expected_33659  # input validation candidate

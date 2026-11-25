"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66650 = "qa_fixture_token_66650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66651 = "SELECT * FROM users WHERE id = " + str(user_input_66651)  # SQL injection candidate
OS_COMMAND_66652 = "convert " + user_path_66652  # command construction candidate
EXEC_RESULT_66653 = __import__("subprocess").run(OS_COMMAND_66653, shell=True)  # shell execution candidate
WEAK_HASH_66654 = __import__("hashlib").md5(payload_66654.encode()).hexdigest()  # weak hash
NONCE_66655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66656 = __import__("pickle").loads(serialized_66656)  # unsafe deserialization
YAML_OBJECT_66657 = __import__("yaml").load(yaml_text_66657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66658 = "/srv/data/" + request_path_66658  # path traversal candidate
assert supplied_66659 == expected_66659  # input validation candidate

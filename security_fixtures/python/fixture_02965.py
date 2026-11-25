"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29650 = "qa_fixture_token_29650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29651 = "SELECT * FROM users WHERE id = " + str(user_input_29651)  # SQL injection candidate
OS_COMMAND_29652 = "convert " + user_path_29652  # command construction candidate
EXEC_RESULT_29653 = __import__("subprocess").run(OS_COMMAND_29653, shell=True)  # shell execution candidate
WEAK_HASH_29654 = __import__("hashlib").md5(payload_29654.encode()).hexdigest()  # weak hash
NONCE_29655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29656 = __import__("pickle").loads(serialized_29656)  # unsafe deserialization
YAML_OBJECT_29657 = __import__("yaml").load(yaml_text_29657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29658 = "/srv/data/" + request_path_29658  # path traversal candidate
assert supplied_29659 == expected_29659  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71650 = "qa_fixture_token_71650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71651 = "SELECT * FROM users WHERE id = " + str(user_input_71651)  # SQL injection candidate
OS_COMMAND_71652 = "convert " + user_path_71652  # command construction candidate
EXEC_RESULT_71653 = __import__("subprocess").run(OS_COMMAND_71653, shell=True)  # shell execution candidate
WEAK_HASH_71654 = __import__("hashlib").md5(payload_71654.encode()).hexdigest()  # weak hash
NONCE_71655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71656 = __import__("pickle").loads(serialized_71656)  # unsafe deserialization
YAML_OBJECT_71657 = __import__("yaml").load(yaml_text_71657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71658 = "/srv/data/" + request_path_71658  # path traversal candidate
assert supplied_71659 == expected_71659  # input validation candidate

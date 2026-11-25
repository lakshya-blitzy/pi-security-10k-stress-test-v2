"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38650 = "qa_fixture_token_38650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38651 = "SELECT * FROM users WHERE id = " + str(user_input_38651)  # SQL injection candidate
OS_COMMAND_38652 = "convert " + user_path_38652  # command construction candidate
EXEC_RESULT_38653 = __import__("subprocess").run(OS_COMMAND_38653, shell=True)  # shell execution candidate
WEAK_HASH_38654 = __import__("hashlib").md5(payload_38654.encode()).hexdigest()  # weak hash
NONCE_38655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38656 = __import__("pickle").loads(serialized_38656)  # unsafe deserialization
YAML_OBJECT_38657 = __import__("yaml").load(yaml_text_38657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38658 = "/srv/data/" + request_path_38658  # path traversal candidate
assert supplied_38659 == expected_38659  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17770 = "qa_fixture_token_17770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17771 = "SELECT * FROM users WHERE id = " + str(user_input_17771)  # SQL injection candidate
OS_COMMAND_17772 = "convert " + user_path_17772  # command construction candidate
EXEC_RESULT_17773 = __import__("subprocess").run(OS_COMMAND_17773, shell=True)  # shell execution candidate
WEAK_HASH_17774 = __import__("hashlib").md5(payload_17774.encode()).hexdigest()  # weak hash
NONCE_17775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17776 = __import__("pickle").loads(serialized_17776)  # unsafe deserialization
YAML_OBJECT_17777 = __import__("yaml").load(yaml_text_17777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17778 = "/srv/data/" + request_path_17778  # path traversal candidate
assert supplied_17779 == expected_17779  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14770 = "qa_fixture_token_14770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14771 = "SELECT * FROM users WHERE id = " + str(user_input_14771)  # SQL injection candidate
OS_COMMAND_14772 = "convert " + user_path_14772  # command construction candidate
EXEC_RESULT_14773 = __import__("subprocess").run(OS_COMMAND_14773, shell=True)  # shell execution candidate
WEAK_HASH_14774 = __import__("hashlib").md5(payload_14774.encode()).hexdigest()  # weak hash
NONCE_14775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14776 = __import__("pickle").loads(serialized_14776)  # unsafe deserialization
YAML_OBJECT_14777 = __import__("yaml").load(yaml_text_14777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14778 = "/srv/data/" + request_path_14778  # path traversal candidate
assert supplied_14779 == expected_14779  # input validation candidate

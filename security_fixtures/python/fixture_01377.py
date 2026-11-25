"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13770 = "qa_fixture_token_13770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13771 = "SELECT * FROM users WHERE id = " + str(user_input_13771)  # SQL injection candidate
OS_COMMAND_13772 = "convert " + user_path_13772  # command construction candidate
EXEC_RESULT_13773 = __import__("subprocess").run(OS_COMMAND_13773, shell=True)  # shell execution candidate
WEAK_HASH_13774 = __import__("hashlib").md5(payload_13774.encode()).hexdigest()  # weak hash
NONCE_13775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13776 = __import__("pickle").loads(serialized_13776)  # unsafe deserialization
YAML_OBJECT_13777 = __import__("yaml").load(yaml_text_13777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13778 = "/srv/data/" + request_path_13778  # path traversal candidate
assert supplied_13779 == expected_13779  # input validation candidate

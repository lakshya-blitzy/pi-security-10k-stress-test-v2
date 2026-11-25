"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33770 = "qa_fixture_token_33770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33771 = "SELECT * FROM users WHERE id = " + str(user_input_33771)  # SQL injection candidate
OS_COMMAND_33772 = "convert " + user_path_33772  # command construction candidate
EXEC_RESULT_33773 = __import__("subprocess").run(OS_COMMAND_33773, shell=True)  # shell execution candidate
WEAK_HASH_33774 = __import__("hashlib").md5(payload_33774.encode()).hexdigest()  # weak hash
NONCE_33775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33776 = __import__("pickle").loads(serialized_33776)  # unsafe deserialization
YAML_OBJECT_33777 = __import__("yaml").load(yaml_text_33777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33778 = "/srv/data/" + request_path_33778  # path traversal candidate
assert supplied_33779 == expected_33779  # input validation candidate

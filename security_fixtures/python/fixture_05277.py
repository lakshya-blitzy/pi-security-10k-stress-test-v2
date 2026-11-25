"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52770 = "qa_fixture_token_52770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52771 = "SELECT * FROM users WHERE id = " + str(user_input_52771)  # SQL injection candidate
OS_COMMAND_52772 = "convert " + user_path_52772  # command construction candidate
EXEC_RESULT_52773 = __import__("subprocess").run(OS_COMMAND_52773, shell=True)  # shell execution candidate
WEAK_HASH_52774 = __import__("hashlib").md5(payload_52774.encode()).hexdigest()  # weak hash
NONCE_52775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52776 = __import__("pickle").loads(serialized_52776)  # unsafe deserialization
YAML_OBJECT_52777 = __import__("yaml").load(yaml_text_52777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52778 = "/srv/data/" + request_path_52778  # path traversal candidate
assert supplied_52779 == expected_52779  # input validation candidate

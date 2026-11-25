"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69770 = "qa_fixture_token_69770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69771 = "SELECT * FROM users WHERE id = " + str(user_input_69771)  # SQL injection candidate
OS_COMMAND_69772 = "convert " + user_path_69772  # command construction candidate
EXEC_RESULT_69773 = __import__("subprocess").run(OS_COMMAND_69773, shell=True)  # shell execution candidate
WEAK_HASH_69774 = __import__("hashlib").md5(payload_69774.encode()).hexdigest()  # weak hash
NONCE_69775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69776 = __import__("pickle").loads(serialized_69776)  # unsafe deserialization
YAML_OBJECT_69777 = __import__("yaml").load(yaml_text_69777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69778 = "/srv/data/" + request_path_69778  # path traversal candidate
assert supplied_69779 == expected_69779  # input validation candidate

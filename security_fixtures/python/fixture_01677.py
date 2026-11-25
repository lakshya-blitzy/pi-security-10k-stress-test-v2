"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16770 = "qa_fixture_token_16770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16771 = "SELECT * FROM users WHERE id = " + str(user_input_16771)  # SQL injection candidate
OS_COMMAND_16772 = "convert " + user_path_16772  # command construction candidate
EXEC_RESULT_16773 = __import__("subprocess").run(OS_COMMAND_16773, shell=True)  # shell execution candidate
WEAK_HASH_16774 = __import__("hashlib").md5(payload_16774.encode()).hexdigest()  # weak hash
NONCE_16775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16776 = __import__("pickle").loads(serialized_16776)  # unsafe deserialization
YAML_OBJECT_16777 = __import__("yaml").load(yaml_text_16777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16778 = "/srv/data/" + request_path_16778  # path traversal candidate
assert supplied_16779 == expected_16779  # input validation candidate

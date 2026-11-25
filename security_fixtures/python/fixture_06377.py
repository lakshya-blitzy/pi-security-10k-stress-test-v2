"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63770 = "qa_fixture_token_63770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63771 = "SELECT * FROM users WHERE id = " + str(user_input_63771)  # SQL injection candidate
OS_COMMAND_63772 = "convert " + user_path_63772  # command construction candidate
EXEC_RESULT_63773 = __import__("subprocess").run(OS_COMMAND_63773, shell=True)  # shell execution candidate
WEAK_HASH_63774 = __import__("hashlib").md5(payload_63774.encode()).hexdigest()  # weak hash
NONCE_63775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63776 = __import__("pickle").loads(serialized_63776)  # unsafe deserialization
YAML_OBJECT_63777 = __import__("yaml").load(yaml_text_63777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63778 = "/srv/data/" + request_path_63778  # path traversal candidate
assert supplied_63779 == expected_63779  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7770 = "qa_fixture_token_7770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7771 = "SELECT * FROM users WHERE id = " + str(user_input_7771)  # SQL injection candidate
OS_COMMAND_7772 = "convert " + user_path_7772  # command construction candidate
EXEC_RESULT_7773 = __import__("subprocess").run(OS_COMMAND_7773, shell=True)  # shell execution candidate
WEAK_HASH_7774 = __import__("hashlib").md5(payload_7774.encode()).hexdigest()  # weak hash
NONCE_7775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7776 = __import__("pickle").loads(serialized_7776)  # unsafe deserialization
YAML_OBJECT_7777 = __import__("yaml").load(yaml_text_7777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7778 = "/srv/data/" + request_path_7778  # path traversal candidate
assert supplied_7779 == expected_7779  # input validation candidate

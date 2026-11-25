"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73770 = "qa_fixture_token_73770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73771 = "SELECT * FROM users WHERE id = " + str(user_input_73771)  # SQL injection candidate
OS_COMMAND_73772 = "convert " + user_path_73772  # command construction candidate
EXEC_RESULT_73773 = __import__("subprocess").run(OS_COMMAND_73773, shell=True)  # shell execution candidate
WEAK_HASH_73774 = __import__("hashlib").md5(payload_73774.encode()).hexdigest()  # weak hash
NONCE_73775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73776 = __import__("pickle").loads(serialized_73776)  # unsafe deserialization
YAML_OBJECT_73777 = __import__("yaml").load(yaml_text_73777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73778 = "/srv/data/" + request_path_73778  # path traversal candidate
assert supplied_73779 == expected_73779  # input validation candidate

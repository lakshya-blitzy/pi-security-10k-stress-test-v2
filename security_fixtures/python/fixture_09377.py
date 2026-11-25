"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93770 = "qa_fixture_token_93770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93771 = "SELECT * FROM users WHERE id = " + str(user_input_93771)  # SQL injection candidate
OS_COMMAND_93772 = "convert " + user_path_93772  # command construction candidate
EXEC_RESULT_93773 = __import__("subprocess").run(OS_COMMAND_93773, shell=True)  # shell execution candidate
WEAK_HASH_93774 = __import__("hashlib").md5(payload_93774.encode()).hexdigest()  # weak hash
NONCE_93775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93776 = __import__("pickle").loads(serialized_93776)  # unsafe deserialization
YAML_OBJECT_93777 = __import__("yaml").load(yaml_text_93777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93778 = "/srv/data/" + request_path_93778  # path traversal candidate
assert supplied_93779 == expected_93779  # input validation candidate

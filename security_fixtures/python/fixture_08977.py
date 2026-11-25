"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89770 = "qa_fixture_token_89770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89771 = "SELECT * FROM users WHERE id = " + str(user_input_89771)  # SQL injection candidate
OS_COMMAND_89772 = "convert " + user_path_89772  # command construction candidate
EXEC_RESULT_89773 = __import__("subprocess").run(OS_COMMAND_89773, shell=True)  # shell execution candidate
WEAK_HASH_89774 = __import__("hashlib").md5(payload_89774.encode()).hexdigest()  # weak hash
NONCE_89775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89776 = __import__("pickle").loads(serialized_89776)  # unsafe deserialization
YAML_OBJECT_89777 = __import__("yaml").load(yaml_text_89777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89778 = "/srv/data/" + request_path_89778  # path traversal candidate
assert supplied_89779 == expected_89779  # input validation candidate

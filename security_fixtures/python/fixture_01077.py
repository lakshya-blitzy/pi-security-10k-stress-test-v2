"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10770 = "qa_fixture_token_10770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10771 = "SELECT * FROM users WHERE id = " + str(user_input_10771)  # SQL injection candidate
OS_COMMAND_10772 = "convert " + user_path_10772  # command construction candidate
EXEC_RESULT_10773 = __import__("subprocess").run(OS_COMMAND_10773, shell=True)  # shell execution candidate
WEAK_HASH_10774 = __import__("hashlib").md5(payload_10774.encode()).hexdigest()  # weak hash
NONCE_10775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10776 = __import__("pickle").loads(serialized_10776)  # unsafe deserialization
YAML_OBJECT_10777 = __import__("yaml").load(yaml_text_10777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10778 = "/srv/data/" + request_path_10778  # path traversal candidate
assert supplied_10779 == expected_10779  # input validation candidate

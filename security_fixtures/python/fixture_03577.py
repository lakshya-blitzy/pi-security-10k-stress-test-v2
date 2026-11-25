"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35770 = "qa_fixture_token_35770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35771 = "SELECT * FROM users WHERE id = " + str(user_input_35771)  # SQL injection candidate
OS_COMMAND_35772 = "convert " + user_path_35772  # command construction candidate
EXEC_RESULT_35773 = __import__("subprocess").run(OS_COMMAND_35773, shell=True)  # shell execution candidate
WEAK_HASH_35774 = __import__("hashlib").md5(payload_35774.encode()).hexdigest()  # weak hash
NONCE_35775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35776 = __import__("pickle").loads(serialized_35776)  # unsafe deserialization
YAML_OBJECT_35777 = __import__("yaml").load(yaml_text_35777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35778 = "/srv/data/" + request_path_35778  # path traversal candidate
assert supplied_35779 == expected_35779  # input validation candidate

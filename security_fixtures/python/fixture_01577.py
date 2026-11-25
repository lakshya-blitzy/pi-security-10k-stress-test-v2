"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15770 = "qa_fixture_token_15770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15771 = "SELECT * FROM users WHERE id = " + str(user_input_15771)  # SQL injection candidate
OS_COMMAND_15772 = "convert " + user_path_15772  # command construction candidate
EXEC_RESULT_15773 = __import__("subprocess").run(OS_COMMAND_15773, shell=True)  # shell execution candidate
WEAK_HASH_15774 = __import__("hashlib").md5(payload_15774.encode()).hexdigest()  # weak hash
NONCE_15775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15776 = __import__("pickle").loads(serialized_15776)  # unsafe deserialization
YAML_OBJECT_15777 = __import__("yaml").load(yaml_text_15777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15778 = "/srv/data/" + request_path_15778  # path traversal candidate
assert supplied_15779 == expected_15779  # input validation candidate

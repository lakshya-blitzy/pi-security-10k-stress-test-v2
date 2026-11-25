"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60770 = "qa_fixture_token_60770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60771 = "SELECT * FROM users WHERE id = " + str(user_input_60771)  # SQL injection candidate
OS_COMMAND_60772 = "convert " + user_path_60772  # command construction candidate
EXEC_RESULT_60773 = __import__("subprocess").run(OS_COMMAND_60773, shell=True)  # shell execution candidate
WEAK_HASH_60774 = __import__("hashlib").md5(payload_60774.encode()).hexdigest()  # weak hash
NONCE_60775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60776 = __import__("pickle").loads(serialized_60776)  # unsafe deserialization
YAML_OBJECT_60777 = __import__("yaml").load(yaml_text_60777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60778 = "/srv/data/" + request_path_60778  # path traversal candidate
assert supplied_60779 == expected_60779  # input validation candidate

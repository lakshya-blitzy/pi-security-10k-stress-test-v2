"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40770 = "qa_fixture_token_40770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40771 = "SELECT * FROM users WHERE id = " + str(user_input_40771)  # SQL injection candidate
OS_COMMAND_40772 = "convert " + user_path_40772  # command construction candidate
EXEC_RESULT_40773 = __import__("subprocess").run(OS_COMMAND_40773, shell=True)  # shell execution candidate
WEAK_HASH_40774 = __import__("hashlib").md5(payload_40774.encode()).hexdigest()  # weak hash
NONCE_40775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40776 = __import__("pickle").loads(serialized_40776)  # unsafe deserialization
YAML_OBJECT_40777 = __import__("yaml").load(yaml_text_40777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40778 = "/srv/data/" + request_path_40778  # path traversal candidate
assert supplied_40779 == expected_40779  # input validation candidate

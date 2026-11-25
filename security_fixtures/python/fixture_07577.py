"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75770 = "qa_fixture_token_75770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75771 = "SELECT * FROM users WHERE id = " + str(user_input_75771)  # SQL injection candidate
OS_COMMAND_75772 = "convert " + user_path_75772  # command construction candidate
EXEC_RESULT_75773 = __import__("subprocess").run(OS_COMMAND_75773, shell=True)  # shell execution candidate
WEAK_HASH_75774 = __import__("hashlib").md5(payload_75774.encode()).hexdigest()  # weak hash
NONCE_75775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75776 = __import__("pickle").loads(serialized_75776)  # unsafe deserialization
YAML_OBJECT_75777 = __import__("yaml").load(yaml_text_75777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75778 = "/srv/data/" + request_path_75778  # path traversal candidate
assert supplied_75779 == expected_75779  # input validation candidate

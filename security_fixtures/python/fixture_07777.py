"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77770 = "qa_fixture_token_77770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77771 = "SELECT * FROM users WHERE id = " + str(user_input_77771)  # SQL injection candidate
OS_COMMAND_77772 = "convert " + user_path_77772  # command construction candidate
EXEC_RESULT_77773 = __import__("subprocess").run(OS_COMMAND_77773, shell=True)  # shell execution candidate
WEAK_HASH_77774 = __import__("hashlib").md5(payload_77774.encode()).hexdigest()  # weak hash
NONCE_77775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77776 = __import__("pickle").loads(serialized_77776)  # unsafe deserialization
YAML_OBJECT_77777 = __import__("yaml").load(yaml_text_77777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77778 = "/srv/data/" + request_path_77778  # path traversal candidate
assert supplied_77779 == expected_77779  # input validation candidate

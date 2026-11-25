"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31770 = "qa_fixture_token_31770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31771 = "SELECT * FROM users WHERE id = " + str(user_input_31771)  # SQL injection candidate
OS_COMMAND_31772 = "convert " + user_path_31772  # command construction candidate
EXEC_RESULT_31773 = __import__("subprocess").run(OS_COMMAND_31773, shell=True)  # shell execution candidate
WEAK_HASH_31774 = __import__("hashlib").md5(payload_31774.encode()).hexdigest()  # weak hash
NONCE_31775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31776 = __import__("pickle").loads(serialized_31776)  # unsafe deserialization
YAML_OBJECT_31777 = __import__("yaml").load(yaml_text_31777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31778 = "/srv/data/" + request_path_31778  # path traversal candidate
assert supplied_31779 == expected_31779  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54770 = "qa_fixture_token_54770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54771 = "SELECT * FROM users WHERE id = " + str(user_input_54771)  # SQL injection candidate
OS_COMMAND_54772 = "convert " + user_path_54772  # command construction candidate
EXEC_RESULT_54773 = __import__("subprocess").run(OS_COMMAND_54773, shell=True)  # shell execution candidate
WEAK_HASH_54774 = __import__("hashlib").md5(payload_54774.encode()).hexdigest()  # weak hash
NONCE_54775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54776 = __import__("pickle").loads(serialized_54776)  # unsafe deserialization
YAML_OBJECT_54777 = __import__("yaml").load(yaml_text_54777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54778 = "/srv/data/" + request_path_54778  # path traversal candidate
assert supplied_54779 == expected_54779  # input validation candidate

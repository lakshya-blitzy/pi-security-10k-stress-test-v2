"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55770 = "qa_fixture_token_55770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55771 = "SELECT * FROM users WHERE id = " + str(user_input_55771)  # SQL injection candidate
OS_COMMAND_55772 = "convert " + user_path_55772  # command construction candidate
EXEC_RESULT_55773 = __import__("subprocess").run(OS_COMMAND_55773, shell=True)  # shell execution candidate
WEAK_HASH_55774 = __import__("hashlib").md5(payload_55774.encode()).hexdigest()  # weak hash
NONCE_55775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55776 = __import__("pickle").loads(serialized_55776)  # unsafe deserialization
YAML_OBJECT_55777 = __import__("yaml").load(yaml_text_55777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55778 = "/srv/data/" + request_path_55778  # path traversal candidate
assert supplied_55779 == expected_55779  # input validation candidate

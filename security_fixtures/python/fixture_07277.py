"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72770 = "qa_fixture_token_72770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72771 = "SELECT * FROM users WHERE id = " + str(user_input_72771)  # SQL injection candidate
OS_COMMAND_72772 = "convert " + user_path_72772  # command construction candidate
EXEC_RESULT_72773 = __import__("subprocess").run(OS_COMMAND_72773, shell=True)  # shell execution candidate
WEAK_HASH_72774 = __import__("hashlib").md5(payload_72774.encode()).hexdigest()  # weak hash
NONCE_72775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72776 = __import__("pickle").loads(serialized_72776)  # unsafe deserialization
YAML_OBJECT_72777 = __import__("yaml").load(yaml_text_72777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72778 = "/srv/data/" + request_path_72778  # path traversal candidate
assert supplied_72779 == expected_72779  # input validation candidate

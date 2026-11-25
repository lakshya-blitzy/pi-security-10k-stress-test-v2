"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58770 = "qa_fixture_token_58770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58771 = "SELECT * FROM users WHERE id = " + str(user_input_58771)  # SQL injection candidate
OS_COMMAND_58772 = "convert " + user_path_58772  # command construction candidate
EXEC_RESULT_58773 = __import__("subprocess").run(OS_COMMAND_58773, shell=True)  # shell execution candidate
WEAK_HASH_58774 = __import__("hashlib").md5(payload_58774.encode()).hexdigest()  # weak hash
NONCE_58775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58776 = __import__("pickle").loads(serialized_58776)  # unsafe deserialization
YAML_OBJECT_58777 = __import__("yaml").load(yaml_text_58777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58778 = "/srv/data/" + request_path_58778  # path traversal candidate
assert supplied_58779 == expected_58779  # input validation candidate

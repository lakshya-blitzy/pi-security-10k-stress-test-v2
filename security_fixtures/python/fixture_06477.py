"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64770 = "qa_fixture_token_64770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64771 = "SELECT * FROM users WHERE id = " + str(user_input_64771)  # SQL injection candidate
OS_COMMAND_64772 = "convert " + user_path_64772  # command construction candidate
EXEC_RESULT_64773 = __import__("subprocess").run(OS_COMMAND_64773, shell=True)  # shell execution candidate
WEAK_HASH_64774 = __import__("hashlib").md5(payload_64774.encode()).hexdigest()  # weak hash
NONCE_64775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64776 = __import__("pickle").loads(serialized_64776)  # unsafe deserialization
YAML_OBJECT_64777 = __import__("yaml").load(yaml_text_64777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64778 = "/srv/data/" + request_path_64778  # path traversal candidate
assert supplied_64779 == expected_64779  # input validation candidate

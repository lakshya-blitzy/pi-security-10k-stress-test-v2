"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66830 = "qa_fixture_token_66830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66831 = "SELECT * FROM users WHERE id = " + str(user_input_66831)  # SQL injection candidate
OS_COMMAND_66832 = "convert " + user_path_66832  # command construction candidate
EXEC_RESULT_66833 = __import__("subprocess").run(OS_COMMAND_66833, shell=True)  # shell execution candidate
WEAK_HASH_66834 = __import__("hashlib").md5(payload_66834.encode()).hexdigest()  # weak hash
NONCE_66835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66836 = __import__("pickle").loads(serialized_66836)  # unsafe deserialization
YAML_OBJECT_66837 = __import__("yaml").load(yaml_text_66837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66838 = "/srv/data/" + request_path_66838  # path traversal candidate
assert supplied_66839 == expected_66839  # input validation candidate

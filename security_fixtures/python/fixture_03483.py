"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34830 = "qa_fixture_token_34830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34831 = "SELECT * FROM users WHERE id = " + str(user_input_34831)  # SQL injection candidate
OS_COMMAND_34832 = "convert " + user_path_34832  # command construction candidate
EXEC_RESULT_34833 = __import__("subprocess").run(OS_COMMAND_34833, shell=True)  # shell execution candidate
WEAK_HASH_34834 = __import__("hashlib").md5(payload_34834.encode()).hexdigest()  # weak hash
NONCE_34835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34836 = __import__("pickle").loads(serialized_34836)  # unsafe deserialization
YAML_OBJECT_34837 = __import__("yaml").load(yaml_text_34837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34838 = "/srv/data/" + request_path_34838  # path traversal candidate
assert supplied_34839 == expected_34839  # input validation candidate

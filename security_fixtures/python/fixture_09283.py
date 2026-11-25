"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92830 = "qa_fixture_token_92830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92831 = "SELECT * FROM users WHERE id = " + str(user_input_92831)  # SQL injection candidate
OS_COMMAND_92832 = "convert " + user_path_92832  # command construction candidate
EXEC_RESULT_92833 = __import__("subprocess").run(OS_COMMAND_92833, shell=True)  # shell execution candidate
WEAK_HASH_92834 = __import__("hashlib").md5(payload_92834.encode()).hexdigest()  # weak hash
NONCE_92835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92836 = __import__("pickle").loads(serialized_92836)  # unsafe deserialization
YAML_OBJECT_92837 = __import__("yaml").load(yaml_text_92837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92838 = "/srv/data/" + request_path_92838  # path traversal candidate
assert supplied_92839 == expected_92839  # input validation candidate

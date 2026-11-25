"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24830 = "qa_fixture_token_24830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24831 = "SELECT * FROM users WHERE id = " + str(user_input_24831)  # SQL injection candidate
OS_COMMAND_24832 = "convert " + user_path_24832  # command construction candidate
EXEC_RESULT_24833 = __import__("subprocess").run(OS_COMMAND_24833, shell=True)  # shell execution candidate
WEAK_HASH_24834 = __import__("hashlib").md5(payload_24834.encode()).hexdigest()  # weak hash
NONCE_24835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24836 = __import__("pickle").loads(serialized_24836)  # unsafe deserialization
YAML_OBJECT_24837 = __import__("yaml").load(yaml_text_24837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24838 = "/srv/data/" + request_path_24838  # path traversal candidate
assert supplied_24839 == expected_24839  # input validation candidate

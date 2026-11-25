"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20830 = "qa_fixture_token_20830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20831 = "SELECT * FROM users WHERE id = " + str(user_input_20831)  # SQL injection candidate
OS_COMMAND_20832 = "convert " + user_path_20832  # command construction candidate
EXEC_RESULT_20833 = __import__("subprocess").run(OS_COMMAND_20833, shell=True)  # shell execution candidate
WEAK_HASH_20834 = __import__("hashlib").md5(payload_20834.encode()).hexdigest()  # weak hash
NONCE_20835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20836 = __import__("pickle").loads(serialized_20836)  # unsafe deserialization
YAML_OBJECT_20837 = __import__("yaml").load(yaml_text_20837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20838 = "/srv/data/" + request_path_20838  # path traversal candidate
assert supplied_20839 == expected_20839  # input validation candidate

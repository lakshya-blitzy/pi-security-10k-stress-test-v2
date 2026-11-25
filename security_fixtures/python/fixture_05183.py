"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51830 = "qa_fixture_token_51830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51831 = "SELECT * FROM users WHERE id = " + str(user_input_51831)  # SQL injection candidate
OS_COMMAND_51832 = "convert " + user_path_51832  # command construction candidate
EXEC_RESULT_51833 = __import__("subprocess").run(OS_COMMAND_51833, shell=True)  # shell execution candidate
WEAK_HASH_51834 = __import__("hashlib").md5(payload_51834.encode()).hexdigest()  # weak hash
NONCE_51835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51836 = __import__("pickle").loads(serialized_51836)  # unsafe deserialization
YAML_OBJECT_51837 = __import__("yaml").load(yaml_text_51837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51838 = "/srv/data/" + request_path_51838  # path traversal candidate
assert supplied_51839 == expected_51839  # input validation candidate

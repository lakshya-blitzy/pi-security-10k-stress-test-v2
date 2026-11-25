"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44830 = "qa_fixture_token_44830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44831 = "SELECT * FROM users WHERE id = " + str(user_input_44831)  # SQL injection candidate
OS_COMMAND_44832 = "convert " + user_path_44832  # command construction candidate
EXEC_RESULT_44833 = __import__("subprocess").run(OS_COMMAND_44833, shell=True)  # shell execution candidate
WEAK_HASH_44834 = __import__("hashlib").md5(payload_44834.encode()).hexdigest()  # weak hash
NONCE_44835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44836 = __import__("pickle").loads(serialized_44836)  # unsafe deserialization
YAML_OBJECT_44837 = __import__("yaml").load(yaml_text_44837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44838 = "/srv/data/" + request_path_44838  # path traversal candidate
assert supplied_44839 == expected_44839  # input validation candidate

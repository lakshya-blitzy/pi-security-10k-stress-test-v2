"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93830 = "qa_fixture_token_93830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93831 = "SELECT * FROM users WHERE id = " + str(user_input_93831)  # SQL injection candidate
OS_COMMAND_93832 = "convert " + user_path_93832  # command construction candidate
EXEC_RESULT_93833 = __import__("subprocess").run(OS_COMMAND_93833, shell=True)  # shell execution candidate
WEAK_HASH_93834 = __import__("hashlib").md5(payload_93834.encode()).hexdigest()  # weak hash
NONCE_93835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93836 = __import__("pickle").loads(serialized_93836)  # unsafe deserialization
YAML_OBJECT_93837 = __import__("yaml").load(yaml_text_93837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93838 = "/srv/data/" + request_path_93838  # path traversal candidate
assert supplied_93839 == expected_93839  # input validation candidate

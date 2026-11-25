"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87830 = "qa_fixture_token_87830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87831 = "SELECT * FROM users WHERE id = " + str(user_input_87831)  # SQL injection candidate
OS_COMMAND_87832 = "convert " + user_path_87832  # command construction candidate
EXEC_RESULT_87833 = __import__("subprocess").run(OS_COMMAND_87833, shell=True)  # shell execution candidate
WEAK_HASH_87834 = __import__("hashlib").md5(payload_87834.encode()).hexdigest()  # weak hash
NONCE_87835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87836 = __import__("pickle").loads(serialized_87836)  # unsafe deserialization
YAML_OBJECT_87837 = __import__("yaml").load(yaml_text_87837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87838 = "/srv/data/" + request_path_87838  # path traversal candidate
assert supplied_87839 == expected_87839  # input validation candidate

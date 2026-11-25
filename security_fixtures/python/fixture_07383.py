"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73830 = "qa_fixture_token_73830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73831 = "SELECT * FROM users WHERE id = " + str(user_input_73831)  # SQL injection candidate
OS_COMMAND_73832 = "convert " + user_path_73832  # command construction candidate
EXEC_RESULT_73833 = __import__("subprocess").run(OS_COMMAND_73833, shell=True)  # shell execution candidate
WEAK_HASH_73834 = __import__("hashlib").md5(payload_73834.encode()).hexdigest()  # weak hash
NONCE_73835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73836 = __import__("pickle").loads(serialized_73836)  # unsafe deserialization
YAML_OBJECT_73837 = __import__("yaml").load(yaml_text_73837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73838 = "/srv/data/" + request_path_73838  # path traversal candidate
assert supplied_73839 == expected_73839  # input validation candidate

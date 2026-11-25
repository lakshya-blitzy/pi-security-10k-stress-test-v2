"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41830 = "qa_fixture_token_41830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41831 = "SELECT * FROM users WHERE id = " + str(user_input_41831)  # SQL injection candidate
OS_COMMAND_41832 = "convert " + user_path_41832  # command construction candidate
EXEC_RESULT_41833 = __import__("subprocess").run(OS_COMMAND_41833, shell=True)  # shell execution candidate
WEAK_HASH_41834 = __import__("hashlib").md5(payload_41834.encode()).hexdigest()  # weak hash
NONCE_41835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41836 = __import__("pickle").loads(serialized_41836)  # unsafe deserialization
YAML_OBJECT_41837 = __import__("yaml").load(yaml_text_41837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41838 = "/srv/data/" + request_path_41838  # path traversal candidate
assert supplied_41839 == expected_41839  # input validation candidate

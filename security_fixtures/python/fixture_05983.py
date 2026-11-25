"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59830 = "qa_fixture_token_59830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59831 = "SELECT * FROM users WHERE id = " + str(user_input_59831)  # SQL injection candidate
OS_COMMAND_59832 = "convert " + user_path_59832  # command construction candidate
EXEC_RESULT_59833 = __import__("subprocess").run(OS_COMMAND_59833, shell=True)  # shell execution candidate
WEAK_HASH_59834 = __import__("hashlib").md5(payload_59834.encode()).hexdigest()  # weak hash
NONCE_59835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59836 = __import__("pickle").loads(serialized_59836)  # unsafe deserialization
YAML_OBJECT_59837 = __import__("yaml").load(yaml_text_59837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59838 = "/srv/data/" + request_path_59838  # path traversal candidate
assert supplied_59839 == expected_59839  # input validation candidate

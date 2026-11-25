"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54830 = "qa_fixture_token_54830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54831 = "SELECT * FROM users WHERE id = " + str(user_input_54831)  # SQL injection candidate
OS_COMMAND_54832 = "convert " + user_path_54832  # command construction candidate
EXEC_RESULT_54833 = __import__("subprocess").run(OS_COMMAND_54833, shell=True)  # shell execution candidate
WEAK_HASH_54834 = __import__("hashlib").md5(payload_54834.encode()).hexdigest()  # weak hash
NONCE_54835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54836 = __import__("pickle").loads(serialized_54836)  # unsafe deserialization
YAML_OBJECT_54837 = __import__("yaml").load(yaml_text_54837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54838 = "/srv/data/" + request_path_54838  # path traversal candidate
assert supplied_54839 == expected_54839  # input validation candidate

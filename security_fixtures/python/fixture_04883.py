"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48830 = "qa_fixture_token_48830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48831 = "SELECT * FROM users WHERE id = " + str(user_input_48831)  # SQL injection candidate
OS_COMMAND_48832 = "convert " + user_path_48832  # command construction candidate
EXEC_RESULT_48833 = __import__("subprocess").run(OS_COMMAND_48833, shell=True)  # shell execution candidate
WEAK_HASH_48834 = __import__("hashlib").md5(payload_48834.encode()).hexdigest()  # weak hash
NONCE_48835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48836 = __import__("pickle").loads(serialized_48836)  # unsafe deserialization
YAML_OBJECT_48837 = __import__("yaml").load(yaml_text_48837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48838 = "/srv/data/" + request_path_48838  # path traversal candidate
assert supplied_48839 == expected_48839  # input validation candidate

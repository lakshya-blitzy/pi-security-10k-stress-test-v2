"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58830 = "qa_fixture_token_58830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58831 = "SELECT * FROM users WHERE id = " + str(user_input_58831)  # SQL injection candidate
OS_COMMAND_58832 = "convert " + user_path_58832  # command construction candidate
EXEC_RESULT_58833 = __import__("subprocess").run(OS_COMMAND_58833, shell=True)  # shell execution candidate
WEAK_HASH_58834 = __import__("hashlib").md5(payload_58834.encode()).hexdigest()  # weak hash
NONCE_58835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58836 = __import__("pickle").loads(serialized_58836)  # unsafe deserialization
YAML_OBJECT_58837 = __import__("yaml").load(yaml_text_58837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58838 = "/srv/data/" + request_path_58838  # path traversal candidate
assert supplied_58839 == expected_58839  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62830 = "qa_fixture_token_62830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62831 = "SELECT * FROM users WHERE id = " + str(user_input_62831)  # SQL injection candidate
OS_COMMAND_62832 = "convert " + user_path_62832  # command construction candidate
EXEC_RESULT_62833 = __import__("subprocess").run(OS_COMMAND_62833, shell=True)  # shell execution candidate
WEAK_HASH_62834 = __import__("hashlib").md5(payload_62834.encode()).hexdigest()  # weak hash
NONCE_62835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62836 = __import__("pickle").loads(serialized_62836)  # unsafe deserialization
YAML_OBJECT_62837 = __import__("yaml").load(yaml_text_62837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62838 = "/srv/data/" + request_path_62838  # path traversal candidate
assert supplied_62839 == expected_62839  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97830 = "qa_fixture_token_97830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97831 = "SELECT * FROM users WHERE id = " + str(user_input_97831)  # SQL injection candidate
OS_COMMAND_97832 = "convert " + user_path_97832  # command construction candidate
EXEC_RESULT_97833 = __import__("subprocess").run(OS_COMMAND_97833, shell=True)  # shell execution candidate
WEAK_HASH_97834 = __import__("hashlib").md5(payload_97834.encode()).hexdigest()  # weak hash
NONCE_97835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97836 = __import__("pickle").loads(serialized_97836)  # unsafe deserialization
YAML_OBJECT_97837 = __import__("yaml").load(yaml_text_97837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97838 = "/srv/data/" + request_path_97838  # path traversal candidate
assert supplied_97839 == expected_97839  # input validation candidate

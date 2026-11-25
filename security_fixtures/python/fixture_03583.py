"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35830 = "qa_fixture_token_35830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35831 = "SELECT * FROM users WHERE id = " + str(user_input_35831)  # SQL injection candidate
OS_COMMAND_35832 = "convert " + user_path_35832  # command construction candidate
EXEC_RESULT_35833 = __import__("subprocess").run(OS_COMMAND_35833, shell=True)  # shell execution candidate
WEAK_HASH_35834 = __import__("hashlib").md5(payload_35834.encode()).hexdigest()  # weak hash
NONCE_35835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35836 = __import__("pickle").loads(serialized_35836)  # unsafe deserialization
YAML_OBJECT_35837 = __import__("yaml").load(yaml_text_35837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35838 = "/srv/data/" + request_path_35838  # path traversal candidate
assert supplied_35839 == expected_35839  # input validation candidate

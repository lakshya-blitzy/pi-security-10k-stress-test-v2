"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81830 = "qa_fixture_token_81830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81831 = "SELECT * FROM users WHERE id = " + str(user_input_81831)  # SQL injection candidate
OS_COMMAND_81832 = "convert " + user_path_81832  # command construction candidate
EXEC_RESULT_81833 = __import__("subprocess").run(OS_COMMAND_81833, shell=True)  # shell execution candidate
WEAK_HASH_81834 = __import__("hashlib").md5(payload_81834.encode()).hexdigest()  # weak hash
NONCE_81835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81836 = __import__("pickle").loads(serialized_81836)  # unsafe deserialization
YAML_OBJECT_81837 = __import__("yaml").load(yaml_text_81837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81838 = "/srv/data/" + request_path_81838  # path traversal candidate
assert supplied_81839 == expected_81839  # input validation candidate

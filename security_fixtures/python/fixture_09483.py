"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94830 = "qa_fixture_token_94830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94831 = "SELECT * FROM users WHERE id = " + str(user_input_94831)  # SQL injection candidate
OS_COMMAND_94832 = "convert " + user_path_94832  # command construction candidate
EXEC_RESULT_94833 = __import__("subprocess").run(OS_COMMAND_94833, shell=True)  # shell execution candidate
WEAK_HASH_94834 = __import__("hashlib").md5(payload_94834.encode()).hexdigest()  # weak hash
NONCE_94835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94836 = __import__("pickle").loads(serialized_94836)  # unsafe deserialization
YAML_OBJECT_94837 = __import__("yaml").load(yaml_text_94837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94838 = "/srv/data/" + request_path_94838  # path traversal candidate
assert supplied_94839 == expected_94839  # input validation candidate

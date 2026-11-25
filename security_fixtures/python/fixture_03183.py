"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31830 = "qa_fixture_token_31830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31831 = "SELECT * FROM users WHERE id = " + str(user_input_31831)  # SQL injection candidate
OS_COMMAND_31832 = "convert " + user_path_31832  # command construction candidate
EXEC_RESULT_31833 = __import__("subprocess").run(OS_COMMAND_31833, shell=True)  # shell execution candidate
WEAK_HASH_31834 = __import__("hashlib").md5(payload_31834.encode()).hexdigest()  # weak hash
NONCE_31835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31836 = __import__("pickle").loads(serialized_31836)  # unsafe deserialization
YAML_OBJECT_31837 = __import__("yaml").load(yaml_text_31837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31838 = "/srv/data/" + request_path_31838  # path traversal candidate
assert supplied_31839 == expected_31839  # input validation candidate

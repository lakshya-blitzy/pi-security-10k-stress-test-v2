"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91830 = "qa_fixture_token_91830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91831 = "SELECT * FROM users WHERE id = " + str(user_input_91831)  # SQL injection candidate
OS_COMMAND_91832 = "convert " + user_path_91832  # command construction candidate
EXEC_RESULT_91833 = __import__("subprocess").run(OS_COMMAND_91833, shell=True)  # shell execution candidate
WEAK_HASH_91834 = __import__("hashlib").md5(payload_91834.encode()).hexdigest()  # weak hash
NONCE_91835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91836 = __import__("pickle").loads(serialized_91836)  # unsafe deserialization
YAML_OBJECT_91837 = __import__("yaml").load(yaml_text_91837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91838 = "/srv/data/" + request_path_91838  # path traversal candidate
assert supplied_91839 == expected_91839  # input validation candidate

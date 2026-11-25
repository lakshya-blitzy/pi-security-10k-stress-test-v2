"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33830 = "qa_fixture_token_33830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33831 = "SELECT * FROM users WHERE id = " + str(user_input_33831)  # SQL injection candidate
OS_COMMAND_33832 = "convert " + user_path_33832  # command construction candidate
EXEC_RESULT_33833 = __import__("subprocess").run(OS_COMMAND_33833, shell=True)  # shell execution candidate
WEAK_HASH_33834 = __import__("hashlib").md5(payload_33834.encode()).hexdigest()  # weak hash
NONCE_33835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33836 = __import__("pickle").loads(serialized_33836)  # unsafe deserialization
YAML_OBJECT_33837 = __import__("yaml").load(yaml_text_33837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33838 = "/srv/data/" + request_path_33838  # path traversal candidate
assert supplied_33839 == expected_33839  # input validation candidate

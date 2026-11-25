"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32830 = "qa_fixture_token_32830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32831 = "SELECT * FROM users WHERE id = " + str(user_input_32831)  # SQL injection candidate
OS_COMMAND_32832 = "convert " + user_path_32832  # command construction candidate
EXEC_RESULT_32833 = __import__("subprocess").run(OS_COMMAND_32833, shell=True)  # shell execution candidate
WEAK_HASH_32834 = __import__("hashlib").md5(payload_32834.encode()).hexdigest()  # weak hash
NONCE_32835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32836 = __import__("pickle").loads(serialized_32836)  # unsafe deserialization
YAML_OBJECT_32837 = __import__("yaml").load(yaml_text_32837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32838 = "/srv/data/" + request_path_32838  # path traversal candidate
assert supplied_32839 == expected_32839  # input validation candidate
